#Importálások
from functions import *
import sys
#Admin jogok tesztelése
is_admin()

#Üdvözlés, információk kiírása.
print("WEBSITE DOWNLOADER")
print("Author: Siera221")
print("Comomands: help")
#Ha admin akkor a program tovább folytatódik.
if is_admin():
    i = 1
    #Parancsok megnyitása.
    while(i <= 5):
        if(input() ==  "help"):
            help()
        if(input() == "webclone"):
            if __name__ == '__main__':
                print('\n--- Website Adatok ---\n')
                initializer()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)