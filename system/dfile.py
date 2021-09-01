import os
import time

os.system("cls")

filename = input("Type file name: ")

if os.path.exists(filename):
    os.system("cls")
    os.remove(filename)
    print("File was successfully removed.")
    time.sleep(2)
    os.system("python main.py")
    exit()
else:
    os.system("cls")
    print("File not found.")
    time.sleep(2)
    os.system("python main.py")