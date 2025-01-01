#!/usr/bin/env python3
from __future__ import print_function
import time
import argparse
import datetime
import os
import re
import site
import time
from configparser import ConfigParser
from pathlib import Path
from socket import socket
import threading
import subprocess

from alive_progress import *
from colorama import Fore
from rich.console import Console
# custom modules
from lang.en import *
from modules.plugin import *
from modules.configcheck import *
from modules.crypt import *
from modules.lang import *
from modules.modules import *
from modules.printmodules import *
from modules.scanmodules import *
from modules.siteListGen import *
from modules.webscrape import *
from modules.report import *
from modules.webhook import *
from datetime import date

# Variables
domain_extensions = False
alist = True
test = False
testall = False
webscrape = False
fastMode = 0
cError = 0
count = 0
# holder is just something tookie-osint can return when tookie-osint needs to return nothing.
holder = 0
siteProgcounter = 0
ec = 0
slectpath = ""
version = ""
modes = ""
inputnum = ""
ars = ""
uname = ""
# cool arrow because I keep forgetting what UNICODE arrow I used. ⤷
# Initialization and configuration setup
console = Console()
config = ConfigParser()
#sets up command line arguments
argument = parse_args()
#updates config file if new plugins are found.
pluginUpdater()
# Grabs The Color Scheme From The Config File
colorScheme = colorSchemeGrabber(config, argument)
# gets the defualt browser and system information
browser = WebScraper.get_default_browser()
saveBrowser(config, browser)
# gets the version of tookie-osint
version = versionToPass
#headers for tookie-osint to use
randomheaders = loadHeaders(config)
# loads the language
language_module = language_m
# Initialize the encryption key and cipher suite
encryption_key = generate_encryption_key()
cipher_suite = create_cipher(encryption_key)
# gets the info to encrypt
sys_info = f"{platform.system()}{platform.release()}-tookie-osintVer-{version}-{platform.python_version()}-{browser}{language_code}"
# encrypts the key
encrypted_sys_info = encrypt_text(cipher_suite, sys_info)
# Loads the webhook from the config
webhook_url = str(config.get('main','discordwebhookurl'))

def run_script():
    exec(open('discordrpc.py').read())
if str(config.get('Plugins',"discordrpc")) == "true":
    #RPC Thread
    thread = threading.Thread(target=run_script)
    thread.start()

# logs the key
save_encryption_info(config, encryption_key, encrypted_sys_info)
date = date.today()
# These stores the loaded site info
siteList, siteErrors, siteNSFW = [], [], []

# checks that the folders exist. if not it creates them
create_folders(
    ["config", "captured", "downloadedSites", "modules", "proxys", "sites", "lang", "tookie-osint","plugins","reports"],
    language_module
)
# Prints the initial UI elements
print(language_module.browser + browser)
print(language_module.encrypt1)
logo(colorScheme, "", version, config)
print()
configUpdateStuff(colorScheme, config, browser, language_module, argument)

# Handle command line arguments
if argument.username:
    # this is the variable that gets the username
    uname_list = [item.strip() for item in argument.username.split(",")]
else:
    uname = input(f"{language_module.target}")
    # this removes the comma and puts the usernames into a list
    uname_list = [item.strip() for item in uname.split(",")]
    
    email = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', uname)
    if email:
        print("Email OSINT isnt supported just yet.")
        # remove exit when ready to send to full production
        email = True
        # email_sites = get_site_names()
        # print(email_sites)
        # WebScraper.email_scrape()
        print("Quitting.....")
        exit()
    else:
        pass
    
# This is where tookie-osint gathers the inputed options and then run them.
# Not all of the options execute on input.
if argument:
    input1 = "0"

if any(vars(argument).values()):
    holder += 1
    if argument.scan and uname_list == "":
            print("You must provide a username")
            exit(99)
    if not argument.scan:
        print("You must use -s to start")
        print("")
        exit(99)
    if argument.fast:
        fastMode = 1
    if argument.webscrape:
        webscrape = True
