from colorama import *
import time
import platform
import os


def print_logoscreen(version):
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
                   A Advanced OSINT Tool                  {(     )}
===========================================================""===""=========
                                                            |||||
                 By Jeffrey Montanari                        |||
                 Twiter: @alfredredbird1                      |

             Thanks To Our Sponsor: Smoke-wolf
"""
    )
    ## prints os infomation
    print(
        Fore.RESET
        + "==========================================================================="
    )
    print(
        Fore.RED
        + "     Desclaimer: Not All Sites And Or Proxys Are Garineteed To Work! \n     By Using You Take Full Account Of Your Actions"
    )
    print(Fore.RESET + " ")
    print("     " + platform.system() + "                  Alfred Version:")
    print("     " + platform.release() + "                  " + version)
    print("")
    print(
        Fore.RESET
        + "==========================================================================="
    )
    print(" ")


def connectionError(cError, f):
    if cError >= 5:
        print(
            Fore.RED + """==========================================================="""
        )
        print(
            Fore.RED
            + "Uh Oh Error! Looks Like The Connection Dont Seem To Be Working. Check your connection Or Proxy, Then Try Again :("
        )
        print(
            Fore.RED + """==========================================================="""
        )
    if cError <= 5:
        f.close
        print("""===========================================================""")


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

        -h  | --help |
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
      Clear |--Clear | Clears The Terminal
        -q  | --quit | (Quits)
------------+--------+------------------------------------------
     [FILES]:        |
        -r  | --read | (Reads Last Search Results) 
        -ls |        | Prints The Files In ./alfred
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


def wiki():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """░█▀▀▄░█░░█▀▀░█▀▀▄░█▀▀░█▀▄░░░▒█░░▒█░░▀░░▒█░▄▀░░▀░
▒█▄▄█░█░░█▀░░█▄▄▀░█▀▀░█░█░░░▒█▒█▒█░░█▀░▒█▀▄░░░█▀
▒█░▒█░▀▀░▀░░░▀░▀▀░▀▀▀░▀▀░░░░▒▀▄▀▄▀░▀▀▀░▒█░▒█░▀▀▀
"""
    )
    print(
        """
    [1] Installation
    [2] Options
    [3] Errors
    [4] Dark Alfred
    [5] Modules
    """
    )
    search = input("What Are You Looking For?  ⤷  ")
    if search == "1":
        print(
            "You Can Find Info On It Here: https://github.com/Alfredredbird/alfred/wiki/Instalations"
        )
        returntoAlfred(3)
        return True
    elif search == "2":
        print(
            "You Can Find Info On It Here: https://github.com/Alfredredbird/alfred/wiki/Usage---Options"
        )
        returntoAlfred(3)
        return True
    elif search == "3":
        print(
            "You Can Find Info On It Here: https://github.com/Alfredredbird/alfred/wiki/Errors"
        )
        returntoAlfred(3)
        return True
    elif search == "4":
        print(
            "You Can Find Info On It Here: https://github.com/Alfredredbird/alfred/wiki/Dark-Alfred"
        )
        returntoAlfred(3)
        return True
    elif search == "5":
        print(
            "You Can Find Info On It Here: https://github.com/Alfredredbird/alfred/wiki/Modules"
        )
        returntoAlfred(3)
        return True
    else:
        print(
            "Not Sure.... But You Can Check Here: https://github.com/Alfredredbird/alfred/wiki/"
        )
        returntoAlfred(3)
        return True


def returntoAlfred(seconds):
    print("Returning To Alfred Soon...")
    time.sleep(seconds)


def unameinfo(uname):
    print("Requested Username: " + uname)
