import os

SITE = "http://blahblahblah.com"



def make_restore(sites):
    try:
        site = sites[-1]

        with open(".tookie", "w") as f:
            f.write(
                "=====Tookie-OSINT Restore File=====\n"
                f"URL = {site['url']}\n"
                f"FOUND = {site['found']}\n"
                f"STATUS = {site['status']}\n"
            )

    except Exception as e:
        print(e)

def load_restore():
    try:
        with open(".tookie", "r") as f:
            lines = f.readlines()

        restore = {}

        for line in lines[1:]:
            key, value = line.strip().split(" = ", 1)
            restore[key.lower()] = value

        print(restore)
        YN = input("Use Restore File? [Y/n]")
        if YN.lower == "y":
            print("Y")
        else:
            pass
            

    except Exception as e:
        print(e)

