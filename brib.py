#!/usr/bin/env python
from __future__ import print_function
from time import sleep
from rich.console import Console
from alive_progress import *
from timeit import default_timer
from colorama import Fore, Back, Style
from pathlib import Path
from socket import socket
from modules.modules import *
import urllib.request, urllib.error, urllib.parse
import ssl
import sys
import os
import urllib.request
import platform
import logging
import json
import requests
import time
import site
import random
import string

# variables
modes = ""
inputnum = ""
ars = ""
alist = True
fastMode = 0
cError = 0
siteProgcounter = 0
console = Console()
testall = False
slectpath = ""
test = False
ec = 0
version = ""

with open("version.txt", "r") as fp:
    version = fp.read()
    fp.close()


def get_random_string(length):
    # choose from all lowercase letter

    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


# site lists
siteList = []
siteNSFW = []

# clears the terminal when Alfred is ran
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
cfu = input("Check For Updates? [y/n]: ⤷ ")
if "Y" in cfu or "y" in cfu:
    exec(open("alfred/update.py").read())
elif "N" in cfu or "n" in cfu:
    print("Ok! Ill Ask Later....")


uname = input("⤷ ")

#
# This is where we gather the inputed options and then run them.
# Not all of the options exicute on inout.
#
#
while test != True:
    input1 = input("⤷ ")
    if input1 != "":
        if "-t" in input1:
            timeoutC(modes, input1)
        if "-c" in input1:
            proxyCheck(modes, input1)
        if "-q" in input1 or "--quit" in input1:
            qexit()

        if "-gsl" in input1:
            siteListGen(console, testall, get_random_string)

        if "-d" in input1:
          d_option()
        if "-S" in input1:
            Cap_S_option(modes, input1)

        if "-s" in input1:
            input2 = input("[Y/N]? ⤷ ")
            if input2 == "":
                lol = 1
            if input2 != "":
                if input2 == "Y" or input2 == "y":
                    modes += input1
                    inputnum += input2
                if input2 == "N" or input2 == "n":
                    modes = ""
                    inputnum = ""
                    uname = input("⤷ ")
                    test = False
                    input2 = ""
                    input1 = ""

        if "-ec" in input1:
            ec = 1
        if "-lp" in input1:
            l_p()
        if "-O" in input1 or "-o" in input1:
            slectpath = Path.home() / str(input("PATH: ⤷ "))
            file_path = os.path.join(slectpath)
            # check if the directory exists
            fastMode = 2

            if os.path.exists(file_path):
                # reads the file

                try:
                    file = open(file_path, "r+")
                    file1 = open(file_path, "r")
                    Lines = file1.readlines()

                    count = 0
                    L = [Lines]

                    for line in Lines:
                        count += 1
                        print("Lines {}: {}".format(count, line.strip()))

                    file.close()

                except PermissionError():
                    print("Permission Error")
                except TypeError():
                    print("Type Error")
            else:
                print(Fore.RED + "Cant Find The Save File!")
                print(Fore.RESET)
                exit(69)

        if "-r" in input1 or "--read" in input1:
            R_option(slectpath)
        # code to read and check files

        if "-p" in input1 or "--ping" in input1:
            p_option()

        if "-a" in input1:
            modes += input1

        if "-f" in input1:
            fastMode = 1

        if "-N" in input1:
            modes += input1

        if "-h" in uname or "--help" in uname or "-h" in input1 or "--help" in input1:
            print_help()

    if "" in input1 and inputnum != "":
        test = True
    inputnum = ""
dir_path = Path.home() / "Downloads"

file_name = "usernames.alfred"
file_path = os.path.join(dir_path, file_name)
# check if the directory exists
if os.path.exists(dir_path):
    # create the file
    print(" ")
    print("Creating / Overwriting Save File.")

else:
    print("Directory doesn't exist.")


if fastMode == 0:
    try:
        with open("sites.json", "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")

        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)

if fastMode == 1:
    try:
        with open("fsites.json", "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")

        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)
if fastMode == 2:
    try:
        with open(slectpath, "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")

        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)

connection_error = 0


