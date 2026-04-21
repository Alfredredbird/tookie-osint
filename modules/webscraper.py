import time
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3.exceptions import ReadTimeoutError
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = None

def get_driver():
    global driver
    if driver is None:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")            
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-port=0")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(

            options=options
        )

        driver.set_page_load_timeout(15)
    return driver



def extract_fields(driver, site_config):
    results = {}

    for field_name, config in site_config.items():
        try:
            if config["by"] == "css":
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, config["selector"])
                    )
                )
            elif config["by"] == "xpath":
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, config["selector"])
                    )
                )
            else:
                continue
            attr = config.get("attr")
            results[field_name] = element.get_attribute(attr) if attr else element.text.strip()

            results[field_name] = element.text.strip()
        except TimeoutException:
            print(f"[!] Field '{field_name}' not found on page (timeout)")
            results[field_name] = None
        except Exception as e:
            print(f"[DEBUG] Failed to extract {field_name}: {e}")
            results[field_name] = None

    return results

def check_site(url, message, field_config=None, allsites=False, delay=2):
    driver = get_driver()

    try:
        driver.get(url)
    except TimeoutException:
        print(f"[TIMEOUT] {url}")
        return False
    except ReadTimeoutError:
        print(f"[DRIVER TIMEOUT] ChromeDriver hung on: {url}")
        return False
    except WebDriverException as e:
        msg = str(e)

        if "ERR_NAME_NOT_RESOLVED" in msg:
            print(f"[DNS ERROR] Could not resolve: {url}")
        elif "ERR_CONNECTION_REFUSED" in msg:
            print(f"[SELENIUM ERROR] Connection Refused: {url}")
        return False

    time.sleep(delay)

    found = message.lower() not in driver.page_source.lower()

    if found:
        print(f"[{Fore.GREEN}+{Fore.RESET}] {url}")
    elif allsites:
        print(f"[{Fore.RED}-{Fore.RESET}] {url}")

    if found and field_config:
        extracted = extract_fields(driver, field_config)

        print(f"    {Fore.CYAN}Scraped Data:{Fore.RESET}")
        for key, value in extracted.items():
            print(f"      {Fore.YELLOW}{key}:{Fore.RESET} {value}")

        return {
            "url": url,
            "found": True,
            "data": extracted
        }

    return found

def close_driver():
    global driver
    if driver is not None:
        driver.quit()
        driver = None