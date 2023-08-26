import os
import shutil
import base64
import requests
import glob
import time


# variables
version = ""
alfred_version = ""
alfred_update_path = (
    "https://raw.githubusercontent.com/Alfredredbird/alfred/main/version.txt"
)
alfred_install_path = "/alfred/"
gitfile_loc = "https://raw.githubusercontent.com/Alfredredbird/alfred/main/"
udfl = []
dlfl = ""
fl = []
fh = []
# READS ALFRED VERSION
with open("version.txt", "r") as fp:
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
    with open("udfl") as file:
        udfl = [line.rstrip() for line in file]

    print(udfl)
    # delets the files listed in udfl
    for item in udfl:
        if "/update.py" not in udfl:
            os.remove(alfred_install_path + item)
        if "/update.py" in udfl:
            udfl.remove("/update.py")

    # waits then downloads a new file manager copy
    try:
        time.sleep(3)
        rc = requests.get(gitfile_loc + "udfl")
        open(alfred_install_path + "udfl", "wb").write(rc.content)

        print(udfl)
    except ConnectionError:
        print("Failed To Fecth Update Files. (-2)")

    try:
        # reads the udfl file
        with open("udfl") as file:
            fl = [line.rstrip() for line in file]
        time.sleep(2)
        print("Downloading Files")

        # downloads the files from udfl
        for item in fl:
            url = gitfile_loc + item
            r = requests.get(url, allow_redirects=True)
            print(item)
            open(alfred_install_path + item, "wb").write(r.content)
            fl.remove(item)
        with open("udfl") as file:
            fh = [line.rstrip() for line in file]
        # checks to see if the file exists, if not it reinstalls it
        while True:
            for item in fh:
                print("Working...")

                if os.path.exists(alfred_install_path + item) == True:
                    fh.remove(item)

                else:
                    url = gitfile_loc + item
                    r = requests.get(url, allow_redirects=True)

                    open(alfred_install_path + item, "wb").write(r.content)
            if len(fh) == 0:
                print("Update Done!")
                exec(open("brib.py").read())

    except ConnectionError:
        print("Failed To Download Update Files. (-3)")
else:
    print("Your On The Latest Version!")
