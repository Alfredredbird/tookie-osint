import logging
import os
import platform
import subprocess
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.remote_connection import LOGGER


def get_default_browser_windows():
    try:
        browser_key = r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"
        with os.popen(
            f'reg query "HKEY_CURRENT_USER\\{browser_key}" /v ProgId'
        ) as reg_query:
            output = reg_query.read()
        browser_name = output.split()[-1].strip()
        return browser_name
    except Exception:
        return None


def get_default_browser_mac():
    try:
        command = "osascript -e 'get id of app id \"com.apple.Safari\"'"
        output = subprocess.check_output(command, shell=True, text=True)
        if "Safari" in output:
            return "Safari"
        else:
            return "Unknown"
    except Exception:
        return None


def get_default_browser_linux():
    try:
        # Check the BROWSER environment variable
        browser = os.getenv("BROWSER")
        if browser:
            return browser
        # Try using xdg-settings
        xdg_browser_command = "xdg-settings get default-web-browser"
        browser = os.popen(xdg_browser_command).read().strip()
        if browser:
            return browser
        return "Unknown"
    except Exception:
        return None


def get_default_browser():
    os_name = platform.system()
    if os_name == "Windows":
        return get_default_browser_windows()
    elif os_name == "Darwin":  # macOS
        return get_default_browser_mac()
    elif os_name == "Linux":
        return get_default_browser_linux()
    else:
        return "Unknown"


# web scraper
def scrape(url, target_error_message, selected_webdriver, language_module):
    try:
        # Set the log level to suppress webdriver console output
        LOGGER.setLevel(logging.ERROR)

        if selected_webdriver == "Chrome":
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.headless = True
            chrome_options.add_argument(
                "--log-level=3"
            )  # Set the log level to suppress logging
            driver = webdriver.Chrome(options=chrome_options)
        elif selected_webdriver == "Firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.headless = True
            firefox_options.add_argument(
                "--log-level=3"
            )  # Set the log level to suppress logging
            driver = webdriver.Firefox(options=firefox_options)
        elif selected_webdriver == "Edge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument("--headless")
            edge_options.headless = True
            edge_options.add_argument(
                "--log-level=3"
            )  # Set the log level to suppress logging
            driver = webdriver.Edge(options=edge_options)
        else:
            print(language_module.error10)
            return None

        driver.get(url)
        driver.implicitly_wait(10)
        elements = driver.find_elements(
            By.XPATH, f'//*[contains(text(), "{target_error_message}")]'
        )
        if elements:
            there = "Yes"
            # line 133 is for dev testing
            # print(f"Found the error message: '{target_error_message} {url}'")
            return there
        else:  # f"Error message '{target_error_message}' not found on the page."
            there = "No"
            # line 138 is for dev testing
            # print(f"Error message '{target_error_message}' not found on the page. '{url}'")
            return there
    except Exception as e:
        print(f"{language_module.error11}{e}")
        return None
