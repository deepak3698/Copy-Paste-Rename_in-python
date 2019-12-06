import shutil
import re
import os

def copy_withregx(path,path2):
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        dt = re.findall(r"[#][0-9]+", file)
        val = int(dt[0][1:])
        if (val > 51 and val < 71):
            shutil.copy2(f'{path}\{file}', f'{path2}')

def rename(path):
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        dt = re.findall(r"[#][0-9]+", file)
        val = int(dt[0][1:])
        os.rename(f"{file}", f"{val}.mp4")


path=""   #the path where you want to do changes/or from where you want to copy the data

path2=""    # the path where you want to copy the data


# copy_withregx(path,path2)

# rename(path)







