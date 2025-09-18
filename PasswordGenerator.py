#In diesem mini-Projekt möchte ich einen password generator erstellen.

#! ToDO: 
#!          1. args verarbeiten.
#!          2. Konsolen Ansicht verschönern

#? Ziel: Ein Password Generator, der Viele arten von Passwörtern erstellen kann. (Ohne "import random")

#Importe
import time
import argparse

def randomNum(maxnumber):
    global seed
    timeNow = time.time()
    number = int((timeNow - int(timeNow)) * 1000000)
    return number%maxnumber

def generate_password(length,uppercase,lowercase,special,number):
    
    #init Vars
    Password = ""
    UppercaseGlobal = False
    LowercaseGlobal = False
    NumberGlobal = False
    SpecialCharacterGlobal = False
    
    #Kontrolle für länge
    # EIn bisschen Simpel aber OK
    if length < 4:
        UppercaseGlobal = True
        LowercaseGlobal = True
        NumberGlobal = True
        SpecialCharacterGlobal = True

    for i in range(length):
        
        Listlength = len(ListOfCharacters)
        while True:
            NewChar = str(ListOfCharacters[randomNum(Listlength)]) #My bad
            time.sleep(0.00001) #Konnte ja keiner ahnen...🚬
            if  uppercase == False and NewChar.isupper():
                UppercaseGlobal = True
                print("44")
                continue
            if lowercase == False  and NewChar.islower():
                LowercaseGlobal = True
                continue
            if special == False  and not NewChar.isalnum():
                SpecialCharacterGlobal = True
                continue
            if number == False  and NewChar.isdigit():
                NumberGlobal = True
                continue
            Password += NewChar
            break
        if Password[i].isupper():
            UppercaseGlobal = True
        elif Password[i].islower():
            LowercaseGlobal = True
        elif Password[i].isdigit():
            NumberGlobal = True
        else:
            SpecialCharacterGlobal = True
    if not UppercaseGlobal or not LowercaseGlobal or not NumberGlobal or not SpecialCharacterGlobal:
        return generate_password(length,uppercase,lowercase,special,number)#Hier würde er die Recursion erzeugen. 
    return Password


# Diese Funktion gibt mir die Args aus dem Commandline als Dict zurück
# PARAMETER: none
# RETURN: dict with args
def get_args():
    parser = argparse.ArgumentParser(
    prog="pwgem",
    description="Helps you to create a strong Password",
    epilog="This Program is made by LutzoLab"
)
    #--help fällt raus... Das macht argparser alleine
    parser.add_argument("-l", "--length", type=int, help="Length of the password")
    parser.add_argument("-c", "--charlist", type=str, help="Custom character list to use")
    parser.add_argument("-up", "--uppercase", type=bool, help="Include uppercase letters")
    parser.add_argument("-low", "--lowercase", type=bool, help="Include lowercase letters")
    parser.add_argument("-sp", "--special", type=bool, help="Include special characters")
    parser.add_argument("-num", "--number", type=bool, help="Include numbers")
    parser.add_argument("-save", "--save", type=bool, help="Save the password as a .txt file")

    # create Namespace with all args
    
    args = parser.parse_args()
    print(type(args.uppercase))
    print(args.uppercase == "False")
    return vars(args)

if __name__=="__main__":
    print("<PWGEN>")
    #Hier werden die Args geprüft
    args = get_args()
    
    #Handel CharList
    ListOfCharacters = []
    if args["charlist"] != None:
        try:
            with open(args["charlist"],"r") as file:
                for line in file:
                    for i in line:
                        ListOfCharacters.append(i)
        except Exception as e:
            print(f"Can't open file: -> {e}")
    else:
        CharSet = r"!#$%&()*+-/0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]_abcdefghijklmnopqrstuvwxyz{}~"
        
        for i in CharSet:
            ListOfCharacters.append(i)
    passwordLength = args["length"]
    if not passwordLength:
        passwordLength = 8
    print(args)
    print(type(args["uppercase"]))
    print(args["uppercase"])
    print(generate_password(passwordLength,args["uppercase"],args["lowercase"],args["special"],args["number"]))