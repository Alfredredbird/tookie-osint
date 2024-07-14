import datetime
import json
from configparser import ConfigParser
from urllib.parse import urljoin
from selenium.common.exceptions import NoSuchDriverException
import random
import requests
from bs4 import BeautifulSoup as bs
from colorama import *
from modules.webhook import *
from modules.webscrape import *
from modules.configcheck import *
config = ConfigParser()
config.read("./config/config.ini")

date = datetime.date.today()

# gets driver from the config
config.read("./config/config.ini")
selected_webdriver = config.get("main", "browser")

try:
 scraper = WebScraper(selected_webdriver)
except selenium.common.NoSuchDriverException:
    print("Uh Oh! Looks Like Your Device Does Not Support Our WebScraper :(")    
except Exception as e:
    print("Uh Oh! Looks Like Your Device Does Not Support Our WebScraper :(")
            

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
    randomheaders,
    webhook_url
):
    try:
        if config["main"]["userandomuseragents"] == "no":
            header = {"User-Agent": config["Personalizations"]["useragent"]}
        elif config["main"]["userandomuseragents"] == "yes" and os.path.exists("proxys/headers.txt"):
            header = {"User-Agent": str(random.choice(randomheaders))}
            if "-a" in modes:
                print(header)
        elif not os.path.exists("proxys/headers.txt"):
            header = {"User-Agent": config["Personalizations"]["useragent"]}
        # Timeout and proxies settings based on the mode flags
        timeout_setting = 1.5
        allow_redirects_setting = ars if "-d" in modes else False
        proxies_setting = None if "-c" not in modes or "-t" in modes else proxies

        response = requests.get(
            siteN + uname,
            headers=header,
            timeout=timeout_setting,
            allow_redirects=allow_redirects_setting,
            proxies=proxies_setting,
            json=False, # Assuming json=False is default for all requests
        )

        if not webscrape:
            result = ""
        if webscrape:
            # error message to find
            error_to_find = siteErrors
            # combineds to make url
            website_url = siteN + uname
            if selected_webdriver:
                result = scraper.scrape(
                    website_url, error_to_find, language_module
                )

                # print(result)
        if ec == 1:
            print(response.status_code)
        if response.status_code == 200 and result == "No":
            siteProgcounter += 1
    
    
        if webscrape:
            if response.status_code >= 200 and response.status_code <= 399 and result == "No":
                print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")
                return str(date) + "[" + "+" + "] " + siteN + uname
            if response.status_code >= 400 and response.status_code <= 500 and result == "Yes":
                print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                f.write(str(date) + "[" + "-" + "] " + siteN + uname + "\n")
                return str(date) + "[" + "-" + "] " + siteN + uname 

        

        if not webscrape:
            if response.status_code >= 200 and "-N" not in modes and response.status_code <= 399:
                print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")
                if webhook_url != "none":
                 send_webhook_message(webhook_url, uname, f"{siteN}{uname}")
                return str(date) + "[" + "+" + "] " + siteN + uname
            
            if response.status_code >= 400 and response.status_code <= 500 and "-a" in modes:
                print("[" + Fore.RED + "-" + Fore.RESET + "] " + siteN + uname)
                f.write(str(date) + "[" + "-" + "] " + siteN + uname + "\n")
                return str(date) + "[" + "-" + "] " + siteN + uname
            
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
                    return str(date)+"["+"+"+ "] "+ siteN + uname + "             NSFW"
                elif response.status_code == 200 and siteNSFW == "Unknown":
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
                    return str(date)+"["+"+"+ "] "+ siteN + uname + "             NSFW?"
                elif response.status_code == 200 and siteNSFW == "false":    
                    print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + siteN + uname)
                    f.write(str(date) + "[" + "+" + "] " + siteN + uname + "\n")
                    return str(date) + "[" + "+" + "] " + siteN + uname
       




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
            return str(date) + "[" + "E" + "] " + siteN + uname
        
    except KeyboardInterrupt:
        print("""===========================================================""")
        print(language_module.status7)

        f.close
        print(language_module.save2)
        exit(99)
              


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
            session.headers["User-Agent"] = config["Personalizations"]["useragent"]

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
