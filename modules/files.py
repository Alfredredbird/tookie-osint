import os
import requests
import platform
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def make_restore(sites, username):
    # An empty scan has no site to resume from. Indexing it used to print
    # "list index out of range" after every run that found nothing.
    if not sites:
        return
    try:
        site = sites[-1]
        # Get the URL
        url = site["url"]
        # Parse the URL
        parsed = urlparse(url)
        # remove the username from the path
        path = parsed.path.rstrip("/")

        if path.endswith("/" + username):
            path = path[:-(len(username) + 1)]

        # Rebuild the URL
        base_url = parsed._replace(path=path).geturl()

        with open(".tookie", "w") as f:
            f.write(
                "=====Tookie-OSINT Restore File=====\n"
                f"URL = {base_url}\n"
                f"FOUND = {site['found']}\n"
                f"STATUS = {site['status']}\n"
            )
        print(f"[+] Restore file created: {base_url}")
    except Exception as e:
        print(e)


def use_restore_answer(answer):
    # The prompt is [Y/n], so pressing Enter accepts the file. "yes" used to
    # be treated as a no because only the single letter y was recognized.
    return str(answer).strip().lower() in ("", "y", "yes")


def load_restore():
    try:
        with open(".tookie", "r") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("URL = "):
                url = line.strip().split(" = ", 1)[1]
                print("==============================================")
                print(f"Found restore file!")
                print("==============================================")
                if use_restore_answer(input("Use Restore File? [Y/n] ")):
                    return url

                return None

    except FileNotFoundError:
        # First run, or the previous scan found nothing. That is not an error.
        return None
    except Exception as e:
        print(e)

    return None

def send_webhook(webhook_url, username, message, type="info"):
    if type == "info":
        payload = {
            "username": "Tookie-OSINT Webhook",
            "embeds": [{
                "title": "Tookie-OSINT Webhook",
                "description": f"{message}",
                "color": 65280,
                "fields": [
                    {"name": "Status", "value": "Online", "inline": True},
                    {"name": "Server", "value": f"{platform.node()}", "inline": True}
                ]
            }]
        }
    elif type == "site":
        payload = {
            "username": "Tookie-OSINT Webhook",
            "embeds": [{
                "title": "Tookie-OSINT Webhook",
                "description": f"{message}",
                "color": 65280,
                "fields": [
                    {"name": "Status", "value": "Online", "inline": True},
                    {"name": "Server", "value": f"{platform.node()}", "inline": True}
                ]
            }]
        }
    elif type == "error":
        payload = {
            "username": "Tookie-OSINT Webhook",
            "embeds": [{
                "title": "Tookie-OSINT Webhook",
                "description": f"{message}",
                "color": 16711680,
                "fields": [
                    {"name": "Status", "value": "Error", "inline": True},
                    {"name": "Server", "value": f"{platform.node()}", "inline": True}
                ]
            }]
        }
    else:
        # An unknown type used to fall through with payload unset and raise
        # UnboundLocalError in the middle of a scan.
        print(f"[!] Unknown webhook type: {type}")
        return False

    # A refused connection or a timeout used to raise out of the result loop,
    # so write_to_file() never ran and the report was lost.
    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Webhook notification failed: {e}")
        return False
    return True
