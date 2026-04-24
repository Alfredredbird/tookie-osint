import os
import re
import csv
import sys
import json
import time
import random
import signal
import platform
import requests
import threading
from colorama import Fore
from modules.webscraper import *


# Restrict caller-supplied usernames to a safe filename fragment before they
# are used as output file paths. Without this, "-u ../../../tmp/x" (or any
# -U userfile line containing path separators) would let the caller steer the
# output file anywhere the invoking user can write. Replaces every character
# outside [A-Za-z0-9._-] with "_", collapses ".." sequences, refuses empty
# or dot-only results, and caps length at 128.
_UNSAFE_FILENAME_CHARS = re.compile(r"[^A-Za-z0-9._-]")


def _safe_filename(user):
    if not isinstance(user, str):
        user = str(user)
    safe = _UNSAFE_FILENAME_CHARS.sub("_", user)
    safe = safe.replace("..", "_")
    safe = safe.strip(".")
    if not safe:
        safe = "output"
    return safe[:128]


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

# loads the json feilds for scraping
def load_fields():
    feilds_file = os.path.join(BASE_DIR, "sites", "feilds.json")
    with open(feilds_file, "r") as f:
        return json.load(f)

# grabs version info and such
def get_info():
 version_file = os.path.join(BASE_DIR, "config", "version")
 with open(version_file, "r") as f:
    lines = f.readline()
    f.close()
    return lines

# scan file
def scan_file(user, num, data=""):
    safe_user = _safe_filename(user)
    if num == 0:
        # write header
        with open(f"{safe_user}.txt", "a") as scanfile:
            scanfile.write(f"Tookie-OSINT {get_info()}\n\n")
            scanfile.close()
    elif num == 1:
        #write url
        with open(f"{safe_user}.txt", "a") as scanfile:
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

def get_system_data(threads, skip_headers):
    """Print basic system information."""
    arc = platform.machine()
    system = platform.system()
    python_version = platform.python_version()
    node = platform.node()

    system_lower = system.lower()

    if "linux" in system_lower:
        os_color = Fore.YELLOW
    elif "nt" in system_lower or "windows" in system_lower:
        os_color = Fore.BLUE
    else:
        os_color = Fore.RESET

    print(f"    CPU: {arc}")
    print(f"    OS: {os_color}{system}{Fore.RESET}")
    print(f"    System: {Fore.RED}{node}{Fore.RESET}")
    print(f"    Python Version: {Fore.BLUE}{python_version}{Fore.RESET}")
    print(f"    Threads: {Fore.GREEN}{threads}{Fore.RESET}")

    headers_loaded = 0 if skip_headers else count_header_lines()
    print(f"    Headers Loaded: {headers_loaded}")

    print("    " + "=" * 45)

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
    if not os.path.isfile(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


# scan sites
def scan_site(site, user, debug, skip_headers, user_agents, allsites=False):
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
        if not skip_headers and user_agents:
            headers = {"User-Agent": random.choice(user_agents)}

        r = requests.get(url, headers=headers, timeout=10)
        if shutdown_event.is_set():
            return None

        code = r.status_code
        found = 200 <= code <= 305

        result["status"] = code
        result["found"] = found

        if debug:
            print(f"[DEBUG] Hit: {url} Code: {code}")

        # 🔹 PRINT LOGIC
        if found or allsites:
            print(sitestring(site, user, code))

        # 🔹 RETURN LOGIC
        if found or allsites:
            return result

        return None

    except requests.RequestException as e:
        if debug:
            print(f"[!] Skipping {url}: {e}")

        if allsites:
            return result

        return None


# file writing related functions
def write_txt(user, results):
    safe_user = _safe_filename(user)
    with open(f"{safe_user}.txt", "w") as f:
        f.write(f"Tookie-OSINT {get_info()}\n\n")
        f.write("found url\n")
        for r in results:
            f.write(f"{str(r['found']).lower():<6} {r['url']}\n")

def write_csv(user, results):
    safe_user = _safe_filename(user)
    with open(f"{safe_user}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["found", "url", "status"])
        for r in results:
            writer.writerow([r["found"], r["url"], r["status"]])

def write_json(user, results):
    safe_user = _safe_filename(user)
    with open(f"{safe_user}.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def scan_webscraper(user, field_configs=None, debug=False, skip_headers=False, user_agents=None, delay=None,allsites=False):
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
        domain = site_url.replace("https://", "").replace("http://", "").split("/")[0].removeprefix("www.")
        url = site_url + user

        site_fields = field_configs.get(domain) if field_configs else None

        if delay:
            check_site(url, error_message, site_fields, allsites, delay)
        else:
            check_site(url, error_message, site_fields, allsites)
        if debug:
            print(f"Expected error message: {error_message}")    


def write_to_file(user, results, output_format):
    if output_format == "txt":
        write_txt(user, results)
    elif output_format == "csv":
        write_csv(user, results)
    elif output_format == "json":
        write_json(user, results)

def check_update():
    
    # Checks if a new version of Tookie-OSINT is available.
    
    remote_url = "https://raw.githubusercontent.com/Alfredredbird/tookie-osint/refs/heads/main/config/version"
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

def is_arch():
    # --- Arch Linux Package Check ---
 if os.path.exists("/etc/arch-release"):
    try:
        import selenium
        import webdriver_manager
    except ImportError:
        print(f"\n{Fore.YELLOW}[!] Arch Linux detected. You need to install the webdriver manger and selenium before using the webscraper.")
        print(f"{Fore.YELLOW}    if you already have it installed, ignore this meesage.")
        print(f"{Fore.CYAN}    Run: sudo pacman -S python-selenium python-webdriver-manager")
        print(f"{Fore.CYAN}    Or if using an AUR helper: yay -S python-selenium python-webdriver-manager\n")

def load_user_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
