import os
from time import sleep
import subprocess as sp
import colorama
from colorama import Fore, Back, Style
a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
colorama.init(autoreset=True)
hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
res = Style.RESET_ALL
abu2 = Style.DIM+Fore.WHITE
putih = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
ungu2 = Style.NORMAL+Fore.MAGENTA
ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
hijau2 = Style.NORMAL+Fore.GREEN
yellow2 = Style.NORMAL+Fore.YELLOW
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
red2 = Style.NORMAL+Fore.RED
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
cyan = Style.RESET_ALL+Style.BRIGHT+Fore.CYAN
cyan2 = Style.NORMAL+Fore.CYAN
kur1 = Style.BRIGHT+Fore.RED+"["
kur2 = Style.BRIGHT+Fore.RED+"]"
pink = Back.RED + Fore.WHITE
blue = Back.BLUE + Fore.WHITE
os.system('clear')
#sp.call(['pip install colorama'], shell=True)

print(BOLD+pink+'\n\n\t\t Shorcut for help you - TERKEY (Termux Key) ')
#print('\t https://t.me/CRABS_ID')
print(blue+'\t\t'+'='*44)
print('\nProses..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
   os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

#key = "extra-keys = [['ESC','/','-','HOME','UP','END'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT']]"
key = "extra-keys = [['HOME','ESC','TAB','CTRL','ALT','-','LEFT','RIGHT','DOWN','UP']]"
tx = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
tx.write(key)
tx.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\nThanks using this tools\n\n')


# ini cuma shortcut buat bantu para nub
# karjok pangesty
