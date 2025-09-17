#In diesem mini-Projekt möchte ich einen password generator erstellen.

#! ToDO:    1. Recursions wahrscheinlichkeit rausnehmen
#!          2. argparser hinzufügen
#!          3. Zeichen liste In hardcode setzten + Möglichkeit eigene Sammlungen zu benutzen 
#!          4. Konsolen Ansicht verschönern

#? Ziel: Ein Password Generator, der Viele arten von Passwörtern erstellen kann. (Ohne "import random")


#Importe
import time
ListOfCharacters = []

CharSet = r"!#$%&()*+-/0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]_abcdefghijklmnopqrstuvwxyz{}~"
for i in CharSet:
    ListOfCharacters.append(i)


# with open("PasswordLiberie.txt", "r") as file:
#     characters = file.read()
#     for i in characters:
#         ListOfCharacters.append(i)

def randomNum(maxnumber):
    global seed
    timeNow = time.time()
    number = int((timeNow - int(timeNow)) * 1000000)
    return number%maxnumber

def generate_password(length):
    
    #init Vars
    Password = ""
    Uppercase = False
    Lowercase = False
    Number = False
    SpecialCharacter = False
    
    #Kontrolle für länge
    # EIn bisschen Simpel aber OK
    if length < 4:
        Uppercase = True
        Lowercase = True
        Number = True
        SpecialCharacter = True

    for i in range(length):
        Listlength = len(ListOfCharacters)
        Password += str(ListOfCharacters[randomNum(Listlength)]) #My bad
        if Password[i].isupper():
            Uppercase = True
            print(f"Uppercase: {Uppercase}{Password[i]}")
        elif Password[i].islower():
            Lowercase = True
            print(f"Lowercase: {Lowercase}{Password[i]}")
        elif Password[i].isdigit():
            Number = True
            print(f"Number: {Number}{Password[i]}")
        else:
            SpecialCharacter = True
            print(f"SpecialCharacter: {SpecialCharacter}{Password[i]}")
    if not Uppercase or not Lowercase or not Number or not SpecialCharacter:
        print("again")
        return generate_password(length)#Hier würde er die Recursion erzeugen. 
    return Password


#test durchlauf
print(generate_password(12))
