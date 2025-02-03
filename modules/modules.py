#!/usr/bin/env python3
import argparse
import subprocess
import http.client
import json
import os
import random
import socket
import string
import time
import csv
from configparser import ConfigParser
from os import listdir
from os.path import isfile, join
from pathlib import Path

import requests
import wget
from bs4 import BeautifulSoup
from colorama import *
from rich.console import Console
from torrequest import TorRequest

from modules.configcheck import *

config = ConfigParser()
config.read("./config/config.ini")


def redirects1(modes, input1):
    input2 = input("   ⤷ ")
    if input2 == "":
        lol = 1
    if input2 != "":
        modes += input1
        try:
            ars = bool(input2)
            return input1, modes
        except ValueError:
            print("Timeout Must Be A Number")
            if "-d" in input2:
                input1.replace("-d", "")


def list_proxys(colorScheme):
    # Dictionary to map proxy types to file names
    proxy_types = {  
        "http": "http.txt",
        "socks4": "socks4.txt",
        "socks5": "socks5.txt",
    }

    input2 = input("TYPE:  ⤷ ")
    if input2 == "":
        lol = 1
    # Retrieve file name from dictionary
    file_name = proxy_types.get(input2)  
    if file_name:
        file_path = f"./proxys/{file_name}"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                Lines = file.readlines()
                for count, line in enumerate(Lines, 1):
                    print(f"Proxy {count}: {line.strip()}")
        else:
            print(colorScheme + f"Cant Find The Proxy File for {input2}!")
            print(Fore.RESET)
    else:
        # Case for invalid type
        print(colorScheme + "Invalid proxy type!") 
        print(Fore.RESET)


def read_save(colorScheme, slectpath):
    # Determine file path based on the select_path input
    file_path = Path.home() / "Downloads" / "usernames.tookie-osint" if slectpath == "" else slectpath
    
    # Check if the file exists and read it
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        for line_number, line in enumerate(lines, start=1):
            print(f"Captured {line_number}: {line.strip()}")
    else:
        print(colorScheme + "Can't Find The Save File!")
        print(Fore.RESET)


def ping(colorScheme):
    headers = {"User-Agent": config["Personalizations"]["useragent"]}
    print(colorScheme + "Defaults to HTTPS.")

    print(Fore.RESET + " ")

    reqSite = input("Enter the URL of the site you want to ping: ")

    if not reqSite.startswith("https://") and not reqSite.startswith("http://"):
        urlFix = reqSite.split("//", 1)
        reqSite = urlFix[
            len(urlFix) - 1
        ]  # Account for people doing weird stuff like ftp:// instead
        reqSite = f"https://{reqSite}"

    try:
        test = requests.get(reqSite, headers=headers)
        code = http.client.responses[test.status_code]
        print(Fore.RESET + f"Status code: {test.status_code} ({code})")
    except requests.ConnectionError as e:
        print(colorScheme + f"Connection error: {e}" + Fore.RESET)
    except Exception as e:
        print(colorScheme + f"Unknown error: {e}" + Fore.RESET)


def qexit():
    exitInput = input("Exit? [Y/N]").lower()
    if exitInput == "y":
        exit(0)
    if exitInput == "n":
        print("Continuing....")


def proxyCheck(colorScheme, modes, input1):
    typeInput = input("TYPE: ⤷ ")
    if typeInput != "":
        input2 = input("    IP: ⤷  ")
        if input2 == "":
            print("    You need an IP, silly!")
            lol = 1
        if input2 != "":
            modes += input1

            input3 = input("     PORT: ⤷  ")
            if input3 != "":
                try:
                    # finish adding connectton options
                    prxs = input2 + ":" + input3
                    proxies = {"{typeInput}": prxs}
                #  print("Proxy: " + input2 + ":" + input3)
                except requests.exceptions.ProxyError:
                    print(colorScheme + "Proxy Error!" + Fore.RESET)

                print("")
                print("     Save Proxy To File?")
                saveProxy = input("         [Y/n]?  ⤷ ").lower()
                if saveProxy == "y":
                    with open("proxyList.txt", "a") as fp:
                        fp.write(" \n" + input2 + ":" + input3)
                        fp.close()

                elif saveProxy == "n":
                    print(
                        "Continuing"
                        + Fore.RED
                        + "."
                        + Fore.GREEN
                        + "."
                        + Fore.YELLOW
                        + "."
                        + Fore.RESET
                    )

            if input3 == "":
                print("     Where's the port?!")
                lol = 1
                return lol

    if typeInput == "":
        print("Needs Proxy Type!")
        if "-c" in input1:
            input1.replace("-c", "")


