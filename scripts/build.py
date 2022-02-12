# Copyright 2022 iiPython
# Build the installer.zip file

# Modules
import os
import shutil
import zipfile
import subprocess

# Initialization
if not os.path.isdir("python") and os.name == "nt":
    print("You need to have a 'python' directory containing the Python 3.10 runtime.")
    print("Download Python from https://python.org")
    exit(1)

to_include = [f for f in os.listdir() if f not in [
    ".git", "__pycache__", "scripts", ".xtconfig", "main.xt",
    "build", "dist", "installer.py", "installer.spec"
]]
print("Including all of the following:\n", "\n\t-  ".join([""] + to_include).lstrip("\n"))
if not input("\nIs this correct (y/N)? ").lower() == "y":
    exit(1)

python = "py" if os.name == "nt" else "python3"
x2_version = input("x2 version: ")

# Handle build dir
if os.path.isdir("build"):
    shutil.rmtree("build")

os.mkdir("build")
print()

# Build our zip file
print("Zipping to package.zip ...")
with zipfile.ZipFile("build/package.zip", "w") as zf:
    for fn in to_include:
        if os.path.isfile(fn):
            zf.write(fn, fn)

        else:
            for path, _, files in os.walk(fn):
                if "__pycache__" in path:
                    continue

                for file in files:
                    fp = os.path.join(path, file)
                    zf.write(fp, fp)

print("  ..done!")

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

# Build zip file
print("\nBuilding x2.zip ...")
with zipfile.ZipFile("x2.zip", "w") as zf:
    [zf.write(f) for f in ["package.zip", install_file]]

print("  ..done!")

# Clean up build directory
print("\nCleaning build directory ...")
for item in os.listdir():
    if item == "x2.zip":
        continue

    elif os.path.isfile(item):
        os.remove(item)

    else:
        shutil.rmtree(item)

print("  ..done!")
os.chdir("../")
