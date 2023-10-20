import platform 
from colorama import *

ver = "v2.2(a) Rev 1"


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
                   A Advanced OSINT Tool                  {(     )}"""+
Fore.RESET +"""
==========================================================="""+Fore.RED
+ '''""'''+ Fore.RESET+ """==="""+ Fore.RED+'''""'''+Fore.RESET+"""========="""+Fore.RESET+Fore.RED+
"""
                                                            ||||| """
+Fore.RESET+"""
                 By Jeffrey Montanari        """+
                 Fore.RED+"""                |||"""
                 +Fore.RESET+ """
                 Twiter: @alfredredbird1        """+Fore.RED+"""              | """+ 
                 Fore.RESET+ """

               Many Thanks To Our Sponsors!
"""
    )
    ## prints os infomation
    print(Fore.RESET+ "===========================================================================")
    print(Fore.RED+ "     Desclaimer: Not All Sites And Or Proxys Are Garineteed To Work! \n     By Using You Take Full Account Of Your Actions")
    print(Fore.RESET + " ")
    print("     " + "OS:" + "                                      Alfred Version:")
    print("     " + platform.system()+" "+platform.release() + "                               " + version)
    print("     ")
    print("     " + "Python Version:" + "                          Host:")
    print("     " + platform.python_version() + "                                   " + str(platform.node()) )
    print("")
    print(Fore.RESET+ "===========================================================================")
    print(" ")

print_logoscreen(ver)    
