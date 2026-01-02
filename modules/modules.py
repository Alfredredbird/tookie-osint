import os
import csv
import json
import random
import platform
import requests
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
    lines = f.readline()
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

def get_system_data(threads):
    # gets basic system info
    arc = platform.machine()
    typ = platform.system()
    pyv = platform.python_version()
    node = platform.node()

    print("    CPU: " + arc)
    if "linux" in typ.lower():
      print("    OS:" + Fore.YELLOW + typ + Fore.RESET)
    if "nt" in typ.lower() or "windows" in typ.lower():
      print("    OS:" + Fore.BLUE + typ + Fore.RESET)
    print("    System: " + Fore.RED + str(node) + Fore.RESET)
    print("    Python Version: " + Fore.BLUE + str(pyv) + Fore.RESET)
    print("    Threads: " + Fore.GREEN + str(threads) + Fore.RESET)
    print("    ==============================================")

# grabs header file from github
def get_header_file(debug=False):
    url = "https://raw.githubusercontent.com/Alfredredbird/user-agentl-ist/refs/heads/main/header.txt"
    save_path = "sites/headers.txt"

    if os.path.isfile(save_path):
        if debug:
         print("[+] headers.txt already exists, skipping download")
        return

    choice = input(
        "[?] headers.txt not found.\n"
        "    Download it from GitHub? (y/n): "
    ).strip().lower()

    if choice not in ("y", "yes"):
        print("[-] Skipped downloading headers.txt")
        return

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    try:
        print("[*] Downloading headers.txt...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(save_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print("[+] headers.txt downloaded successfully")

    except requests.RequestException as e:
        print(f"[!] Failed to download headers.txt: {e}")

# makes needed directories
def make_sys_dirs(debug=False):
    dirs = ["sites","lang","docs","config","modules"]
    for dir in dirs:
        try:
         os.mkdir(dir)
        except Exception:
            if debug:
             print(dir + " folder is here")
            continue


def load_user_agents(path="sites/headers.txt"):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

# scan sites
def scan_site(site, user, debug, skip_headers, user_agents):
    url = site + user
    result = {
        "url": url,
        "found": False,
        "status": None
    }

    try:
        headers = None
        if not skip_headers:
            headers = {"User-Agent": random.choice(user_agents)}

        r = requests.get(url, headers=headers, timeout=10)
        code = r.status_code

        result["status"] = code
        result["found"] = 200 <= code <= 305

        if debug:
            print(f"[DEBUG] Hit: {url} Code: {code}")

        print(sitestring(site, user, code))
        return result

    except requests.RequestException as e:
        if debug:
            print(f"[!] Skipping {url}: {e}")
        return result

# file writing related functions
def write_txt(user, results):
    with open(f"{user}.txt", "w") as f:
        f.write(f"Tookie-OSINT {get_info()}\n\n")
        f.write("found url\n")
        for r in results:
            f.write(f"{str(r['found']).lower():<6} {r['url']}\n")

def write_csv(user, results):
    with open(f"{user}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["found", "url", "status"])
        for r in results:
            writer.writerow([r["found"], r["url"], r["status"]])

def write_json(user, results):
    with open(f"{user}.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)