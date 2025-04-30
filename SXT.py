import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    print sorry
elif bit == '32bit':
    import SXT
