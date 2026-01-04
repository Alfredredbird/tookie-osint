import time
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


driver = None

def get_driver():
    global driver
    if driver is None:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service("/usr/bin/chromedriver")

        driver = webdriver.Chrome(
            service=service,
            options=options
        )
    return driver


def check_site(url, message, allsites=False, delay=2):
    driver = get_driver()
    try:
     driver.get(url)
    except WebDriverException as e:
        msg = str(e)

        if "ERR_NAME_NOT_RESOLVED" in msg:
            print(f"[DNS ERROR] Could not resolve: {url}")
            return False
        print(f"[SELENIUM ERROR] {url} -> {e}")
        return False

    time.sleep(delay)

    if message.lower() in driver.page_source.lower():
        if allsites:
         print(f"[{Fore.RED}-{Fore.RESET}] {url}")
         return False
        pass
    else:
        print(f"[{Fore.GREEN}+{Fore.RESET}] {url}")
        return True

def close_driver():
    global driver
    if driver is not None:
        driver.quit()
        driver = None