def timeoutC(modes, input1):
    input2 = input("   ⤷ ")
    if input2 == "":
        lol = 1
        return lol
    if input2 != "":
        modes += input1

        try:
            timeout = int(input2)
            return timeout
        except ValueError:
            print("Timeout Must Be A Number")
            if "-t" in input2:
                input1.replace("-t", "")


def darktookie(colorScheme, console, uname):
    # clears the terminal when Dark tookie-osint is ran
    os.system("cls" if os.name == "nt" else "clear")
    test = False
    lol = 0
    inputnum = 0
    start = False
    siteList = []
    modes = ""
    iptext = ""
    try:
        rp = requests.get("http://ipecho.net/plain")
        iptext = rp.text
    except ConnectionError:
        print("Connection Error! Cant Get Ip Address.")
    print(
        Fore.BLACK
        + """
                    ,╓╔╦╦╦╖╓
                ╔▒╠╠╩╙╙╙"╙╙╚╬╠▒╦,
              ,Φ╠╩"   ,╓▄▄╓,    ╙
            @╠╩   *████▀▀▀███▓,   ╬╬,
           ╬╠╙  ▄µ          ╙███   ╬╠µ
          ╠╠╩  ██▌  ╓▒╠╩╝╠╬╦  ╙██   ╠╠
          ╠╠  j██  ⌠╠╩    ╚╠▒  ██▌  ╠╠⌐
          ╠╠   ██  └╠╬    ╠╠╩  ██▌  ╠╠⌐
          ╚╠φ  ╟██   ╚╬╠╠╠╩`  ▄██  ,╠╬
           ╠╠╦  ╙██▌,      ,,  ╙  ,╠╠
            ╚╬`   ╙▀█████████▀   #╠╩
               ,@╦     └└─    ╓@╠╩`
                "╚╠╠▒▒φφφφ@▒╠╠╩╙

    ░█▀▄▒▄▀▄▒█▀▄░█▄▀░░░▀█▀░▄▀▄░▄▀▄░█▄▀░█▒██▀░░
    ▒█▄▀░█▀█░█▀▄░█▒█▒░░▒█▒░▀▄▀░▀▄▀░█▒█░█░█▄▄▒░

 """
    )
    print("Searching The DarkWeb For Usernames With: " + uname + ".")
    print("Your Ip Is: " + iptext)
    print(
        colorScheme
        + "===================================================================="
        + Fore.RESET
    )
    print(
        """
Caution! By Using This Might Expose
You To Dangerous Websites Or Content.
Read More On The Doc's https://github.com/alfredredbird/tookie-osint/wiki
"""
    )
    print(
        colorScheme
        + "===================================================================="
        + Fore.RESET
    )

    input1 = input("⤷  ")
    while test != True:
        if input1 != "":
            # if there is a problem with this code its prob this
            if "-tp" in input1:
                torPassword = input("Tor Password:  ⤷").lower()
            if "-s" in input1:
                input2 = input("Are You Sure? [Y/N]? ⤷ ").lower()
                if input2 == "":
                    lol = 1
                if input2 != "":
                    if input2 == "y":
                        input3 = input("100% Sure? [Y/N]? ⤷ ").lower()
                        if input2 != "":
                            if input2 == "y":
                                #  modes += input1
                                #  inputnum += input2
                                print("Ok..")
                                start = True
                            if input2 == "n":
                                test = False
                                input1 = ""
                                print("Ok! Returing To tookie-osint.")
                                time.sleep(2)
                                return test

                    if input2 == "n":
                        test = False
                        input1 = ""
                        print("Ok! Returing To tookie-osint.")
                        time.sleep(2)
                        return test

        if "" in input1 and inputnum != "":
            test = True
        inputnum = ""
    if start:
        try:
            with open("sites.json", "r") as f:
                for jsonObj in f:
                    siteDic = json.loads(jsonObj)
                    siteList.append(siteDic)
        except FileNotFoundError:
            print(colorScheme + "Cant Find Site File")

            exit(-1)
        except json.JSONDecodeError:
            print(colorScheme + "Error With Site File" + Fore.RESET)
            exit(-9)

        dir_path = Path.home() / "Downloads"
        file_name = "usernames.txt"
        file_path = os.path.join(dir_path, file_name)
        # check if the directory exists
        if os.path.exists(dir_path):
            # create the file
            print(" ")
            print("Creating / Overwriting Save File.")

        else:
            print("Directory doesn't exist.")
        with open(file_path, "w") as f:
            for site in siteList:
                with console.status("Working....") as status:
                    siteN = site["site"]
                    try:
                        tr = TorRequest(password=torPassword)
                        tr.reset_identity()
                        response = tr.get(siteN + uname)

                        if (
                            TorRequest.status_code >= 200
                            and TorRequest.status_code >= 300
                        ):
                            print(
                                "["
                                + Fore.GREEN
                                + "+"
                                + Fore.RESET
                                + "] "
                                + siteN
                                + uname
                            )
                            f.write("[" + "+" + "] " + siteN + uname + "\n")

                    except ConnectionError:
                        print("Connection Error!")


