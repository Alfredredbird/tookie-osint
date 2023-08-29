#!/usr/bin/env python
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
import urllib.request
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
siteProgcounter = 0
ec = 0
console = Console()
config = ConfigParser()
slectpath = ""
version = ""
modes = ""
inputnum = ""
ars = ""
# site lists
siteList = []
siteNSFW = []
#opens the config and gets the version number
with open("./config/version.cfg", "r") as fp:
    version = fp.read()
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str
# clears the terminal when Alfred is ran
os.system("cls" if os.name == "nt" else "clear")
#this prints the start up screen and passes the verion varaible in
print_logoscreen(version)
#reads the configuration file 
config.read('./config/config.ini')
#this is the function to update the code
x = random.randint(1, 4)
if(x == 3 and config.get('main', 'checkforupdates') == 'yes'):
    print("You Can Disable Updating In The Config File")
if(x == 2):
    print("Join Our Discord: https://discord.gg/xrdjxyuSQt ")
    


if (config.get('main', 'checkforupdates') == 'yes'):
 cfu = input("Check For Updates? [y/n]: ⤷ ")
 if "Y" in cfu or "y" in cfu:
        exec(open("./update.py").read())
 elif "N" in cfu or "n" in cfu:
        print("Ok! Ill Ask Later....")
 else: 
        print("Not Sure What You Ment. Ill Ask Later")
  
#asks the user if they want to enable updates    
if (config.get('main', 'checkforupdates') == 'no'):
 #gets input
 getNum = random.randint(1, 10)
 if(getNum == 7):
  changeconfig = input("Updates Are Disabed. Wanna Renable Them? [y/n]: ⤷ ")
 #pharses it
  if "Y" in changeconfig or "y" in changeconfig:
        config.set('main', 'checkforupdates', 'yes')
        print("Updates Are Enabled!")
        with open('config.ini', 'w') as f:
            config.write(f)
  elif "N" in changeconfig or "n" in changeconfig:
        print("Ok! Ill Ask Later....")
  else: 
        print("Not Sure What You Ment. Ill Ask Later")
        
#this is the variable that gets the username
uname = input("⤷ ")
# This is where we gather the inputed options and then run them.
# Not all of the options execute on input.
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
            siteListGen(console, testall, get_random_string,domain_extensions,uname)
        if "-d" in input1:
          d_option(modes,input1)
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
        # code to read and check files
        if "-r" in input1 or "--read" in input1:
            R_option(slectpath)
        #code to ping a site
        if "-p" in input1 or "--ping" in input1:
            p_option()
        #code to display all error codes    
        if "-a" in input1:
            modes += input1
        #code to do a fast scan
        if "-f" in input1:
            fastMode = 1
        #code to show NSFW sites
        if "-N" in input1:
            modes += input1
        #prints the help menu
        if "-h" in uname or "--help" in uname or "-h" in input1 or "--help" in input1:
            print_help()
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
    fastmode0(siteList)
if fastMode == 1:
    #fastmode1 is the fast scan mode
    fastmode1(siteList)
if fastMode == 2:
    #fastmode2 is the scan from custom site list
    fastmode2(siteList, slectpath)
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
