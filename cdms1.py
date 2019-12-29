from telethon import TelegramClient, sync, events, functions, types, errors
from telethon.tl.types import UpdateNewMessage,UpdateShortMessage, ReplyInlineMarkup, KeyboardButtonUrl
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest, ImportChatInviteRequest, AddChatUserRequest
from telethon.errors import FloodTestPhoneWaitError, FloodWaitError, SessionPasswordNeededError, PhoneNumberBannedError, YouBlockedUserError, UnauthorizedError, AuthKeyUnregisteredError, UserDeactivatedError, SessionRevokedError, PhoneCodeInvalidError
#from telethon.network.mtprotosender
from time import sleep, time
from colorama import Fore,Style, init as cr
cr(autoreset=True)
import json, re, sys, os, random
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
abu2 = Style.DIM+Fore.WHITE
putih = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
ungu2 = Style.NORMAL+Fore.MAGENTA
hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
hijau2 = Style.NORMAL+Fore.GREEN
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
yellow2 = Style.NORMAL+Fore.YELLOW
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
red2 = Style.NORMAL+Fore.RED
cyan = Style.RESET_ALL+Style.BRIGHT+Fore.CYAN
cyan2 = Style.NORMAL+Fore.CYAN
reset = Fore.RESET
res = Style.RESET_ALL
os.system("cls" if os.name == "nt" else "clear")

# MANUAL CHOICE
choice1 = '⏱ Get 0.2 DOGE'
choice2 = '⏰ Get 2 DOGE'
cph ='I AM NOT A ROBOT'
	
# RANDOM CHOICE
x = ['⏱ Get 0.2 DOGE','⏰ Get 2 DOGE','⏱ Get 0.2 DOGE']

banner = """
"""+Style.BRIGHT+Fore.CYAN+"""

██╗  ██╗ ██████╗ ██████╗ ██████╗ ███████╗
╚██╗██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
 ╚███╔╝ ██║     ██║   ██║██║  ██║█████╗  
 ██╔██╗ ██║     ██║   ██║██║  ██║██╔══╝  
██╔╝ ██╗╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
"""+Style.RESET_ALL+Style.BRIGHT+Fore.WHITE+"""               Mr. Alliance - XCODE Team
"""+Fore.BLUE + """========================================
"""+Style.BRIGHT+Fore.WHITE+"""DONATION : 
"""+Style.BRIGHT+Fore.WHITE+"""BTC  : """+Style.BRIGHT+Fore.GREEN+"""3NVVGiiBdvyd7Qc6iiC4ZN5nD8ypGGQ543
"""+Style.BRIGHT+Fore.WHITE+"""ETH  : """+Style.BRIGHT+Fore.GREEN+"""0xD4B2af2bF12625508ECA99877A02B9e060cd84c2
"""+Style.BRIGHT+Fore.WHITE+"""DOGE : """+Style.BRIGHT+Fore.GREEN+"""DJi7FV2wELjATkd8UcYRftnwAovmwa1NHS"""

print(banner)
print(Fore.BLUE + "========================================" + Fore.RESET)
print(BOLD+Fore.BLUE + "Thanks support to Team 8 :" + Fore.RESET)
print(Fore.WHITE + "@AkkerToby, @ikhiee, @Ikimono_Gakari, all member" + Fore.RESET)
print(Fore.BLUE + "======================================== \n" + Fore.RESET)
if not os.path.exists("session"):
    os.makedirs("session")
if len(sys.argv) < 2:
    print( Fore.RED + "\n\nUsage : python main.py +62" + Fore.RESET)
    sys.exit(1)
api_id = 1148490
api_hash = "d82c81323285aeb9c2ba9ee420d8b009"
phone_number = sys.argv[1]
client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input("Enter Yout Code : "))
    except errors.FloodWaitError:
       print (f'\n{abu2}[{red}✘{abu2}]{red} Waiting time!')
       sleep(2)
    except errors.BadMessageError:
       print (f'\n{abu2}[{red}✘{abu2}]{red} Bad Message!')
    except SessionPasswordNeededError:
        passw = input("Your 2fa Password : ")
        me = client.start(phone_number, passw)
        
account = client.get_me()
print("[$] Name    > "+BOLD+"CDM DOGE")    
print("[$] Account > "+BOLD+account.first_name+BOLD+account.last_name)
print("[$] Phone   > "+BOLD+account.phone)
channel_username = "@cdm_doge_bot"
channel_entity = client.get_entity("@cdm_doge_bot")

