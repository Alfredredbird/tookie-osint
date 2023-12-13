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

    print(udfl)
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
    try:
        time.sleep(3)
        rc = requests.get(gitfile_loc + "/config/udfl")
        open("./config/udfl", "wb").write(rc.content)

        print(udfl)
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
            print(gitfile_loc + item)
            url = gitfile_loc + item
            r = requests.get(url, allow_redirects=True)
            print(item)
            # Added an exception handler for FileNotFoundError
            try:
                open(item, "wb").write(r.content)
                fl.remove(item)
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
                print("Working...")

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
