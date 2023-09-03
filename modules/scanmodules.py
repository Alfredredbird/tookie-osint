from colorama import *
import requests
import json

def Startscan(modes, siteN, uname,cError, ec,f,siteProgcounter,siteNSFW):
            
            try:
                headers = headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                }
                if "-t" in modes:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=timeout,
                        allow_redirects=False,
                        proxies=False,
                        json=False,
                    )  # 35
                if "-d" in modes:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=1.5,
                        allow_redirects=ars,
                        proxies=False,
                        json=False,
                    )
                if "-c" in modes:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=1.5,
                        allow_redirects=False,
                        proxies=proxies,
                        json=False,
                    )

                else:
                    response = requests.get(
                        siteN + uname,
                        headers=headers,
                        timeout=1.5,
                        allow_redirects=False,
                        proxies=False,
                        json=False,
                    )

                if ec == 1:
                    print(response.status_code)
                if response.status_code == 200:
                    siteProgcounter += 1
            except (requests.exceptions.SSLError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout,requests.exceptions.RetryError,requests.exceptions.ProxyError,requests.exceptions.ConnectionError,requests.exceptions.InvalidHeader,requests.exceptions.InvalidURL,requests.exceptions.TooManyRedirects, requests.exceptions.ChunkedEncodingError):
                connection_error = 1
                #  print(requests.exceptions.HTTPError)
                if "-a" in modes:
                    print("[" + Fore.YELLOW + "E" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "E" + "] " + siteN + uname + "\n")
                cError += 1
                return cError                     
            except KeyboardInterrupt:
                print("""===========================================================""")
                print("Stopping........")
                f.close
                print("Saved Results To File")
                exit(99)
            else:
                if "-a" in modes:
                    if response.status_code >= 300 or response.status_code >= 510:
                        print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                        f.write("[" + "-" + "] " + siteN + uname + "\n")
                    if response.status_code == 406:
                        print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                        f.write("[" + "-" + "] " + siteN + uname + "\n")

                if "-N" in modes:
                    if response.status_code == 200 and siteNSFW == "true":
                        print("["+ Fore.LIGHTMAGENTA_EX+ "NSFW"+ Fore.RESET+ "] "+ siteN+ uname+ "     "+ Fore.RESET)
                        f.write("["+ "+"+ "] "+ siteN+ uname+ "             NSFW"+ "\n")

                    if response.status_code == 200 and siteNSFW == "false":
                        print(
                            "[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname
                        )
                        f.write("[" + "+" + "] " + siteN + uname + "\n")
                if response.status_code == 200 and "-N" not in modes:
                    print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "+" + "] " + siteN + uname + "\n")
                    return siteProgcounter
                if response.status_code == 406 and "-N" not in modes:
                    print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                    f.write("[" + "+" + "] " + siteN + uname + "\n")

def fastmode0(siteList):
    try:
        with open("./sites.json", "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
        return siteList        
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")

        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)


def fastmode1(siteList):
    try:
        with open("./fsites.json", "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
        return siteList        
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")

        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)    

def fastmode2(siteList, slectpath):
    try:
        with open(slectpath, "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")

        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)            