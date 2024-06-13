import zipfile
from lector.rarfile import rarfile
import os,shutil


def Takeout(inside_path:str):
    listdir = os.listdir(inside_path)
    listdir.sort()
    print(inside_path.split("/")[-1])
    for i1 in listdir:
        if os.path.isfile(inside_path+"/"+i1):
            ext = os.path.splitext(i1)
            if ext[1] not in [".png",".jpeg",".jpg",".bmp"] :
                new_fname = inside_path+" - "+ext[0]+".png"
                os.rename(inside_path+"/"+i1,new_fname)
            else:
                os.rename(inside_path+"/"+i1,inside_path+" - "+i1)
        else:
            Takeout(inside_path+"/"+i1)
            shutil.rmtree(inside_path)
    pass

def do_rpk(path:str,RMold:bool=False):

    extractpath = os.path.dirname(path)+"/"+path.split("/")[-1][:-4]

    try:
        shutil.rmtree(extractpath)
        print("removed",extractpath)
    except Exception as err:
        print(err)

    if path.lower().endswith("cbz"):
        rf = rarfile.RarFile(path)
        rf.extractall(extractpath)
        extracted = os.listdir(extractpath)
        rf.close()
        for folder in extracted:
            Takeout(extractpath+"/"+folder)
        New_name = os.path.dirname(path)+"/"+path.split("/")[-1].replace("[@Bos_library]","[@Bos_library] [FIXED BY tank]")
        try:
            os.remove(New_name)
        except:
            pass

        with zipfile.ZipFile(New_name,"x") as zf:
            for i in os.listdir(extractpath):
                zf.write(extractpath+"/"+i,i)
            zf.close()

    try:
        shutil.rmtree(extractpath)
        if RMold:
            shutil.rmtree(path)
    except Exception as err:
        print(err)
    return New_name