print(f'\n[{hijau}*{reset}]'+BOLD+'START BOT CDM DOGE')
while True:
    try:
       #for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write("                                                              ")
        sys.stdout.write("\r")
        sys.stdout.write(f"\r{abu2}[{red}?{abu2}]{yellow} Still waiting claim" + "\n")
        sys.stdout.flush()
        #posts = client(GetHistoryRequest(peer=channel_entity, limit=5, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        #os = posts.messages[0].message
        # * All actions are frozen for 60 seconds
        select = random.choice(x)
        os = client.send_message(entity=channel_entity, message=select)
        posts = client(GetHistoryRequest(peer=channel_entity, limit=5, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        opg = posts.messages[1].message
        opc = re.search(r" Congratulation! You've got (.*)", opg)
        opb = re.search(r" Your balance is now: (.*)", opg)
        opw = re.search(r" Please wait (.*)", opg)
        bypass = re.search(r" You can continue", opg)
        sec = re.findall( r'([\d.]*\d+)', opg)
        if opc:
            sys.stdout.write(f"{abu2}[{hijau}√{abu2}]{res}" + opc.group() + "\n")
        if opb:
            sys.stdout.write(f"{abu2}[{hijau}√{abu2}]{hijau}" + opb.group() + "\n")
        if opw:
            sys.stdout.write(f"{abu2}[{red}×{abu2}]{red}" + opw.group() + "\n")  
        if bypass:
        	sys.stdout.write(f"{abu2}[{hijau}√{abu2}]{hijau}" + bypass.group() + "\n")
        sys.stdout.write("                                                              ")
        sys.stdout.write("\r")
        sys.stdout.write(abu2+"["+red+"!"+abu2+"]"+yellow+" Sleep "+res+"00:30")
        sleep(1)
       #def waktu(i):
        for m in range(0, -1, -1):   
            for d1 in range(2, -1, -1):  
                for d2 in range(9, -1, -1):
                 sys.stdout.write("\r")      
                 #sys.stdout.write(abu2+"["+red+"!"+abu2+"]"+yellow+" Sleep "+res+"0{}:{}{}".format(waktu(int(sec[0]))))
                 sys.stdout.write(abu2+"["+red+"!"+abu2+"]"+yellow+" Sleep "+res+"0{}:{}{}".format(m,d1,d2))
                 sys.stdout.flush()
                 sleep(1)
                 sys.stdout.write("\r                                          \r")
        posts = client(GetHistoryRequest(peer=channel_entity, limit=5, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        op = posts.messages[0].message
        opm = posts.messages[0].message
        sleep(1)
        if "Solve the captcha:" in op:
           print(f"{abu2}[{hijau}√{abu2}]{hijau} Please wait, still bypass captcha")
           #sleep(2)
           met = op.split(":")[1]
           mett = met.split("=")[0]
           op = re.findall(r"[\W]", mett)
           mettt = mett.split(op[1])
           op = re.findall(r"[\W]", mett)
        if "-" in op[1]:
       	 hasil = int(mettt[0]) - int(mettt[1])
         print(f"{abu2}[{red}!{abu2}]{red} bypass results : {hijau}",hasil)
        elif "+" in op[1]:
           hasil = int(mettt[0]) + int(mettt[1])	
           print(f"{abu2}[{red}!{abu2}]{red} bypass results : {hijau}",hasil)
           client.send_message(entity=channel_entity, message=str(hasil))
           print(f"{abu2}[{hijau}√{abu2}]{hijau} Success bypass math captcha!")
           sleep(2)
        else:
            posts = client(GetHistoryRequest(peer=channel_entity, limit=5, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            print(f"\n{abu2}[{hijau}!{abu2}]{cyan} Update info from bot\n")
            cpo = re.search(r" Are you robot?", opm)
            #bypass = re.search(r" You can continue", opg)
            #sleep(1)
        if cpo:
            sys.stdout.write(f"{abu2}[{hijau}×{abu2}]{red}" + cpo.group() + "\n")
            cpo = client.send_message(entity=channel_entity, message=cph)
            print(f"\n{abu2}[{hijau}√{abu2}]{hijau} Success bypass robot!\n")
            #print(f"\n{abu2}[{hijau}√{abu2}]{hijau} Success bypass robot! "+bypass.group()+"\n")
          
    except KeyboardInterrupt as e:
        print(f"{red}⛔ Exit...")
        sys.exit()

me = client.get_me()
print (f"{abu2}[{red}✘{abu2}]{red} Client Disconnected {abu2}[{hijau}√{abu2}]{hijau} User : {res}{me.first_name} {abu2}[{hijau}√{abu2}]{hijau} Phone : {res}{account.phone} ")
client.disconnect()