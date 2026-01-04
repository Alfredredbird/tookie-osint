import os
import csv
import sys
import json
import random
import signal
import platform
import requests
import threading
from colorama import Fore
from modules.webscraper import *

# shutdown event
shutdown_event = threading.Event()
def handle_sigint(sig, frame):
    print("\n[!] Interrupted, shutting stopping...")
    shutdown_event.set()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#loads sites from the json
def load_sites(debug=False):
    if debug:
        print("Opening site list file")
    sites_file = os.path.join(BASE_DIR, "sites", "sites.json")
    with open(sites_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    urls = [entry["site"] for entry in data]

    if debug:
        print(f"Loaded {len(urls)} URLs")

    return urls

# grabs version info and such
def get_info():
 version_file = os.path.join(BASE_DIR, "config", "version")
 with open(version_file, "r") as f:
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

def get_system_data(threads,skipheaders):
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
    if skipheaders:
     print("    Headers Loaded: 0")
    else:
     print("    Headers Loaded: " + str(count_header_lines()))
    print("    ==============================================")

# grabs header file from github
def get_header_file(debug=False):
    url = "https://raw.githubusercontent.com/Alfredredbird/user-agentl-ist/refs/heads/main/header.txt"
    # Use BASE_DIR here
    save_path = os.path.join(BASE_DIR, "sites", "headers.txt")

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

        print(f"[+] headers.txt downloaded successfully at {save_path}")

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

def count_header_lines(path=None):
    if path is None:
        path = os.path.join(BASE_DIR, "sites", "headers.txt")
    count = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip(): 
                count += 1
    return count

def load_user_agents(path=None):
    if path is None:
        path = os.path.join(BASE_DIR, "sites", "headers.txt")
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


# scan sites
def scan_site(site, user, debug, skip_headers, user_agents):
    if shutdown_event.is_set():
        return None
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
        if shutdown_event.is_set():
            return None

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


def scan_webscraper(user, debug=False, skip_headers=False, user_agents=None, delay=None,allsites=False):
    """
    loads sites/sites.json and calls check_site with URL + errorMessage.
    user: the username to append to the site URL
    """
    if user_agents is None:
        user_agents = []

    if debug:
        print("[*] Loading sites with error messages...")
    sites_file = os.path.join(BASE_DIR, "sites", "sites.json")
    with open(sites_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for entry in data:
        site_url = entry.get("site", "")
        error_message = entry.get("errorMessage", "No error message defined")
        url = site_url + user

        if delay:
            check_site(url, error_message,allsites, delay)
        else:
            check_site(url, error_message,allsites)
        if debug:
            print(f"Expected error message: {error_message}")    


def write_to_file(output_format):
    if output_format == "txt":
        write_txt(user, results)
    elif output_format == "csv":
        write_csv(user, results)
    elif output_format == "json":
        write_json(user, results)

def check_update():
    
    # Checks if a new version of Tookie-OSINT is available.
    
    remote_url = "https://raw.githubusercontent.com/Alfredredbird/tookie-osint/refs/heads/dev/config/version"
    local_version = get_info().strip()

    try:
        response = requests.get(remote_url, timeout=10)
        response.raise_for_status()
        latest_version = response.text.strip()

        if latest_version == local_version:
            print(f"[✓] You are running the latest version: {local_version}")
            return False, latest_version
        else:
            print(f"[!] Update available! Local: {local_version} → Latest: {latest_version}")
            time.sleep(1)
            return True, latest_version

    except requests.RequestException as e:
        print(f"[!] Failed to check for updates: {e}")
        return False, local_version