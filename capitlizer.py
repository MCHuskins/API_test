import os
import argparse

#

parser = argparse.ArgumentParser(description='recursivley capitals all files in a directory.')
parser.add_argument("target_directory", default=".")
parser.add_argument("-l",  action="store_true")

args = parser.parse_args()

directory_look_at = args.target_directory
lowercase = args.l

def modify(word):
    if lowercase:
        return word.lower()
    else:
        return word.upper()

def addpath(filepath, nname):
    return filepath[0:len(nname)*-1] + nname

def rename(filepath):
    nname= modify(os.path.basename(filepath))
    newfilename = addpath(filepath, nname)
    os.rename(filepath, newfilename)

def recursivefilename(directory):
   for each in os.listdir(directory):
       d_e = os.path.join(directory,each)
       if os.path.isfile(d_e):
           rename(d_e)
       if os.path.isdir(d_e):
           recursivefilename(d_e)

recursivefilename(directory_look_at)