print(Fore.GREEN + "searching for sites with: " + uname + Fore.RESET)
print("")
siteCount = 0
with open(file_path, "w") as f:
    for site in siteList:
        siteCount += 1
        with console.status("Working....") as status:
            siteN = site["site"]
            siteNSFW = site["nsfw"]

            try:
                headers = headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                }
                if "-t" in modes:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=timeout,
                        allow_redirects=False,
                        proxies=False,
                        json=False,
                    )  # 35
                if "-d" in modes:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=1.5,
                        allow_redirects=ars,
                        proxies=False,
                        json=False,
                    )
                if "-c" in modes:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=1.5,
                        allow_redirects=False,
                        proxies=proxies,
                        json=False,
                    )

                else:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=1.5,
                        allow_redirects=False,
                        proxies=False,
                        json=False,
                    )

                if ec == 1:
                    print(response.status_code)
                if response.status_code == 200:
                    siteProgcounter += 1
            except requests.exceptions.SSLError:
                connection_error = 1
                #  print(requests.exceptions.HTTPError)
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "S" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "S" + "] " + siteN + uname + "\n")
            except requests.exceptions.HTTPError:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "H" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "H" + "] " + siteN + uname + "\n")
            except requests.exceptions.ConnectTimeout:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "T" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "T" + "] " + siteN + uname + "\n")
            except requests.exceptions.ReadTimeout:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "T" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "T" + "] " + siteN + uname + "\n")
            except requests.exceptions.RetryError:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "R" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "R" + "] " + siteN + uname + "\n")
            except requests.exceptions.ProxyError:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "p" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "P" + "] " + siteN + uname + "\n")
            except requests.exceptions.ConnectionError:
                cError += 1
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "C" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "C" + "] " + siteN + uname + "\n")
            except requests.exceptions.InvalidURL:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "I" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "I" + "] " + siteN + uname + "\n")
            except requests.exceptions.InvalidHeader:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "N" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "N" + "] " + siteN + uname + "\n")
            except requests.exceptions.ChunkedEncodingError:
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "CE" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "CE" + "] " + siteN + uname + "\n")
            except KeyboardInterrupt:
                print(
                    """
===========================================================

"""
                )
                print("Stopping........")
                print("Found: " + str(siteProgcounter) + " Posible Accounts")
                f.close
                print("Saved Results To File")
                exit(99)
            else:
                if "-a" in modes:
                    if response.status_code >= 300 or response.status_code >= 510:
                        print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                        f.write("[" + "-" + "] " + siteN + uname + "\n")
                    if response.status_code == 406:
                        print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                        f.write("[" + "-" + "] " + siteN + uname + "\n")

                if "-N" in modes:
                    if response.status_code == 200 and siteNSFW == "true":
                        print(
                            "["
                            + Fore.LIGHTMAGENTA_EX
                            + "NSFW"
                            + Fore.RESET
                            + "] "
                            + siteN
                            + uname
                            + "     "
                            + Fore.RESET
                        )
                        f.write(
                            "["
                            + "+"
                            + "] "
                            + siteN
                            + uname
                            + "             NSFW"
                            + "\n"
                        )

                    if response.status_code == 200 and siteNSFW == "false":
                        print(
                            "[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname
                        )
                        f.write("[" + "+" + "] " + siteN + uname + "\n")
                if response.status_code == 200 and "-N" not in modes:
                    print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "+" + "] " + siteN + uname + "\n")
                if response.status_code == 406 and "-N" not in modes:
                    print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "+" + "] " + siteN + uname + "\n")

if cError >= 5:
    print(
        Fore.RED
        + """
===========================================================

"""
    )
    print(
        Fore.RED
        + "Uh Oh Error! Looks Like The Connection Dont Seem To Be Working. Check your connection Or Proxy, Then Try Again :("
    )
    print(
        Fore.RED
        + """

===========================================================
"""
    )
if cError <= 5:
    f.close
    print(
        """
===========================================================

"""
    )


def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100


print(
    "Found: "
    + str(siteProgcounter)
    + "/"
    + str(siteCount)
    + " Posible Accounts With "
    + str(is_what_percent_of(siteProgcounter, siteCount).__round__())
    + "% Acuracy"
)
print("Saved Results To File")


startagain = input("Run Again?: [Y/N] ⤷ ")
if "Y" in startagain or "y" in startagain:
    exec(open("brib.py").read())
elif "N" in startagain or "n" in startagain:
    exit()
