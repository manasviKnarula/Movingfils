import os;
import shutil;

path = input("enter the source folder: ")
path1 = input("enter the destination folder: ")


list_of_files = os.listdir(path+"/")

for file in list_of_files:
    shutil.copy((path+"/"+file),(path1+"/"))
