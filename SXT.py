import os
import platform

arch = platform.machine()

if arch == "x86_64":
    print("64-bit system detected.")
    os.system("chmod 777 SXT64")
    os.system("./SXT64")
elif arch in ["i386", "i686"]:
    print("32-bit system detected.")
    os.system("chmod 777 SXT")
    os.system("./SXT")
else:
    print(f"Unknown architecture: {arch}")