else:
    while test != True:
        if email != True:
         input1 = input("⤷ ")
         if input1 != "":
            # the options follow a simple ruleset
            # first you need the input ex: "-ls" then you need the function it will run ex: dirList
            # lastly, you need the inputs or anything you want to pass into the function ex: [modes, input1]
            action = {
                "-ls": [dirList, []],
                "ls": [dirList, []],
                "-t": [timeoutC, [modes, input1]],
                "-FS": [fileShare, [language_module]],
                "-q": [qexit, []],
                "-gsl": [
                    siteListGen,
                    [
                        console,
                        testall,
                        get_random_string,
                        domain_extensions,
                        uname,
                        language_module,
                    ],
                ],
                "-c": [proxyCheck, [colorScheme, modes, input1]],
                "-lp": [list_proxys, [colorScheme]],
                "-h": [print_help, []],
                "--help": [print_help, []],
                "-d": [redirects1, [modes, input1]],
                "-u": [unameinfo, [uname, language_module]],
                "-Cat": [catFile, [colorScheme]],
                "--Config": [config_editor, [config, language_module]],
                "-p": [ping, [colorScheme]],
                "--ping": [ping, [colorScheme]],
                "-r": [read_save, [colorScheme, slectpath]],
                "--read": [read_save, [colorScheme, slectpath]],
                "--Clear": [logo, [colorScheme, uname, version, config]],
                "clear": [logo, [colorScheme, uname, version, config]],
                "-w": [emptyModule, []],
                "-s": [emptyModule, []],
                "-S": [emptyModule, []],
                "-ec": [emptyModule, []],
                "-O": [emptyModule, []],
                "-o": [emptyModule, []],
                "--Wiki": [emptyModule, []],
                "-a": [emptyModule, []],
                "-f": [emptyModule, []],
                "-N": [emptyModule, []],
                "-Tor": [darktookie, [colorScheme, console, uname]],
                "--extensions": [print_and_run_plugins, []],
                "-ex": [print_and_run_plugins, []],
                
            }
            valid = [key for key in action.keys()]
            option_matched = False
            for option in valid:
                if option in input1:
                    args = action[option][1]
                    action[option][0](*args)
                    option_matched = True
                    break  # Exit the loop if a matching option is found

            if not option_matched:
                print(f"Invalid option: '{input1}' Try --help for more information")

            if "-S" in input1:
                print(
                    f"{Fore.RED + language_module.note + Fore.RESET}{language_module.warning1}"
                )
                dirDump(globalPath(config))
                time.sleep(2)
                siteDownloader(language_module)
                time.sleep(4)
                print(f"{language_module.download1}CSS")
                scriptDownloader(globalPath(config) + "css_files.txt", ".css", count)
                time.sleep(2)
                print(f"{language_module.download1}JS")
                scriptDownloader(
                    globalPath(config) + "javascript_files.txt", ".js", count
                )
                dv = input(f"{language_module.confirm1}")
                if "y" in dv:
                    siteD = input(f"{language_module.prompt1}")
                    imgandVidDownlaod(siteD)
                elif "n" in dv:
                    print("Ok!")
                else:
                    print(language_module.idk1)
            # this is the function that starts tookie-osint.
            if "-s" in input1:
                if uname == "":
                 uname = input("Please enter a target before continuing: ").lower()
                 uname_list = [item.strip() for item in uname.split(",")]
                if uname != "":
                    input2 = input("[Y/N]? ⤷ ").lower()
                    if input2 == "y":
                        modes += input1
                        inputnum += input2
                    if input2 == "n":
                        holder = 1

            # Your scanning logic here
            if "-ec" in input1:
                ec = 1
            if "-w" in input1:
                webscrape = True
            if "-O" in input1 or "-o" in input1:
                slectpath = Path.home() / str(input(f"{language_module.path}"))
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
                    except PermissionError:
                        print(language_module.error1)
                    except TypeError:
                        print(language_module.error2)
                else:
                    print(Fore.RED + f"{language_module.error3}" + Fore.RESET)
                    exit(69)
            if "--Wiki" in input1:
                wiki(language_module)
                logo(colorScheme, uname, version, config)
            # code to display all error codes
            if "-a" in input1:
                modes += input1
            # code to do a fast scan
            if "-f" in input1:
                fastMode = 1
            # code to show NSFW sites
            if "-N" in input1:
                modes += input1
         # checks for empty input
         # it will keep printing ⤷ until -s is entered and Y is entered
         if "" in input1 and inputnum != "":
            test = True
         inputnum = ""
         
        else:
         # email osint options
         input3 = input("⤷ ")
         if input3 != "": 
             # will add actions later
            action = {
                 "-s": [emptyModule, []],
                 "-u": [emailinfo, [uname]],
             }
            valid = [key for key in action.keys()]
            option_matched = False
            for option in valid:
                if option in input3:
                    args = action[option][1]
                    action[option][0](*args)
                    option_matched = True
                    break  # Exit the loop if a matching option is found

            if not option_matched:
                print(f"Invalid option: '{input3}' Try --help for more information")
            # this is the function that starts tookie-osint.
            if "-s" in input3:
              inputnum += "idk"
              emailSiteName = get_site_names()
              # this is temporary, i need to add it to the lines below
              print(emailSiteName)
              exit()

                
         if "" in input3 and inputnum != "":
            test = True
            inputnum = ""

