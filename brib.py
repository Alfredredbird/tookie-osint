#!/usr/bin/env python3
from __future__ import print_function
import os
import site
import time
from configparser import ConfigParser
from pathlib import Path
from socket import socket
from time import sleep
from timeit import default_timer
from alive_progress import *
from colorama import Back, Fore, Style
from rich.console import Console
from modules.configcheck import *
from modules.modules import *
from modules.printmodules import *
from modules.scanmodules import *
from modules.siteListGen import *
from modules.webscrape import *
from lang.en import *
from modules.crypt import *
import datetime


# cool arrow because I keep forgetting what UNICODE arrow I used. ⤷
# variables
domain_extensions = False
alist = True
test = False
testall = False
webscrape = False
fastMode = 0
cError = 0
count = 0
# holder is just something Alfred can return when Alfred needs to return nothing.
holder = 0
siteProgcounter = 0
ec = 0
console = Console()
config = ConfigParser()
slectpath = ""
version = ""
modes = ""
inputnum = ""
ars = ""
date = datetime.date.today()
# These stores the loaded site info
siteList = []
siteErrors = []
siteNSFW = []
#loads the language
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
language_code = getLang(config)
language_module = load_language(language_code)
# checks that the folders exist. if not it creates them
folders_to_create = [
    "config",
    "captured",
    "downloadedSites",
    "modules",
    "proxys",
    "sites",
    "lang",
]
create_folders(folders_to_create)
# gets the defualt browser and system information
browser = get_default_browser()
print(language_module.browser + browser )
# gets the version of Alfred
version = configC()
# gets the info to encrypt
syskey = (
    platform.system()
    + platform.release()
    + "-AlfredVer-"
    + configC()
    + "-"
    + platform.python_version()
    + "-"
    + browser
)
# encrypts the key
encrypted_text = encrypt(syskey)
print(language_module.encrypt1)
# logs the key
saveInfo(config, encrypted_text)
# this prints the start up screen and passes the verion varaible in
print_logoscreen(version, config)
# does config stuff
configUpdateStuff(config, browser)
# this is the variable that gets the username
uname = input(f"{language_module.target}")
# this removes the comma and puts the usernames into a list
uname_list = [item.strip() for item in uname.split(",")]

# This is where Alfred gathers the inputed options and then run them.
# Not all of the options execute on input.
while test != True:
    input1 = input("⤷ ")
    if input1 != "":
        # the options follow a simple ruleset
        # first you need the input ex: "-ls" then you need the function it will run ex: dirList
        # lastly, you need the inputs or anything you want to pass into the function ex: [modes, input1]
        action = {
            "-ls": [dirList, []],
            "ls": [dirList, []],
            "-t": [timeoutC, [modes, input1]],
            "-FS": [fileShare, []],
            "-q": [qexit, []],
            "-gsl": [
                siteListGen,
                [console, testall, get_random_string, domain_extensions, uname],
            ],
            "-c": [proxyCheck, [modes, input1]],
            "-lp": [list_proxys, []],
            "-h": [print_help, []],
            "--help": [print_help, []],
            "-d": [redirects1, [modes, input1]],
            "-u": [unameinfo, [uname]],
            "-Cat": [catFile, []],
            "--Config": [configEditor, [config]],
            "-p": [ping, []],
            "--ping": [ping, []],
            "-r": [read_save, [slectpath]],
            "--read": [read_save, [slectpath]],
            "--Clear": [logo, [uname, version, config]],
            "clear": [logo, [uname, version, config]],
        }
        valid = [key for key in action.keys()]
        for option in valid:
            if option in input1:
                args = action[option][1]
                action[option][0](*args)
        if "-w" in input1:
            webscrape = True
        if "-S" in input1:
            print(
                "Sites Many Not Allow Downloading Their Site Files. Use At Your Own Risk."
            )
            dirDump(globalPath(config))
            time.sleep(2)
            siteDownloader()
            time.sleep(4)
            print("Downloading CSS")
            scriptDownloader(globalPath(config) + "css_files.txt", ".css", count)
            time.sleep(2)
            print("Downloading JS")
            scriptDownloader(globalPath(config) + "javascript_files.txt", ".js", count)
            dv = input("Want To Download Images/Videos? ⤷ ")
            if "Y" in dv or "y" in dv:
                print("Downlading Videos/Images")
                siteD = input("Enter Site Again: ⤷ ")
                imgandVidDownlaod(siteD)
            elif "N" in dv or "n" in dv:
                print("Ok!")
            else:
                print("Not Sure What You Ment. Ill Ask Later")
        if "-s" in input1:
            input2 = input("[Y/N]? ⤷ ")

            if input2 != "":
                if input2 == "Y" or input2 == "y":
                    modes += input1
                    inputnum += input2
                if input2 == "N" or input2 == "n":
                    holder = 1
        if "-ec" in input1:
            ec = 1
        if "-w" in input1:
            webscrape = True
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
        if "--Wiki" in input1:
            wiki()
            logo(uname, version, config)
        # code to display all error codes
        if "-a" in input1:
            modes += input1
        # code to do a fast scan
        if "-f" in input1:
            fastMode = 1
        # code to run a LOOOOOOOOOONG scan
        if "-m" in input1:
            fastMode = 3
        # code to show NSFW sites
        if "-N" in input1:
            modes += input1
        # code to acses Dark Alfred
        if "-Tor" in input1:
            darkAlfred(console, uname)
            logo(uname, version, config)
    # checks for empty input
    if "" in input1 and inputnum != "":
        test = True
    inputnum = ""
# creates the save file
file_name = uname + ".txt"
file_path = os.path.join("./captured/", file_name)
# check if the directory exists
if os.path.exists("./captured/"):
    # creates the file
    print(" ")
    print("Creating / Overwriting Save File.")
else:
    print("Directory doesn't exist.")
# determins what list of sites to use.
if fastMode == 0:
    # fastmode0 is the default scan mode
    scanFileList(siteList, "./sites/sites.json")
if fastMode == 1:
    # fastmode1 is the fast scan mode
    scanFileList(siteList, "./sites/fsites.json")
if fastMode == 2:
    # fastmode2 is the scan from custom site list
    scanFileList(siteList, slectpath)
if fastMode == 3:
    # fastmode2 is the scan from custom site list
    scanFileList(siteList, "./sites/Megasites.json")
# prints ui stuff
print(Fore.GREEN + "searching for sites with: " + uname + Fore.RESET)
print("===========================================================")
if webscrape == True:
    print(Fore.RED + "Note!" + Fore.RESET + " Using The Webscraper Is Pretty Slow.")
    print("===========================================================")
print("")
siteCount = 0
# opens the save file and writes working sites to it
with open(file_path, "a") as f:
    for site in siteList:
        siteCount += 1
        with console.status("Working....") as status:
            siteN = site["site"]
            siteNSFW = site["nsfw"]
            siteErrors = site["errorMessage"]
            i = 0
            for item in uname_list:
                Startscan(
                    modes,
                    siteN,
                    uname_list[i],
                    cError,
                    ec,
                    f,
                    siteProgcounter,
                    siteNSFW,
                    ars,
                    webscrape,
                    siteErrors,
                    date,
                )
                i += 1


# checks for a connection error and prints
connectionError(cError, f)


# calculates the percentage
def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100


print("")
print("===========================================================")
print("")
print("Saved Results To ./captured/captured.alfred")
# Asks to be ran again
startagain = input("Run Again?: [Y/N] ⤷ ")
if "Y" in startagain or "y" in startagain:
    exec(open("brib.py").read())
elif "N" in startagain or "n" in startagain:
    exit()
