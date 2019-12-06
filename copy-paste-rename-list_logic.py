import shutil
import os

def copy_withlistlogic(path,path2):
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        a=file[len(file)-6]
        b=file[len(file)-5]
        try:
            c=int(a+b)
        except:
            pass
        if(c>51 and c<71):
            shutil.copy2(f'{path}\{file}', f'{path2}')


def rename(path):
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        a = file[len(file) - 6]
        b = file[len(file) - 5]
        try:
            c = int(a + b)
        except:
            pass
        try:
            os.rename(f"{file}", f"{c}.mp4")
        except:
            pass

path=""   #the path where you want to do changes/or from where you want to copy the data

path2=""    # the path where you want to copy the data


# copy_withlistlogic(path,path2)

# rename(path)





