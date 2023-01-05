# Copyright 2022 iiPython
# Build the installer.zip file

# Modules
import os
import shutil
import subprocess

# Initialization
if not os.path.isdir("python") and os.name == "nt":
    print("You need to have a 'python' directory containing the Python 3.10 runtime.")
    print("Download Python from https://python.org")
    exit(1)

python = "py" if os.name == "nt" else "python3"

# Handle build dir
if os.path.isdir("build"):
    shutil.rmtree("build")

os.mkdir("build")

# Copy installer.py
print("\nCopying installer.py ...")
shutil.copy("scripts/installer.py", "build/installer.py")
print("  ..done!")

# Build with pyinstaller
print("\nBuilding exe ...")
if not shutil.which("pyinstaller"):
    if (input("Pyinstaller was not detected, install it (Y/n)? ") or "y").lower() == "y":
        subprocess.run([python, "-m", "pip", "install", "-U", "pyinstaller"], stdout = subprocess.PIPE)
        print("  ..installed!")

    else:
        print("You need pyinstaller to build the exe, rerun this script once it is installed.")
        exit(1)

os.chdir("build")
subprocess.run(["pyinstaller", "-i", "../scripts/assets/x2.ico", "-F", "installer.py"], stderr = subprocess.PIPE)

install_file = "installer.exe" if os.name == "nt" else "installer"
shutil.move(f"dist/{install_file}", f"./{install_file}")
print("  ..done!")

# Clean up build directory
print("\nCleaning build directory ...")
for item in os.listdir():
    if item in ["installer", "installer.exe"]:
        continue

    elif os.path.isfile(item):
        os.remove(item)

    else:
        shutil.rmtree(item)

print("  ..done!")
os.chdir("../")
