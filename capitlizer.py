import os

def capital(word):
    return word.lower()

def addpath(filepath, nname):
    return filepath[0:len(nname)*-1] + nname

def rename(filepath):
    nname= capital(os.path.basename(filepath))
    newfilename = addpath(filepath, nname)
    os.rename(filepath, newfilename)

def recursivefilename(directory):
    for each in os.listdir(directory):
        if os.path.isfile(directory + "/" + each):
            rename(directory + "/" + each)
        if os.path.isdir(directory + "/" + each):
            recursivefilename(directory + "/" + each)

recursivefilename("./target_folder")
