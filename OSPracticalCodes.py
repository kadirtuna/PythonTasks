#OS Library
import os

print(os.name)#nt=Windows, posx=Linux

currentDir = os.getcwd()
print(currentDir)

folderName = "New_Folder"
os.mkdir(folderName)

newFolderName = "New_Folder_2"
os.rename(folderName, newFolderName)

os.chdir(os.getcwd() + "\\" + newFolderName)
print(os.getcwd())

files = os.listdir()
print(files)

for f in files:
    if f.endswith(".py"):
        print(f)
        
os.rmdir(newFolderName)

for i in os.walk(currentDir):
    print(i)

os.path.exists("OSPracticalCodes.py")
os.path.exists("OSPracticalCodes2.py")
