import os
import requests

class Updater:
    def __init__(self):
        # Global variables
        self.config_version_path = "./config/version.cfg"
        self.config_udfl_path = "./config/udfl"
        self.alfred_update_path = "https://raw.githubusercontent.com/EliteGreyIT67/alfred/main/config/version.cfg"
        self.gitfile_location = "https://raw.githubusercontent.com/EliteGreyIT67/alfred/main/"
        self.version = self.read_file(self.config_version_path)
        self.udfl_list = self.read_file_lines(self.config_udfl_path)

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read().strip()

    def read_file_lines(self, file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file]

    def delete_files(self):
        for file_path in self.udfl_list:
            try:
                if "update.py" not in file_path:
                    os.remove(file_path)
            except FileNotFoundError:
                pass # Ignore files that are not found

    def download_files(self, file_list):
        print("Downloading Files")
        for file_path in file_list:
            try:
                response = requests.get(self.gitfile_location + file_path, allow_redirects=True)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "wb") as file:
                    file.write(response.content)
            except Exception as e:
                print(f"Error saving file from {file_path}: {e}")

    def update(self):
        print("Checking for updates...")
        try:
            remote_version = requests.get(self.alfred_update_path).text.strip()
            if remote_version != self.version:
                print("Update available!")
                self.delete_files()
                self.download_files(self.udfl_list)
                with open(self.config_version_path, "w") as file:
                    file.write(remote_version) # update the version file
                print("Update Done! Restarting...")
                os.execv(__file__, []) # Restart the script
            else:
                print("You're on the latest version!")
        except requests.ConnectionError:
            print("Unable to check for update, please try again later.")

    def reinstall(self):
        print("Reinstalling...")
        self.delete_files()
        self.download_files(self.udfl_list)
        os.execv(__file__, []) # Restart the script

# Execution logic
if __name__ == "__main__":
    updater = Updater()
    choice = input("Update or reinstall? [U/r]: ").lower()
    if choice == "u":
        updater.update()
    elif choice == "r":
        updater.reinstall()
    else:
        print("Invalid choice. Exiting...")