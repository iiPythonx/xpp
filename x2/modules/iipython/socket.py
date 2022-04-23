# Copyright 2022 iiPython

# Wrapper for the builtin Python socket module
# It includes basic encryption using Python cryptography

# Modules
import json
import socket
import base64
from typing import Any, List
from types import FunctionType
from copy import copy as copyobj

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF

except ImportError:
    Fernet, hashes, serialization, ec, HKDF = None, None, None, None, None

# Initialization
def _wrap_obj(parent: object, obj: FunctionType, name: str, new: FunctionType) -> None:
    setattr(parent, name, copyobj(obj))
    setattr(parent, obj.__name__, new)

# Classes
class Socket(socket.socket):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        _wrap_obj(self, self.connect, "_sock_connect", self._connect_wrap)

    def _connect_wrap(self, *args, **kwargs) -> None:
        self._sock_connect(*args, **kwargs)
        self.handshake()

    def _send_wrap(self, content: str) -> None:
        payload = self._fernet.encrypt(content.encode("utf8"))
        self.sendall(payload + b"\x00")

    def _recv_wrap(self) -> List[str]:
        data = b""
        while self:
            chnk = self._sock_recv(2048)
            data += chnk
            if not chnk or chnk[-1:] == b"\x00":
                break

        if not data:
            return []

        return [self._fernet.decrypt(msg).decode("utf8") for msg in data.split(b"\x00") if msg]

    def sendjson(self, data: dict) -> None:
        self._send_wrap(json.dumps(data))

    def recvjson(self) -> List[Any]:
        try:
            return [json.loads(msg) for msg in self._recv_wrap()]

        except TypeError:
            raise OSError  # Connection error, drop connection

    def handshake(self) -> None:
        self._private_key = ec.generate_private_key(ec.SECP384R1())
        server_public = serialization.load_pem_public_key(self.recv(2048))
        self._shared_key = HKDF(
            algorithm = hashes.SHA256(),
            length = 32,
            salt = None,
            info = None
        ).derive(self._private_key.exchange(ec.ECDH(), server_public))
        self.sendall(
            self._private_key.public_key().public_bytes(
                encoding = serialization.Encoding.PEM,
                format = serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

        self._fernet = Fernet(base64.urlsafe_b64encode(self._shared_key))
        _wrap_obj(self, self.send, "_sock_send", self._send_wrap)
        _wrap_obj(self, self.recv, "_sock_recv", self._recv_wrap)

class Connection(object):
    def __init__(self, sock: socket.socket) -> None:
        self.sock = sock
        self.handshake()

    def handshake(self) -> None:
        self._private_key = ec.generate_private_key(ec.SECP384R1())
        self.sock.sendall(
            self._private_key.public_key().public_bytes(
                encoding = serialization.Encoding.PEM,
                format = serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
        client_public = serialization.load_pem_public_key(self.sock.recv(2048))
        self._shared_key = HKDF(
            algorithm = hashes.SHA256(),
            length = 32,
            salt = None,
            info = None
        ).derive(self._private_key.exchange(ec.ECDH(), client_public))
        self._fernet = Fernet(base64.urlsafe_b64encode(self._shared_key))

    def send(self, content: str) -> None:
        payload = self._fernet.encrypt(content.encode("utf8"))
        self.sock.sendall(payload + b"\x00")

    def sendjson(self, data: dict) -> None:
        self.send(json.dumps(data))

    def recv(self) -> List[str]:
        data = b""
        while self.sock:
            chnk = self.sock.recv(2048)
            data += chnk
            if not chnk or chnk[-1:] == b"\x00":
                break

        if not data:
            return []

        return [self._fernet.decrypt(msg).decode("utf8") for msg in data.split(b"\x00") if msg]

    def recvjson(self) -> List[Any]:
        try:
            return [json.loads(msg) for msg in self.recv()]

        except TypeError:
            raise OSError  # Connection error, drop connection
