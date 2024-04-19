import os
import time
import requests


# Global variables
config_version_path = "./config/version.cfg"
config_udfl_path = "./config/udfl"
tookie_osint_update_path = (
    "https://raw.githubusercontent.com/alfredredbird/tookie-osint/main/config/version.cfg"
)
tookie_osint_install_path = "/tookie-osint/"
gitfile_location = "https://raw.githubusercontent.com/alfredredbird/tookie-osint/main/"
dl_count = 0


class Updater:
    def __init__(self):
        self.version = self.read_file(config_version_path)
        self.udfl_list = self.read_file_lines(config_udfl_path)

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read().strip()

    def read_file_lines(self, file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file]

    def save_file_from_url(self, url, destination):
        try:
            response = requests.get(url, allow_redirects=True)
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            with open(destination, "wb") as file:
                file.write(response.content)
            return True
        except Exception as e:
            print(f"Error saving file from {url}: {e}")
            return False

    def update(self):
        try:
            remote_version = requests.get(tookie_osint_update_path).text.strip()
        except requests.ConnectionError:
            print("Failed to fetch updates. (-1)")
            return
        if remote_version != self.version:
            self.process_update(remote_version)
        else:
            print("You're on the latest version!")

    def process_update(self, remote_version):
        print("Fetching Updates!")
        self.delete_files()
        self.save_file_from_url(gitfile_location + "config/udfl", config_udfl_path)
        udfl = self.read_file_lines(config_udfl_path)
        self.download_files(udfl)
        self.verify_and_exec(udfl)

    def delete_files(self):
        if self.udfl_list is not None and isinstance(self.udfl_list, list):
            for file_path in self.udfl_list:
                if "update.py" not in file_path:
                    try:
                        os.remove(file_path)
                    except FileNotFoundError:
                        print(f"Skipping: {file_path}")

    def download_files(self, file_list):
        global dl_count
        print("Downloading Files")
        for file_path in file_list:
            url = gitfile_location + file_path
            if self.save_file_from_url(url, file_path):
                dl_count += 1
                self.progress_bar_manual(dl_count, len(file_list))

    def verify_and_exec(self, file_list):
        missing_files = [f for f in file_list if not os.path.exists(f)]
        for file_path in missing_files:
            self.save_file_from_url(gitfile_location + file_path, file_path)
        if not missing_files:
            print("Update Done!")
            exec(open("brib.py").read())

    def progress_bar_manual(self, current, total, length=40, fill="#"):
        percent = (current / total) * 100
        filled_length = int(length * percent / 100)
        bar = fill * filled_length + "-" * (length - filled_length)
        print(f"\rProgress: [{bar}] {percent:.2f}% Complete", end="\r", flush=True)

    def reinstall(self):
        print("Reinstalling.....!")
        self.delete_files()
        self.save_file_from_url(gitfile_location + "config/udfl", config_udfl_path)
        self.download_files(self.udfl_list)
        self.verify_and_exec(self.udfl_list)


# Usage of the class
choice = input("Update or reinstall? [U/r]: ").lower()
updater = Updater()
if choice == "u":
    updater.update()
elif choice == "r":
    updater.reinstall()
else:
    print("Not sure what you meant... I'll ask later")
