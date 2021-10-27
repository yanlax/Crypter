import os
import pyAesCrypt
import random


def crypter (_mode, _file):
    
    passworld = ''.join([random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNM123456789')) for x in range(12)])
    buffer = 512 * 1024
    ext = _file.split(".")

    if(int(_mode) == 0):
        pyAesCrypt.encryptFile(_file, ext[0].lower() + ".yl", passworld, buffer)
        
        print(" Your passworld: " + passworld)

        os.remove(_file)
        input()

    elif(int(_mode) == 1):
        passworld1 = input(" Enter passworld: ")
        _type = input(" Enter Type: ")
        pyAesCrypt.decryptFile(_file, ext[0].lower() + '.' + _type, passworld1, buffer)

        os.remove(_file)
        input()
print(" ---------------------------------------------------------")
print(" ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░")
print(" ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗")
print(" ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██████╔╝")
print(" ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗")
print(" ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██║░░██║")
print(" ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
print(" ----------------------- By YanLax -----------------------")
print(" 0 - Crypt")
print(" 1 - Decrypt")

mode = input(" Enter mode: ")
filename = input(" Enter file name: ")
crypter(mode, filename)



