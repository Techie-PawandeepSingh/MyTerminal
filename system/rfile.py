import os
import time

os.system("cls")

oldname = input("Type file name: ")

if os.path.exists(oldname):
    os.system("cls")
    newname = input("Type new name: ")
    os.rename(oldname, newname)
    print("File name was successfully changed.")
    time.sleep(2)
    os.system("python main.py")
    exit()
else:
    os.system("cls")
    print("File not found.")
    time.sleep(2)
    os.system("python main.py")
    exit()