def printFiles():
    # ha ha Only Files. Sounds like something else, I wonder what? (Only Fans)
    onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]
    return onlyfiles


def dirList():
    # gets the files in ./tookie-osint
    my_list = printFiles()
    columns = 3
    spaces = "      "
    # prints the files neetly
    for first, second, third in zip(
        my_list[::columns], my_list[1::columns], my_list[2::columns]
    ):
        print(
            f"{Fore.RED + first: <10}{spaces}{Fore.GREEN + second: <10}{spaces}{Fore.BLUE + third + Fore.RESET}"
        )


def catFile(colorScheme):
    file_path = input("Filname:  ⤷ ")
    try:
        with open(file_path, "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                print(siteDic)

    except FileNotFoundError:
        print(colorScheme + "Cant Find Site File")
    except json.JSONDecodeError:
        print(colorScheme + "Error With Site File" + Fore.RESET)


def scriptDownloader(sitePaths, extinsion, count):
    file1 = open(sitePaths, "r")
    Lines = file1.readlines()
    L = [Lines]
    for line in Lines:
        count += 1
        # downloads the file from the site
        print("Downloading File: " + line)
        url = line
        r = requests.get(url, allow_redirects=True)
        try:
            open(globalPath(config) + "file" + str(count) + extinsion, "wb").write(
                r.content
            )
        except FileNotFoundError:
            print("Cant Find Site! " + "Skiping!")
        except OSError:
            print("Permission Error")


def errorCodes(ec):
    ec = 1
    return ec


# Function to download images
def download_images(image_urls, output_directory):
    for url in image_urls:
        try:
            image_filename = os.path.join(output_directory, os.path.basename(url))
            wget.download(url, image_filename)
            print(f"Downloaded: {image_filename}")
        except Exception as e:
            print(f"Error downloading image: {e}")


# Function to download videos
def download_videos(video_urls, output_directory):
    for url in video_urls:
        try:
            video_filename = os.path.join(output_directory, os.path.basename(url))
            wget.download(url, video_filename)
            print(f"Downloaded: {video_filename}")
        except Exception as e:
            print(f"Error downloading video: {e}")

# Get global default download path from configuration
def globalPath(config):
    config.read("./config/config.ini")
    path = config.get("main", "defaultDlPath")
    return path

# Main function
def imgandVidDownlaod(input2):
    url = input2
    output_directory = globalPath(config)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Find and download images
        img_tags = soup.find_all("img")
        img_urls = [img["src"] for img in img_tags if "src" in img.attrs]
        download_images(img_urls, output_directory)

        # Find and download videos (you might need to adjust this for specific websites)
        video_tags = soup.find_all("video")
        video_urls = [video["src"] for video in video_tags if "src" in video.attrs]
        download_videos(video_urls, output_directory)
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def emptyModule():
    """
    This Module is empty and does nothing. Its for when tookie-osint needs to return something
    """
    return True


def parse_args():
    parser = argparse.ArgumentParser(description="tookie-osint OSINT Tool (Command-Line)")
    parser.add_argument(
        "-s", "--scan",
        action="store_true",
        help="Run tookie-osint scan")
    parser.add_argument(
        "-u", "--username", 
        type=str,
        help="Specify target username(s) (comma-separated)"
    )
    parser.add_argument(
        "-f", "--fast",
        action="store_true",
        help="Run tookie-osint with a fast scan"
    )
    parser.add_argument(
        "-w", "--webscrape",
        action="store_true",
        help="Run tookie-osint with the webscraper"
    )
    parser.add_argument(
        "-o", "--otherfile", 
        type=str,
        help="Specify custom site list"
    )
    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Shows all scanned sites"
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Runs tookie-osint In Debug Mode"
    )
    return parser.parse_args()



