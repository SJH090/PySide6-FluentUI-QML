import subprocess
import sys

import env

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    subprocess.run([env.pip(), "install", "PySide6==6.10.0"])
    # subprocess.run([env.pip(), "install", "nuitka==2.7.13"])
    # subprocess.run([env.pip(), "install", "PyInstaller==6.15.0"])
    subprocess.run([env.pip(), "install", "qasync==0.28.0"])
    subprocess.run([env.pip(), "install", "aiohttp==3.13.1"])
    subprocess.run([env.pip(), "install", "qrcode==8.2"])
    subprocess.run([env.pip(), "install", "pillow==12.0.0"])
    subprocess.run([env.pip(), "install", "keyboard==0.13.5"])
    subprocess.run([env.pip(), "install", "PyOpenGL==3.1.10"])
    subprocess.run([env.pip(), "install", "py7zr==1.0.0"])
