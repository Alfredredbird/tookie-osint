import os
import platform
import time
from configparser import ConfigParser

from colorama import *

from modules.lang import *
from modules.modules import *
from modules.webscrape import *

config = ConfigParser()
#this grabbes the langugae loader
language_module = language_m

def logo(uname, version, config):
    config.read("./config/config.ini")
    browser = config.get("main", "browser")
    prerelease = config.get("main", "prerelease")
    os.system("cls" if os.name == "nt" else "clear")
    print(
        Fore.RED
        + """   
                                    
                         ╓φ▒Γ ,╖╗⌐
                        Φ╬╬Γ @╬╬Γ ╔▓
                       ^╣╬▓µ╣╬▓  ▄▓▓▓
                     ╔▓  ╙╬╬╬╩  ╜▀▀▀╙╙
                    ▄▓▓▓▄  ╣╬▓µ╓╓╖╗╗φφ@φ
                  "╙╙╙╙╙"  ╟╬╬╣╝╣╬╬▀╨╣╬▓                 
                  ¥φφφφφφφφ╬╬╩   ╫╬▓, ╟╬⌐                 
                   └╙╨╨╨╨╫╬╬╩ ╔▓  ╚╬╬L `                 
                    %φφφφ╬╬╩ ╔▓▓▓╕ ╙╬Γ                    __,---. 
                     `╙╨╨╨╜  ▀▀▀▀▀¬                      /__|o\  ) 
                 ░█▀▀▄░█░░█▀▀░█▀▀▄░█▀▀░█▀▄                `-\ / /
                 ▒█▄▄█░█░░█▀░░█▄▄▀░█▀▀░█░█                  ,) (,
                 ▒█░▒█░▀▀░▀░░░▀░▀▀░▀▀▀░▀▀░                 //   \\
                   A Advanced OSINT Tool                  {(     )}"""
        + Fore.RESET
        + """
==========================================================="""
        + Fore.RED
        + '''""'''
        + Fore.RESET
        + """==="""
        + Fore.RED
        + '''""'''
        + Fore.RESET
        + """========="""
        + Fore.RESET
        + Fore.RED
        + """
                                                            ||||| """
        + Fore.RESET
        + """
                 By Jeffrey Montanari        """
        + Fore.RED
        + """                |||"""
        + Fore.RESET
        + """
                 Twiter: @alfredredbird1        """
        + Fore.RED
        + """              | """
        + Fore.RESET
        + f"""

               {language_module.title1}
"""
    )
    ## prints os infomation
    print(
        Fore.RESET
        + "==========================================================================="
    )
    print("")
    print(Fore.RED + language_module.disclamer)
    print(Fore.RESET + " ")
    print(
        "     "
        + "OS:"
        + f"                                      Alfred {language_module.version}:"
    )
    print(
        "     "
        + platform.system()
        + " "
        + platform.release()
        + "                               "
        + version
    )
    print("")
    print("     " + "Host:" + "                                    Prerelease:")
    print(
        "     " + str(platform.node()) + "                              " + prerelease
    )
    print("")
    print("")
    print(
        "     "
        + "Browser:"
        + f"                                 Python {language_module.version}:"
    )
    print(
        "     "
        + browser
        + "                                            "
        + platform.python_version()
        + "                               "
        + "                                "
    )
    print("")
    if uname != "":
     print(f"                {language_module.targetusernames} " + uname + Fore.RESET)
    print(
        Fore.RESET
        + "==========================================================================="
    )
    print(" ")


