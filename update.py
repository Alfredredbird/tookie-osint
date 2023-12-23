import os
import time

import requests

# variables
version = ""
alfred_version = ""
alfred_update_path = (
    "https://raw.githubusercontent.com/Alfredredbird/alfred/main/config/version.cfg"
)
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
        third_length = (len(lines) + 2) // 3  # Calculate the approximate third

        max_length_left = max(len(line.strip()) for line in lines[:third_length])
        max_length_middle = max(
            len(line.strip()) for line in lines[third_length : 2 * third_length]
        )
        max_length_right = max(len(line.strip()) for line in lines[2 * third_length :])

        print(
            f"+{'-' * (max_length_left + 2)}+{'-' * (max_length_middle + 2)}+{'-' * (max_length_right + 2)}+"
        )
        for left, middle, right in zip(
            lines[:third_length],
            lines[third_length : 2 * third_length],
            lines[2 * third_length :],
        ):
            left = left.strip().ljust(max_length_left)
            middle = middle.strip().ljust(max_length_middle)
            right = right.strip().ljust(max_length_right)
            print(f"| {left} | {middle} | {right} |")
        print(
            f"+{'-' * (max_length_left + 2)}+{'-' * (max_length_middle + 2)}+{'-' * (max_length_right + 2)}+"
        )


def progress_bar_manual(dlcount, total_items, length, fill="#", print_end="\r"):
    def update_progress(progress, prefix="", suffix=""):
        bar_length = length
        filled_length = int(bar_length * progress / 100)
        bar = fill * filled_length + "-" * (bar_length - filled_length)

        print(f"\r{prefix} [{bar}] {progress:.2f}% {suffix}", end=print_end, flush=True)

    for i in range(total_items):
        # Update the progress bar manually
        progress = (dlcount + 1) / total_items * 100
        update_progress(progress, prefix="Progress:", suffix="Complete")

        # code to run progress bar
        # dlcount += 1
        # total_items = len(udfl)
        # progress_bar_manual(dlcount,total_items, length=20, fill='█', print_end='\r')


def update(alfred_update_path):
    # READS ALFRED VERSION
    with open("./config/version.cfg", "r") as fp:
        version = fp.read()
        fp.close()

    # gets the version number
    try:
        alfred_version = requests.get(alfred_update_path)
        alfred_version = alfred_version.text
        print(alfred_version)
    except ConnectionError:
        print("Failed To Fecth Updates. (-1)")

    # checks for updates
    if alfred_version != version:
        print("Fecthing Updates!")
        with open("./config/udfl") as file:
            udfl = [line.rstrip() for line in file]

        chart()
        # delets the files listed in udfl
        for item in udfl:
            try:
                if "/update.py" not in udfl:
                    os.remove(item)
            except FileExistsError:
                print("skipping: " + item)
            except FileNotFoundError:
                print("skipping: " + item)

        # waits then downloads a new file manager copy
        dlcount = 0
        try:
            time.sleep(3)
            rc = requests.get(gitfile_loc + "/config/udfl")
            open("./config/udfl", "wb").write(rc.content)

        except ConnectionError:
            print("Failed To Fecth Update Files. (-2)")

        try:
            # reads the udfl file
            with open("./config/udfl") as file:
                fl = [line.rstrip() for line in file]
            time.sleep(2)
            print("Downloading Files")

            # downloads the files from udfl
            for item in fl:
                # print(gitfile_loc + item)
                url = gitfile_loc + item
                r = requests.get(url, allow_redirects=True)

                # Added an exception handler for FileNotFoundError
                try:
                    open(item, "wb").write(r.content)
                    fl.remove(item)
                    # progress counter stuff
                    dlcount += 1.90001
                    total_items = len(udfl)
                    progress_bar_manual(
                        dlcount, total_items, length=40, fill="#", print_end="\r"
                    )
                except FileNotFoundError:
                    print("Cant Find: " + item + "Skiping!")
                # Added an exception handler for OSError
                except OSError:
                    print("Permission Error")
            with open("./config/udfl") as file:
                fh = [line.rstrip() for line in file]
            # checks to see if the file exists, if not it reinstalls it
            while True:
                for item in fh:
                    if os.path.exists(item) == True:
                        fh.remove(item)

                    elif not os.path.exists(item):
                        url = gitfile_loc + item
                        r = requests.get(url, allow_redirects=True)

                        open(item, "wb").write(r.content)

                if len(fh) == 0:
                    print("Update Done!")

                    exec(open("brib.py").read())

        except ConnectionError:
            print("Failed To Download Update Files. (-3)")
    else:
        print("Your On The Latest Version!")


def reinstall(chart, gitfile_loc, progress_bar_manual):
    # checks for updates

    print("Reinstalling.....!")
    with open("./config/udfl") as file:
        udfl = [line.rstrip() for line in file]

    chart()
    # delets the files listed in udfl
    for item in udfl:
        try:
            if "/update.py" not in udfl:
                os.remove(item)
        except FileExistsError:
            print("skipping: " + item)
        except FileNotFoundError:
            print("skipping: " + item)

    # waits then downloads a new file manager copy
    dlcount = 0
    try:
        time.sleep(3)
        rc = requests.get(gitfile_loc + "/config/udfl")
        open("./config/udfl", "wb").write(rc.content)

    except ConnectionError:
        print("Failed To Fecth Update Files. (-2)")

    try:
        # reads the udfl file
        with open("./config/udfl") as file:
            fl = [line.rstrip() for line in file]
        time.sleep(2)
        print("Downloading Files")

        # downloads the files from udfl
        for item in fl:
            url = gitfile_loc + item
            r = requests.get(url, allow_redirects=True)
            # Added an exception handler for FileNotFoundError
            try:
                open(item, "wb").write(r.content)
                fl.remove(item)
                # progress counter stuff
                dlcount += 1.90001
                total_items = len(udfl)
                progress_bar_manual(
                    dlcount, total_items, length=40, fill="#", print_end="\r"
                )
            except FileNotFoundError:
                print("Cant Find: " + item + "Skiping!")
            # Added an exception handler for OSError
            except OSError:
                print("Permission Error")
        with open("./config/udfl") as file:
            fh = [line.rstrip() for line in file]
        # checks to see if the file exists, if not it reinstalls it
        print("")
        print("Processing...")
        while True:
            for item in fh:
                if os.path.exists(item) == True:
                    fh.remove(item)

                elif not os.path.exists(item):
                    url = gitfile_loc + item
                    r = requests.get(url, allow_redirects=True)

                    open(item, "wb").write(r.content)
            if len(fh) == 0:
                print("Update Done!")
                time.sleep(1)
                exit(0)

    except ConnectionError:
        print("Failed To Download Update Files. (-3)")


choice = input("update or reinstall? [U/r]")
if "U" in choice or "u" in choice:
    update(alfred_update_path)
elif "r" in choice or "R" in choice:
    reinstall(chart, gitfile_loc, progress_bar_manual)
else:
    print("Not Sure What You Ment...........Ill Ask Later")