def csvmaker(input_file, output_file, string_list):
    # Open the input text file for reading
    with open(input_file, 'r') as txt_file:
        # Read lines from the text file
        lines = txt_file.readlines()

    # Remove newline characters from each line
    lines = [line.strip() for line in lines]

    # Split each line into date and URL
    data = [(line[:10], line[12:]) for line in lines]

    # Open the output CSV file for writing
    with open(output_file, 'w', newline='') as csv_file:

        #checks and counts how many sites work and dont
        minus_count = 0
        plus_count = 0
        for s in string_list:
            minus_count += s.count('-')
            plus_count += s.count('+')
            
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)
        # Write header to the CSV file
        csv_writer.writerow(['Date', 'URL'])
        # Write data to the CSV file
        csv_writer.writerows(data)

    print("Done With CSV!")
    print("Working: " + str(plus_count) + " Not Working: " + str(minus_count))



def loadHeaders(config):
    headers = []
    try:
     with open("proxys/headers.txt") as h:
        for line in h:
            headers.append(line.strip())
     return headers
    except Exception as e:
        try:
         install = input("Looks Like You Dont Have A User Agent File! Want To Download One? (948kb) [y/n]: ")
         if install.lower() == "y":
            response = requests.get("https://raw.githubusercontent.com/alfredredbird/user-agentl-ist/main/header.txt")
    
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract text content from the response
                text_content = response.text
                lines = text_content.splitlines()
                text_content = '\n'.join(lines)
                # Create the directory if it doesn't exist
                directory = os.path.dirname("proxys/")
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Write the text content to the file
                with open("proxys/headers.txt", 'w', encoding='utf-8') as file:
                    file.write(text_content)
                print(f"Agent File Saved To proxys/headers.txt")
                time.sleep(3)
            else:
                print(f"Failed to fetch content from https://raw.githubusercontent.com/alfredredbird/user-agentl-ist/main/header.txt. Status code: {response.status_code}")

         else:    
          print("Ok! Now Using User Agent In Config File.")
          return config.get("main","userandomuseragents")
        except KeyboardInterrupt:
            print("Ok! Now Using User Agent In Config File.")
            return config.get("main","userandomuseragents")

def get_local_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a public DNS server (Google's)
        s.connect(("8.8.8.8", 80))
        # Get the socket's own address
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_site_names(json_path="sites/emailsites.json"):
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
        # Return the keys of the JSON object as a list
        return list(data.keys())
    except FileNotFoundError:
        print(f"File not found: {json_path}")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []
    
