import os
import requests
import platform
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def make_restore(sites, username):
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
                YN = input("Use Restore File? [Y/n] ")


                if YN.lower() == "y":
                    return url

                return None

    except Exception as e:
        print(e)

    return None

def send_webhook(webhook_url, username, message, type="info"):
    print("[+] Sending Webhook")
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
    
    response = requests.post(webhook_url, json=payload)
