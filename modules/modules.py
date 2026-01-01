import os
import json
from colorama import Fore

#loads sites from the json
def load_sites(debug=False):
    if debug:
        print("Opening site list file")
    
    with open("sites/sites.json", "r", encoding="utf-8") as f:
        data = json.load(f) 
    
    urls = [entry["site"] for entry in data]
    
    if debug:
        print(f"Loaded {len(urls)} URLs")
    
    return urls

# grabs version info and such
def get_info():
 with open("config/version", "r") as f:
    lines = f.readlines()
    f.close()
    return lines

# scan file
def scan_file(user, num, data=""):
    if num == 0:
        # write header
        with open(f"{user}.txt", "a") as scanfile:
            scanfile.write(f"Tookie-OSINT {get_info()}\n\n") 
            scanfile.close()
    elif num == 1:
        #write url
        with open(f"{user}.txt", "a") as scanfile:
            scanfile.write(f"{data}\n")
            scanfile.close()

# Assembles success/fail string
def sitestring(url, user, code, colored=True):
    if url == "":
        return "No URL"
    if user == "":
        return "No Username"
    if code == "":
        return "No Code or Bugged code"

    if 200 <= code <= 305:
        symbol = "+" 
        if colored:
            symbol = Fore.GREEN + "+" + Fore.RESET
        return f"[{symbol}] {url}{user}"
    elif 400 <= code <= 500:
        symbol = "-"
        if colored:
            symbol = Fore.RED + "-" + Fore.RESET
        return f"[{symbol}] {url}{user}"
    elif 500 <= code <= 600:
        symbol = "E"
        if colored:
            symbol = Fore.YELLOW + "E" + Fore.RESET
        return f"[{symbol}] {url}{user}"

    