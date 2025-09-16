#In diesem mini-Projekt möchte ich einen password generator erstellen.
import random as rm

ListOfCharacters = []

with open("PasswordLiberie.txt", "r") as file:
    characters = file.read()
    for i in characters:
        ListOfCharacters.append(i)


def randomNum():
    global ListOfCharacters
    return rm.randint(0, len(ListOfCharacters) - 1)

def generate_password(length):
    Password = ""
    Uppercase = False
    Lowercase = False
    Number = False
    SpecialCharacter = False
    for i in range(length):
        Password += ListOfCharacters[randomNum()]
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



