#!/usr/bin/env python

import os
import requests
import argparse

from colorama import Fore
from concurrent.futures import ThreadPoolExecutor, as_completed
from modules.fancy import *
from modules.webscraper import *
from modules.modules import *



#initializes the arg parser
parser = argparse.ArgumentParser( description="Username OSINT scanner",
    prog="tookie-osint",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="""
Examples:
  Basic scan (default txt output):
    tookie-osint -u alfred

  JSON output with 10 threads:
    tookie-osint -u alfred -o json -t 10

  Scan usernames from a file:
    tookie-osint -U users.txt -o csv

  Use proxy and show all results:
    tookie-osint -u alfred -p http://127.0.0.1:8080 -a

  Skip random headers:
    tookie-osint -u alfred --skipheaders

  Use webscraper:
    tookie-osint -u alfred -W

  Use a user file list
    tookie-osint -U users.txt -t 20
""")
#arguments
# parser.add_argument("-h", "--help",)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-u", "--user",help="Username to scan")
group.add_argument("-U", "--userfile",help="File path to username file")
parser.add_argument("-t", "--threads", type=int, default=2, help="Threads. Defualt is 2")
parser.add_argument("-d", "--debug", action='store_true',help="Allows debugging options")
parser.add_argument("-sk", "--skipheaders", action='store_true',help="skips using random user agents")
parser.add_argument("-p", "--proxy", type=str, help="proxy")
parser.add_argument("-W", "--webscraper", action='store_true',help="Toggles uses the webscraper")
parser.add_argument(
    "-o", "--output",
    choices=["txt", "csv", "json"],
    default="txt",
    help="Output format (txt, csv, json)"
)
parser.add_argument("-D", "--delay", type=int, help="Delay webscraper should wait for the page to load")
parser.add_argument("-a", "--all", action='store_true', help="Show all results (positive and negative)")

#initializes the arg parser as a variable
args = parser.parse_args()
#arguments as variables
if args.userfile:
    users = load_user_file(args.userfile)
else:
    users = [args.user]
threads = args.threads
debug = args.debug
skip_headers = args.skipheaders
output_format = args.output
webscrape = args.webscraper
delay = args.delay
allsites = args.all
#makes sure threads is not used with the webscraper
if args.webscraper and args.threads != parser.get_default("threads"):
    parser.print_help()
    parser.exit(
        status=1,
        message="\n[!] Error: -W (webscraper) cannot be used with -t (threads)\n"
    )
# checks for update
check_update()
#asks to download request agent file
get_header_file(debug)
# makes system direcotries
# make_sys_dirs(debug)


# data loading
sites = load_sites(debug)
# debuging options
if debug:
  print("DEBUG")
  print("Opening Scan File")

# loads user agents
user_agents = []
if not skip_headers:
    user_agents = load_user_agents()
# writes scan file (will be removed)
# scan_file(user,0)

# Main Function
all_results = {}

total_users = len(users)

for idx, user in enumerate(users, start=1):
    print(f"\n[+] Scanning username: {user}")
    logo(user, idx, total_users)
    # gets basic system info for the logo
    if webscrape:
        threads = 1
    get_system_data(threads,skip_headers)

    results = []

    if not webscrape:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [
                executor.submit(
                    scan_site, site, user, debug, skip_headers, user_agents, allsites
                )
                for site in sites
            ]

            try:
                for future in as_completed(futures):
                    res = future.result()
                    if res:
                        results.append(res)
            except KeyboardInterrupt:
                print("Stopping!")
                executor.shutdown(wait=False)
                break

    else:
        try:
            scan_webscraper(user, debug, skip_headers, user_agents, delay, allsites)
        except KeyboardInterrupt:
            print("\nStopping web scraper...")
        finally:
            close_driver()

    all_results[user] = results

    # write output per-user
    if output_format == "txt":
        write_txt(user, results)
    elif output_format == "csv":
        write_csv(user, results)
    elif output_format == "json":
        write_json(user, results)
    
print("    ==============================================")
print("Scan done!")
exit(1)
