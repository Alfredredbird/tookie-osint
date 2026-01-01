import os
import requests
import argparse

from colorama import Fore
from modules.modules import *
from modules.fancy import *



#initializes the arg parser
parser = argparse.ArgumentParser()
#arguments
# parser.add_argument("-h", "--help",)
parser.add_argument("-u", "--user",required=True)
parser.add_argument("-U", "--userfile",)
parser.add_argument("-t", "--threads",)
parser.add_argument("-d", "--debug", action='store_true')
parser.add_argument("-p", "--proxy", type=str)
parser.add_argument("-N", "--nsfw", action='store_true')


#initializes the arg parser as a variable
args = parser.parse_args()
#arguments as variables
user = args.user
userfile = args.userfile
threads = args.threads
debug = args.debug

# prints logo
logo(user)

# data loading
sites = load_sites(debug)
# debuging options
if debug:
  print("DEBUG")
  print("Opening Scan File")

# writes scan file
scan_file(user,0)
# Main Function
for site in sites:
    url = site + user
    try:
     request = requests.get(url)
     code = request.status_code
     if debug:
        print(f"Hit: {url} Code: {code}")
     try:
      scan_file(user,1,sitestring(url,user,code, False))
     except Exception as e:
      print(e)

    except requests.RequestException as e:
        print(f"[!] Skipping {url} due to error: {e}")
        continue 
    except KeyboardInterrupt:
        print("Stopping!")
        exit(1)
    # prints status codes
    print(sitestring(url,user,code))
    