if argument.all:
    modes = "-a"

# creates the save file
file_name = uname + ".txt"
file_path = os.path.join("./captured/", file_name)
# check if the directory exists
if os.path.exists("./captured/"):
    # creates the file
    print(" ")
    print(f"{language_module.status2}")
else:
    print(f"{language_module.error4}")
#sets the custom site file argument
if argument.otherfile:
    fastMode = 2
    slectpath = argument.otherfile
    # determins what list of sites to use.
if fastMode == 0:
    # fastmode0 is the default scan mode
    scanFileList(siteList, "./sites/sites.json", language_module)
if fastMode == 1:
    # fastmode1 is the fast scan mode
    scanFileList(siteList, "./sites/fsites.json", language_module)
if fastMode == 2:
    # fastmode2 is the scan from custom site list
    scanFileList(siteList, slectpath, language_module)
# prints ui stuff
print(Fore.GREEN + f"{language_module.scan1}" + uname + Fore.RESET)
print("===========================================================")
if webscrape:
    print(Fore.RED + language_module.note + Fore.RESET + language_module.warning2)
    print("===========================================================")
print("")
siteCount = 0
results = []
# opens the save file and writes working sites to it
with open(file_path, "a") as f:

    for site in siteList:
        siteCount += 1
        with console.status(language_module.status1) as status:
            siteN = site["site"]
            siteNSFW = site["nsfw"]
            siteErrors = site["errorMessage"]
            i = 0 
            
            for item in uname_list:
                scanr =  Startscan(
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
                    language_module,
                    randomheaders,
                    webhook_url
                )
                i += 1
                results.append(str(scanr))

                


print(
    """
===========================================================
     """
)



print(f"{language_module.save1} ./captured/{uname}.txt")
mkcsv = input("Make Output List Into CSV? [Y/n]: ")
if mkcsv == "y":
    csvmaker(f"captured/{uname}.txt", f"captured/{uname}.csv", results)


doreport = input("Do You Want To Run A Report? [Y/n]: ")

if "y" in doreport.lower():
 print("================================")
 print(f"Starting Report With ./captured/{uname}.txt")
 # gets urls from file
 reportUrls = extract_urls(f"./captured/{uname}.txt")
 # Runs the report
 report(reportUrls,uname)


# Asks to be ran again if there are no arguments
if any(vars(argument).values()):
    holder += 1
else:
    startagain = input(f"{language_module.confirm2}").lower()
    if "y" in startagain:
        exec(open("brib.py").read())
    elif "n" in startagain:
        exit()