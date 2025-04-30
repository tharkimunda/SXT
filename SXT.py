import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    chmod 777 SXT64
    ./SXT64
elif bit == '32bit':
    chmod 777 SXT
    ./SXT
