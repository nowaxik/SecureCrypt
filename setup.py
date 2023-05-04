import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="SecureCrypt",
    version="1.0",
    description="Szyfrowanie plików. Program napisany tylko i wyłącznie dla własnego użytku.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)