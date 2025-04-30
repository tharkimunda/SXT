import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system("chmod 777 SXT64")
    os.system("./SXT64")
elif bit == '32bit':
    os.system("chmod 777 SXT")
    os.system("SXT")
