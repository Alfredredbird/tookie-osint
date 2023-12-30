import os
import time
import requests


# variables
version = ""
alfred_version = ""
alfred_update_path = "https://raw.githubusercontent.com/Alfredredbird/alfred/main/config/version.cfg"
alfred_install_path = "/alfred/"
gitfile_loc = "https://raw.githubusercontent.com/Alfredredbird/alfred/main/"
udfl = []
dlfl = ""
fl = []
fh = []
dlcount = 0

def chart():
    file_path = "config/udfl"

    with open(file_path, "r") as file:
        lines = file.readlines()
        third_length = (len(lines) + 2) // 3

        max_length_left = max(len(line.strip()) for line in lines[:third_length])
        max_length_middle = max(len(line.strip()) for line in lines[third_length:2 * third_length])
        max_length_right = max(len(line.strip()) for line in lines[2 * third_length:])

        print(f"+{'-' * (max_length_left + 2)}+{'-' * (max_length_middle + 2)}+{'-' * (max_length_right + 2)}+")
        for left, middle, right in zip(
            lines[:third_length],
            lines[third_length:2 * third_length],
            lines[2 * third_length:],
        ):
            left = left.strip().ljust(max_length_left)
            middle = middle.strip().ljust(max_length_middle)
            right = right.strip().ljust(max_length_right)
            print(f"| {left} | {middle} | {right} |")
        print(f"+{'-' * (max_length_left + 2)}+{'-' * (max_length_middle + 2)}+{'-' * (max_length_right + 2)}+")


def progress_bar_manual(dlcount, total_items, length=40, fill="#"):
    percent_complete = (dlcount / total_items) * 100
    bar_length = length
    filled_length = int(length * percent_complete / 100)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f"\rProgress: [{bar}] {percent_complete:.2f}% Complete", end='\r', flush=True)


def update(alfred_update_path):
    global udfl  # Ensure we use the global variable

    # READS ALFRED VERSION
    with open("./config/version.cfg", "r") as fp:
        version = fp.read()

    # gets the version number
    try:
        alfred_version = requests.get(alfred_update_path).text
        print(alfred_version)
    except requests.ConnectionError:
        print("Failed To Fetch Updates. (-1)")

    # checks for updates
    if alfred_version != version:
        print("Fetching Updates!")
        with open("./config/udfl") as file:
            udfl = [line.rstrip() for line in file]

        chart()

        # deletes the files listed in udfl
        for item in udfl:
            if "/update.py" not in item:
                try:
                    os.remove(item)
                except FileNotFoundError:
                    print("Skipping: " + item)

        # downloads a new file manager copy
        try:
            time.sleep(3)
            response = requests.get(gitfile_loc + "config/udfl")
            with open("./config/udfl", "wb") as file:
                file.write(response.content)
        except requests.ConnectionError:
            print("Failed To Fetch Update Files. (-2)")

        try:
            # reads the udfl file
            with open("./config/udfl") as file:
                fl = [line.rstrip() for line in file]
            time.sleep(2)
            print("Downloading Files")

            # downloads the files from udfl
            for item in fl:
                url = gitfile_loc + item
                try:
                    response = requests.get(url, allow_redirects=True)
                    with open(item, "wb") as file:
                        file.write(response.content)
                    fl.remove(item)
                    dlcount += 1.90001
                    progress_bar_manual(dlcount, len(udfl))
                except FileNotFoundError:
                    print("Can't Find: " + item + " Skipping!")
                except OSError:
                    print("Permission Error")

            # checks to see if the file exists, if not it reinstalls it
            with open("./config/udfl") as file:
                fh = [line.rstrip() for line in file]

            while True:
                for item in fh:
                    if not os.path.exists(item):
                        response = requests.get(gitfile_loc + item, allow_redirects=True)
                        with open(item, "wb") as file:
                            file.write(response.content)
                        fh.remove(item)
                if not fh:  # All files exist
                    print("Update Done!")
                    exec(open("brib.py").read())
                    break
        except requests.ConnectionError:
            print("Failed To Download Update Files. (-3)")
    else:
        print("You're On The Latest Version!")

def reinstall(gitfile_loc, progress_bar_func):
    print("Reinstalling.....!")

    # Read update file list (udfl) and display chart
    with open("./config/udfl") as file:
        udfl = [line.rstrip() for line in file]
    chart()

    # Delete the files listed in udfl
    for item in udfl:
        if "/update.py" not in item:
            try:
                os.remove(item)
            except FileNotFoundError:
                print(f"skipping: {item}")

    # Download a new file manager copy
    try:
        time.sleep(3)
        response = requests.get(gitfile_loc + "config/udfl")
        with open("./config/udfl", "wb") as file:
            file.write(response.content)
    except requests.ConnectionError:
        print("Failed To Fetch Update Files. (-2)")

    # Download the files
    try:
        with open("./config/udfl") as file:
            fl = [line.rstrip() for line in file]
        print("Downloading Files")
        total_items = len(udfl)

        for item in fl:
            url = gitfile_loc + item
            try:
                response = requests.get(url, allow_redirects=True)
                os.makedirs(os.path.dirname(item), exist_ok=True)
                with open(item, "wb") as file:
                    file.write(response.content)
                dlcount += 1
                progress_bar_func(
                    dlcount, total_items, length=40, fill="#"
                )
            except FileNotFoundError:
                print(f"Can't Find: {item} Skipping!")
            except OSError:
                print("Permission Error")

        # Verify all files exist, and re-download missing files if necessary
        with open("./config/udfl") as file:
            fh = [line.rstrip() for line in file]
        for item in fh:
            if not os.path.exists(item):
                response = requests.get(gitfile_loc + item, allow_redirects=True)
                with open(item, "wb") as file:
                    file.write(response.content)

        if all(os.path.exists(item) for item in fh):
            print("Reinstallation Complete!")
            time.sleep(1)
            exec(open("brib.py").read())

    except requests.ConnectionError:
        print("Failed To Download Update Files. (-3)")


choice = input("Update or reinstall? [U/r]: ").lower()
if choice == "u":
    update(alfred_update_path)
elif choice == "r":
    reinstall(gitfile_loc, progress_bar_manual)
else:
    print("Not sure what you meant... I'll ask later")
