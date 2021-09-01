import os

os.system("cls")

while True:
    ucommand = input("MyTerminal >> ")
    if (ucommand == "-help"):
        os.system("cls")
        print("""
Commands:
    -about (Get information about the owner)
    -dfile (Delete a file with this command)
    -dfolder (Delete a folder with this command)
    -rfile (Change name of your file)
    -rfolder (Change name of your folder)
    -clean (Clears the active Terminal text)
    -message (Prints the text)
    -quit (Quit MyTerminal)
        """)
    elif (ucommand == "-about"):
        os.system("cls")
        print("""
MyTerminal (v0.5)
    
    This basic Terminal is created by Techie Pawan.
    For more information, search Techie Pawandeep Singh
    on YouTube.
        """)
    elif (ucommand == "-dfile"):
        os.system("cls")
        os.system("python system/dfile.py")
        exit()
    elif (ucommand == "-dfolder"):
        os.system("cls")
        os.system("python system/dfolder.py")
        exit()
    elif (ucommand == "-clean"):
        os.system("cls")
    elif (ucommand == "-quit"):
        os.system("cls")
        exit()
    elif (ucommand == "-rfile"):
        os.system("cls")
        os.system("python system/rfile.py")
        exit()
    elif (ucommand == "-rfolder"):
        os.system("cls")
        os.system("python system/rfolder.py")
        exit()
    elif (ucommand == "-message"):
        os.system("cls")
        getmessage = input("Type your message: ")
        print(getmessage)
    else:
        os.system("cls")
        print("Invalid command:", ucommand)

# MyTerminal.
# See you in next video, BYE BYE.
# Techie Pawan.