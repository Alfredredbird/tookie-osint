#!/usr/bin/env python3
from __future__ import print_function
from configparser import ConfigParser
from time import sleep
from rich.console import Console
from alive_progress import *
from timeit import default_timer
from colorama import Fore, Back, Style
from pathlib import Path
from socket import socket
from modules.modules import *
from modules.printmodules import *
from modules.scanmodules import *
import random
import urllib.request, urllib.error, urllib.parse
import sys
import os
import platform
import logging
import json
import requests
import time
import site
import string

# variables
domain_extensions = False
alist = True
test = False
testall = False
fastMode = 0
cError = 0
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

# These stores the loaded site infos
siteList = []
siteNSFW = []

# checks if the nesasary files exist
if (os.path.exists('./config/config.ini') == True):
    print("Config File exists")
else:
    print("Cant Find Nesasary Files. Try Reinstalling Alfred")
    exit(1)

if (os.path.exists('./update.py') == True):
    print("Update File exists")
else:
    print("Cant Find Nesasary Files. Try Reinstalling Alfred")
    exit(1)

# opens the config and gets the version number
with open("./config/version.cfg", "r") as fp:
    version = fp.read()


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


# clears the terminal when Alfred is ran
os.system("cls" if os.name == "nt" else "clear")

# this prints the start up screen and passes the verion varaible in
if ("ish" in str(platform.system())):
    print_logoscreenISH(version)
else:    
    print_logoscreen(version)
#does config stuff
configUpdateStuff(config)
#this is the variable that gets the username
uname = input("⤷ ")

# This is where we gather the inputed options and then run them.
# Not all of the options execute on input.
while test != True:
    input1 = input("⤷ ")
    if input1 != "":
        action = {'-t':[timeoutC,[modes, input1]], '-FS':[fileShare,[]],'-q':[qexit,[]],'-gsl':[siteListGen,[console, testall, get_random_string,domain_extensions,uname]], '-c':[proxyCheck,[modes, input1]], '-lp':[list_proxys,[]], '-h':[print_help,[]], '--help':[print_help,[]], '-d':[redirects1,[modes, input1]],'-u':[unameinfo,[uname]],'-Cat':[catFile,[]],'--Config':[configEditor,[config]],'-p':[ping,[]],'--ping':[ping,[]],'-r':[read_save,[slectpath]],'--read':[read_save,[slectpath]],'--Clear':[logo,[uname]],'clear':[logo,[uname]]}
        valid = [key for key in action.keys()]
        for option in valid:
            if option in input1:
                args = action[option][1]
                action[option][0](*args) 
#option phareser for options that cant be put into the option pharser above.     
        if "-ls" in input1:
           #gets the files in ./alfred
           my_list = printFiles()
           columns = 3
           spaces = "      "
           #prints the files neetly
           for first, second, third in zip(my_list[::columns], my_list[1::columns], my_list[2::columns]):
            print(f'{Fore.RED + first: <10}{spaces}{Fore.GREEN + second: <10}{spaces}{Fore.BLUE + third + Fore.RESET}')   
        if "-S" in input1:
            print("Sites Many Not Allow Downloading Their Site Files. Use At Your Own Risk.")
            dirDump("./downloadedSites/")
            time.sleep(2)
            siteDownloader(modes, input1)
            time.sleep(2)
            print("Downloading CSS")
            scriptDownloader("./downloadedSites/css_files.txt", ".css")
            time.sleep(2)
            print("Downloading JS")
            scriptDownloader("./downloadedSites/javascript_files.txt", ".js")
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
                    # modes = ""
                    # inputnum = ""
                    # uname = input("⤷ ")
                    # test = False
                    # input2 = ""
                    # input1 = ""
                    holder = 1
        if "-ec" in input1:
            ec = 1  
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
             logo(uname)                  
        #code to display all error codes    
        if "-a" in input1:
            modes += input1
        #code to do a fast scan
        if "-f" in input1:
            fastMode = 1
        #code to run a LOOOOOOOOOONG scan    
        if "-m" in input1:
            fastMode = 3    
        #code to show NSFW sites
        if "-N" in input1:
            modes += input1
        #code to acses Dark Alfred
        if "-Tor" in input1:
            darkAlfred(console, uname)
            logo(uname)
           
    #checks for empty input
    if "" in input1 and inputnum != "":
        test = True
    inputnum = ""
#creates the save file    
dir_path = Path.home() / "Downloads"
file_name = "usernames.alfred"
file_path = os.path.join(dir_path, file_name)
# check if the directory exists
if os.path.exists(dir_path):
    # creates the file
    print(" ")
    print("Creating / Overwriting Save File.")
else:
    print("Directory doesn't exist.")

#determins what list of sites to use.
if fastMode == 0:
    #fastmode0 is the default scan mode
    scanFileList(siteList,"./sites/sites.json")
if fastMode == 1:
    #fastmode1 is the fast scan mode
    scanFileList(siteList,"./sites/fsites.json")
if fastMode == 2:
    #fastmode2 is the scan from custom site list
    scanFileList(siteList, slectpath)
if fastMode == 3:
    #fastmode2 is the scan from custom site list
    scanFileList(siteList, "./sites/Megasites.json")    
#prints ui stuff
print(Fore.GREEN + "searching for sites with: " + uname + Fore.RESET)
print("")
siteCount = 0
#opens the save file and writes working sites to it
with open(file_path, "w") as f:
    for site in siteList:
        siteCount += 1
        with console.status("Working....") as status:
            siteN = site["site"]
            siteNSFW = site["nsfw"]
            Startscan(modes, siteN, uname,cError, ec, f, siteProgcounter, siteNSFW)
#checks for a connection error and prints
connectionError(cError,f)
#calculates the percentage
def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100
print("Saved Results To File")
#Asks to be ran again
startagain = input("Run Again?: [Y/N] ⤷ ")
if "Y" in startagain or "y" in startagain:
    exec(open("brib.py").read())
elif "N" in startagain or "n" in startagain:
    exit()