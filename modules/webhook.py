import requests

def send_webhook_message(webhook_url, link, uname, username="Tookie-OSINT Bot", color=0x3498db):
    """
    Send a message to a Discord webhook with an embed.

    :param webhook_url: The URL of the Discord webhook
    :param link: The URL found during OSINT
    :param uname: The username found during OSINT
    :param avatar_url: The URL of the image to use as the bot's profile picture
    :param username: The username of the webhook sender (default: Tookie-OSINT Bot)
    :param color: The color of the embed (default: blue)
    """
    if not webhook_url.startswith('http://') and not webhook_url.startswith('https://'):
        raise ValueError("Invalid webhook URL. The URL must start with http:// or https://")

    title = "Tookie-OSINT Discovery"
    description = "***Some Information Might Be Inaccurate***"
    avatar_url = "https://private-user-images.githubusercontent.com/105014217/323384298-67bab5b4-f537-4f05-8a7b-c9fc3a16d256.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjA5ODk3ODMsIm5iZiI6MTcyMDk4OTQ4MywicGF0aCI6Ii8xMDUwMTQyMTcvMzIzMzg0Mjk4LTY3YmFiNWI0LWY1MzctNGYwNS04YTdiLWM5ZmMzYTE2ZDI1Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzE0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcxNFQyMDM4MDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zOWVkNGVmZjNmMDBmM2E5OWI3NjVjYTkyNjM2Njk4MTM2OWNlNjA3ZDM1NmE0MWJiYWFiZWQwMjI4ZTAzODg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.seCrh2vZi8OF38_kTcNt4Jiu4iy8uk5Z2uhng6Socnw"  
    data = {
        "username": username,
        "avatar_url": avatar_url,
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color,
                "fields": [
                    {
                        "name": "Target",
                        "value": link,
                        "inline": False
                    },
                    {
                        "name": "Found",
                        "value": uname,
                        "inline": False
                    }
                ]
            }
        ]
    }
    
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(webhook_url, json=data, headers=headers)
        response.raise_for_status()  # Raises an error for bad status codes
        if response.status_code != 204:
            print(f"Unexpected status code from webhook: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")
