#!/usr/bin/python3

import os
import platform

def PrintLogo():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    print("Welcome to")
    print(" _   _ ____   ____            ")
    print("| \ | | __ ) / ___|___  _ __  ")
    print("|  \| |  _ \| |   / _ \| '_ \ ")
    print("| |\  | |_) | |__| (_) | | | |")
    print("|_| \_|____/ \____\___/|_| |_|")
    print()
    print("Number Base Converter")
    print("            {Directed ByABGEO}")
    print()
#end PrintLogo

def Convert(num, to_base, from_base = 10):
        if isinstance(num, str):
                n = int(num, from_base)
        else:
                n = int(num)

        Alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if n < to_base:
                return Alphabet[n]
        else:
                return Convert(n // to_base, to_base) + Alphabet[n % to_base]
#end Convert

def StartConverting():
    PrintLogo()

    try:
        FromBase = int(input ("From Base (Ex.: 10): "))
    except ValueError:
        print ("This is not a number!")
        FromBase = int(input ("From Base (Ex.: 10): "))

    try:
        ToBase = int(input("To Base (Ex.: 2): "))
    except ValueError:
        print ("This is not a number!")
        ToBase = int(input("To Base (Ex.: 2): "))

    Number = str(input ("Enter Number in " + str(FromBase) + " Base Numeric System:  "))

    print(str(Number) + " in (" + str(FromBase) + ") = " + Convert(Number, ToBase, FromBase) + " in (" + str(ToBase) + ")")

    TryAgain = input ("Try Again [y/n]? ")

    if TryAgain == 'y' or TryAgain == 'Y':
        StartConverting()
    else:
        print("Bye")
#End StartConverting

Action = input ("Enter 'help' for get information about NBCon\n" +
"or 'convert' for start converting: ")

if Action == 'help':
    PrintLogo()
    print("...help...")
elif Action == 'convert':
    StartConverting()
else:
    print("Incorect Command...")
