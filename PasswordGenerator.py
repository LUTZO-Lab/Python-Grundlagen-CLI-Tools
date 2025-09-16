#In diesem mini-Projekt möchte ich einen password generator erstellen.
# ! Wichtig: Ich möchte veruchen als Seed eine richtige zufallige Zahl zu verwenden.
# import random wird nicht verwendet, da es kein echter Zufall ist.

# Als Quelle für den Seed, werde ich die aktuelle Zeit in Nanosekunden verwenden.
# + den hash eines generierten Objektes.

# Wahrscheinlich werde ich auch MS BCryptGenRandom verwenden.

def get_seed():
    import subprocess
    result = subprocess.run("(Get-Process -Id $PID).CPU", capture_output=True, text=True, shell=True)
    print(result.stderr)


get_seed()
