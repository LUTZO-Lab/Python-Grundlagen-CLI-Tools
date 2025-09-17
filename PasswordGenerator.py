#In diesem mini-Projekt möchte ich einen password generator erstellen.
import time

ListOfCharacters = []

with open("PasswordLiberie.txt", "r") as file:
    characters = file.read()
    for i in characters:
        ListOfCharacters.append(i)

def randomNum(maxnumber):
    global seed
    timeNow = time.time()
    number = int((timeNow - int(timeNow)) * 1000000)
    return number%maxnumber

def generate_password(length):
    Password = ""
    Uppercase = False
    Lowercase = False
    Number = False
    SpecialCharacter = False
    for i in range(length):
        Listlength = len(ListOfCharacters)
        print(Listlength)
        print(randomNum(Listlength))
        Password += str(randomNum(Listlength))
        if Password[i].isupper():
            Uppercase = True
        elif Password[i].islower():
            Lowercase = True
        elif Password[i].isdigit():
            Number = True
        else:
            SpecialCharacter = True
    if not Uppercase or not Lowercase or not Number or not SpecialCharacter:
        return generate_password(length)
    return Password
print(generate_password(12))

