import os
import shutil
from_dir="C:/Users/teva_/Downloads"
to_dir="C:/Users/teva_/Downloads/downloadedImages"
list_of_files=os.listdir(from_dir)
#print(list_of_files)
for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    #print(name)
   #print(extension)
    if extension == "":
        continue
    if extension in[".txt",".pdf",".doc",".docx"]:
        #moving files from downloads folder to downloadImages folder
        path1=from_dir+"/"+filename
        #checking inside the downloadedimages folder whether images file folder is created ot not
        path2=to_dir+"/"+"Document_Files"
        #moving from director to directory
        path3=to_dir+"/"+"Document_Files"+"/"+filename

        #check if folder/directory exists before moving the files
        if os.path.exists(path2):
            print("moving"+filename+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+filename+"...")
            shutil.move(path1,path3)


