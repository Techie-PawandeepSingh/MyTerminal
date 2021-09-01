import os
import time

os.system("cls")

foldername = input("Type folder name: ")

if os.path.exists(foldername):
    os.system("cls")
    os.rmdir(foldername)
    print("Folder was successfully removed.")
    time.sleep(2)
    os.system("python main.py")
else:
    os.system("cls")
    print("Folder not found.")
    time.sleep(2)
    os.system("python main.py")