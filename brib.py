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
print_logoscreen(version)

# reads the configuration file
config.read('./config/config.ini')

# this is the function to update the code
x = random.randint(1, 4)
if (x == 3 and config.get('main', 'checkforupdates') == 'yes'):
    print("You Can Disable Updating In The Config File")
if (x == 2):
    print("Join Our Discord: https://discord.gg/xrdjxyuSQt ")

if (config.get('main', 'checkforupdates') == 'yes'):
    cfu = input("Check For Updates? [y/n]: ⤷ ")
    if "Y" in cfu or "y" in cfu:
        exec(open("./update.py").read())
    elif "N" in cfu or "n" in cfu:
        print("Ok! Ill Ask Later....")
    else:
        print("Not Sure What You Ment. Ill Ask Later")

# asks the user if they want to enable updates
if (config.get('main', 'checkforupdates') == 'no'):
    # gets input
    getNum = random.randint(1, 10)
    if (getNum == 7):
        changeconfig = input("Updates Are Disabed. Wanna Renable Them? [y/n]: ⤷ ")
        # pharses it
        if "Y" in changeconfig or "y" in changeconfig:
            config.set('main', 'checkforupdates', 'yes')
            print("Updates Are Enabled!")
            with open('config.ini', 'w') as f:
                config.write(f)
        elif "N" in changeconfig or "n" in changeconfig:
            print("Ok! Ill Ask Later....")
        else:
            print("Not Sure What You Ment. Ill Ask Later")

# this is the variable that gets the username
uname = input("⤷ ")

# This is where we gather the inputed options and then run them.
# Not all of the options execute on input.

while test != True:
    input1 = input("⤷ ")
    if input1 != "":
        action = {
            '-t': [timeoutC, [modes, input1]],
            '-FS': [fileShare, []],