def print_help():
    print(
        """
██╗   ██╗███████╗ █████╗  ██████╗ ███████╗
██║   ██║██╔════╝██╔══██╗██╔════╝ ██╔════╝
██║   ██║███████╗███████║██║  ███╗█████╗  
██║   ██║╚════██║██╔══██║██║   ██║██╔══╝  
╚██████╔╝███████║██║  ██║╚██████╔╝███████╗                      
 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      \      \    
                                                (o>    (o>
Usage: [USERNAME]                               //\    //\ 
       [OPTIONS]                                V_/    V_/ 
================================================================
                                                ||     ||
                                                ||     ||
   [COMMAND]  [ALIAS]  [INFO]
------------+--------+------------------------------------------
        -h  | --help | (Shows This Menu)
------------+--------+------------------------------------------
   [GENERAL]:        |
        -s  |        | (Starts The Program)
        -N  | --nsfw | (Points NSFW Sites)    
        -ec |        | (Prints The Returned Status Code)
        -a  |        | (Shows Everything) 
            |        | Error ID's:
            |        |   
            |        |   E ⥴ Connection Error, Etc
            |        |
        -p  | --ping | (pings website)
    --Clear |  Clear | Clears The Terminal
        -q  | --quit | (Quits)
------------+--------+------------------------------------------
     [FILES]:        |
        -r  | --read | (Reads Last Search Results) 
        -ls |   ls   | Prints The Files In ./alfred
       -Cat |        | Reads The Inputed File
   --Config |        | Edits The Config. 
     --Wiki |        | Prints Wiki Pages 
        -gsl|        | (Generates Random Sites And Tests Them)
            |        |  Ussage:
            |        |     [LENGTH]
            |        |        [AMOUNT]
            |        |           [TYPE] 
            |        |              [OPTIONS]
------------+--------+------------------------------------------
     [SCANS]:        |
        -f  |        | Runs A Fast Scan   
        -m  |        | Runs A Scan From The Big Site List
        -O  |        | Checks Accounts From A List
        -d  |        | (Allows Redirects "Might Not Be Accutate")
        -w  |        | (Allows Alfred To Webscrape)
------------+--------+------------------------------------------
   [PROXIES]:        |                                          
        -c  |        | (Connects To A Proxy Server)             
            |        |      Format [Type] [Ip] [Port]           
            |        |                                          
        -lp |        | (Gives A List Of Posible Working Proxys) 
            |        | Types:                                  
            |        |                                          
            |        |       http   ⥴ /http.txt                 
            |        |       socks4 ⥴ /socks4.txt               
            |        |       socks5 ⥴ /socks5.txt               
            |        |                                          
------------+--------+------------------------------------------
     [OTHER]:        |
        -FS |        | Runs A Simple Network File Share    
        -S  |        | Downloads A Webpage's HTML File
        -u  |        | Prints The Requested Username
------------+--------+------------------------------------------        
       
"""
    )


def wiki(language_module):
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """░█▀▀▄░█░░█▀▀░█▀▀▄░█▀▀░█▀▄░░░▒█░░▒█░░▀░░▒█░▄▀░░▀░
▒█▄▄█░█░░█▀░░█▄▄▀░█▀▀░█░█░░░▒█▒█▒█░░█▀░▒█▀▄░░░█▀
▒█░▒█░▀▀░▀░░░▀░▀▀░▀▀▀░▀▀░░░░▒▀▄▀▄▀░▀▀▀░▒█░▒█░▀▀▀
"""
    )

    # Read options from the INI file
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    for i, (option, link) in enumerate(config.items("Links"), start=1):
        custom_label = {
            "link1": "Instalations",
            "link2": "Ussage/Options",
            "link3": "Errors",
            "link4": "Dark-Alfred",
            "link5": "Modules",
        }.get(option.lower(), "Unknown")

        print(f"{i}. {custom_label}")

    search = input("What Are You Looking For?  ⤷  ")

    try:
        option_index = int(search) - 1
        selected_option = list(config.items("Links"))[option_index]
        print(f"{language_module.wikilist}{selected_option[1]}")
    except (ValueError, IndexError):
        print(f"{language_module.idk3} https://github.com/Alfredredbird/alfred/wiki/")

    returntoAlfred(5, language_module)
    return True


def returntoAlfred(seconds, language_module):
    print(language_module.status4)
    time.sleep(seconds)


def unameinfo(uname, language_module):
    print(language_module.rqUname + uname)
