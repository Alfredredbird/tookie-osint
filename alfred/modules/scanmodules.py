import datetime
import json
from configparser import ConfigParser
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs
from colorama import *

from modules.configcheck import *
from modules.webscrape import *

config = ConfigParser()

date = datetime.date.today()


# scan logic
def Startscan(
    modes,
    siteN,
    uname,
    cError,
    ec,
    f,
    siteProgcounter,
    siteNSFW,
    ars,
    webscrape,
    siteErrors,
    date,
    language_module,
):
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
            if webscrape == False:
                result = ""
            if webscrape == True:
                # error message to find
                error_to_find = siteErrors
                # combineds to make url
                website_url = siteN + uname
                # gets driver from the config
                config.read("./config/config.ini")
                selected_webdriver = config.get("main", "browser")
                if selected_webdriver:
                    result = scrape(
                        website_url, error_to_find, selected_webdriver, language_module
                    )

                # print(result)
        if ec == 1:
            print(response.status_code)
        if response.status_code == 200 and result == "No":
            siteProgcounter += 1
    except (
        requests.exceptions.SSLError,
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ReadTimeout,
        requests.exceptions.RetryError,
        requests.exceptions.ProxyError,
        requests.exceptions.ConnectionError,
        requests.exceptions.InvalidHeader,
        requests.exceptions.InvalidURL,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.ChunkedEncodingError,
        requests.exceptions.ContentDecodingError,
    ):
        connection_error = 1
        if "-a" in modes:
            print("[" + Fore.YELLOW + "E" + Fore.RESET + "] " + siteN + uname)
            f.write(str(date) + "[" + "E" + "] " + siteN + uname + "\n")
        cError += 1
        return cError
    except KeyboardInterrupt:
        print("""===========================================================""")
        print(language_module.status7)

        f.close
        print(language_module.save2)
        exit(99)
    else:
        if webscrape == True:
            if "-a" in modes:
                if (
                    response.status_code >= 400
                    and response.status_code <= 510
                    and result == "Yes"
                ):
                    print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                    f.write(str(date) + "[" + "-" + "] " + siteN + uname + "\n")
                # if response.status_code == 406 and result == "Yes":
                #     print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                #     f.write("[" + "-" + "] " + siteN + uname + "\n")

            if "-N" in modes:
                if (
                    response.status_code == 200
                    and siteNSFW == "true"
                    and result == "No"
                ):
                    print(
                        "["
                        + Fore.LIGHTMAGENTA_EX
                        + "NSFW"
                        + Fore.RESET
                        + "] "
                        + siteN
                        + uname
                        + "     "
                        + Fore.RESET
                    )
                    f.write(
                        str(date)
                        + "["
                        + "+"
                        + "] "
                        + siteN
                        + uname
                        + "             NSFW"
                        + "\n"
                    )
                if (
                    response.status_code == 200
                    and siteNSFW == "Unknown"
                    and result == "No"
                ):
                    print(
                        "["
                        + Fore.BLACK
                        + "NSFW?"
                        + Fore.RESET
                        + "] "
                        + siteN
                        + uname
                        + "     "
                        + Fore.RESET
                    )
                    f.write(
                        str(date)
                        + "["
                        + "+"
                        + "] "
                        + siteN
                        + uname
                        + "             NSFW?"
                        + "\n"
                    )

                if (
                    response.status_code == 200
                    and siteNSFW == "false"
                    and result == "No"
                ):
                    print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                    f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")
            if (
                response.status_code >= 200
                and response.status_code <= 390
                and "-N" not in modes
                and result == "No"
            ):
                print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")
                return siteProgcounter
            if response.status_code == 406 and "-N" not in modes and result == "No":
                print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                f.write("[" + "+" + "] " + siteN + uname + "\n")
        if webscrape == False:
            if "-a" in modes:
                if response.status_code >= 300 and response.status_code <= 510:
                    print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                    f.write(str(date) + "[" + "-" + "] " + siteN + uname + "\n")
                # if response.status_code == 406 and result == "Yes":
                #     print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                #     f.write("[" + "-" + "] " + siteN + uname + "\n")

            if "-N" in modes:
                if response.status_code == 200 and siteNSFW == "true":
                    print(
                        "["
                        + Fore.LIGHTMAGENTA_EX
                        + "NSFW"
                        + Fore.RESET
                        + "] "
                        + siteN
                        + uname
                        + "     "
                        + Fore.RESET
                    )
                    f.write(
                        str(date)
                        + "["
                        + "+"
                        + "] "
                        + siteN
                        + uname
                        + "             NSFW"
                        + "\n"
                    )
                if response.status_code == 200 and siteNSFW == "Unknown":
                    print(
                        "["
                        + Fore.BLACK
                        + "NSFW?"
                        + Fore.RESET
                        + "] "
                        + siteN
                        + uname
                        + "     "
                        + Fore.RESET
                    )
                    f.write(
                        str(date)
                        + "["
                        + "+"
                        + "] "
                        + siteN
                        + uname
                        + "             NSFW?"
                        + "\n"
                    )
                if response.status_code == 200 and siteNSFW == "false":
                    print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                    f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")
            if response.status_code == 200 and "-N" not in modes:
                print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")
                return siteProgcounter
            if response.status_code == 406 and "-N" not in modes:
                print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")


def scanFileList(siteList, slectpath, language_module):
    try:
        with open(slectpath, "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
        return siteList
    except FileNotFoundError:
        print(Fore.RED + language_module.error7)
        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + language_module.error9 + Fore.RESET)
        exit(-9)


def fileShare(language_module):
    host = input(language_module.fs1)
    if "Y" in host or "y" in host:
        print(language_module.fs2)
        exec(open("modules/recive.py").read())
    elif "N" in host or "n" in host:
        print(language_module.fs3)
        exec(open("modules/sender.py").read())

    else:
        print(language_module.idk1)


def siteDownloader(language_module):
    input2 = input("SITE: ⤷ ")
    if input2 == "":
        lol = 1
    if input2 != "":
        try:
            url = str(input2)

            # initialize a session
            session = requests.Session()
            # set the User-agent as a regular browser
            session.headers[
                "User-Agent"
            ] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

            # get the HTML content
            html = session.get(url).content

            # parse HTML using beautiful soup
            soup = bs(html, "html.parser")

            # get the JavaScript files
            script_files = []

            for script in soup.find_all("script"):
                if script.attrs.get("src"):
                    # if the tag has the attribute 'src'
                    script_url = urljoin(url, script.attrs.get("src"))
                    script_files.append(script_url)

            # get the CSS files
            css_files = []

            for css in soup.find_all("link"):
                if css.attrs.get("href"):
                    # if the link tag has the 'href' attribute
                    css_url = urljoin(url, css.attrs.get("href"))
                    css_files.append(css_url)

            print(language_module.siteDl1, len(script_files))
            print(language_module.siteDl2, len(css_files))

            # write file links into files

            with open(globalPath(config) + "javascript_files.txt", "w") as f:
                for js_file in script_files:
                    print(js_file, file=f)

            with open(globalPath(config) + "css_files.txt", "w") as f:
                for css_file in css_files:
                    print(css_file, file=f)
        except requests.exceptions.ConnectionError:
            print(language_module.error8)
        except requests.exceptions.RetryError:
            print(language_module.error8)
        except requests.exceptions.HTTPError:
            print(language_module.error8)
        except requests.exceptions.InvalidURL:
            print(language_module.error8)
        except ConnectionError:
            print(language_module.error8)
        except requests.exceptions.RequestException:
            print(language_module.error8)
        except ValueError:
            print(language_module.error8)
