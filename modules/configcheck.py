import os
import random
import shutil
import time
import shutil
import configparser 

import requests
from colorama import *

from lang.en import *
from modules.lang import *


# This Module does config stuff
#
def configC(language_module):
    # checks if the nesasary files exist
    if os.path.exists("./config/config.ini") == True:
        print(language_module.config1)
    else:
        print(language_module.error5)
        time.sleep(4)
        with open("./config/version.cfg", "w") as f:
            f.write(language_module.status3)
        exec(open("./update.py").read())

    if os.path.exists("./update.py") == True:
        print(language_module.config2)
    else:
        print(language_module.error5)
        exit(1)

    # opens the config and gets the version number
    with open("./config/version.cfg", "r") as fp:
        version = fp.read()
        return version



def delete_pycache(root_dir):
    """
    Recursively searches for and deletes __pycache__ folders within the specified directory.

    Parameters:
    - root_dir (str): The root directory to start searching for __pycache__ folders.
    """
    for foldername, subfolders, filenames in os.walk(root_dir):
        # Check if __pycache__ folder exists in the current directory
        if "__pycache__" in subfolders:
            pycache_path = os.path.join(foldername, "__pycache__")
            print(f"Deleting __pycache__ folder: {pycache_path}")
            # Delete the __pycache__ folder
            shutil.rmtree(pycache_path)


def configUpdateStuff(config, browser, language_module):
    config.read("./config/config.ini")

    # checks to see if the user is running a Pre or if its Alfreds first launch.
    if config.get("main", "firstlaunch") == "yes":
        print(Fore.RED + language_module.note + Fore.RESET + language_module.warning3)
        print("")
    if config.get("main", "prerelease") == "yes":
        print(Fore.RED + language_module.note + Fore.RESET + language_module.warning4)
        print(language_module.prompt2)
        print("")
    # this is the function to update the code
    x = random.randint(1, 4)
    if x == 3 and config.get("main", "checkforupdates") == "yes":
        print(language_module.prompt3)
    if x == 2:
        print(language_module.prompt4)

    if config.get("main", "checkforupdates") == "yes":
        try:
            cfu = input(language_module.config4)
            if "Y" in cfu or "y" in cfu:
                exec(open("./update.py").read())
            elif "N" in cfu or "n" in cfu:
                print(language_module.prompt5)
                print(
                    Fore.RESET
                    + """
===========================================================================
                  """
                )
            else:
                print(language_module.idk2)
                print(
                    Fore.RESET
                    + """
===========================================================================
                  """
                )
        except KeyboardInterrupt:
            config.set("main", "firstlaunch", "no")
            if browser == "MSEdgeHTM":
                browser = "Edge"
            config.set("main", "browser", browser)
            with open("./config/config.ini", "w") as f:
                config.write(f)
            exit(1)

    getNum = random.randint(1, 10)
    # asks the user if they want to enable updates
    if config.get("main", "checkforupdates") == "no":
        if getNum == 7:
            changeconfig = input("Updates Are Disabed. Wanna Renable Them? [y/n]: ⤷ ")
            # pharses it
            if "Y" in changeconfig or "y" in changeconfig:
                config.set("main", "checkforupdates", "yes")
                print(language_module.updates)
                with open("./config/config.ini", "w") as f:
                    config.write(f)
            elif "N" in changeconfig or "n" in changeconfig:
                print(language_module.prompt5)
            else:
                print(language_module.idk2)

    if config.get("main", "firstlaunch") == "yes":
        config.set("main", "firstlaunch", "no")
        if browser == "MSEdgeHTM":
            browser = "Edge"
        config.set("main", "browser", browser)
        with open("./config/config.ini", "w") as f:
            config.write(f)

    if getNum == 3 and config.get("main", "showtips") == "yes":
        # this gets the random tip to display on the screen
        randomTip = random.choice(open("./config/tips.txt").readlines())
        print(randomTip)

def syskeys(config):
    print("Here are your system keys.")
    print(str(config.get("main", "privatekey")))
    print(str(config.get("main", "syscrypt")))
    

# this is the module that edits the configuration file. needs to be cleaned up tho
VALID_CHOICES = {
    "checkforupdates": ["yes", "no"],
    "showtips": ["yes", "no"],
    "browser": ["Firefox", "Edge", "Chrome"],
    "defaultdlpath": [],
    "language": ["en", "ar", "de", "es", "fr", "hi", "il", "it", "ru"],
}

def display_options(config, language_module):
    print("Options:")
    print("=====================================")
    print(f"{language_module.configOption1} {config.get('main', 'checkforupdates')}")
    print(f"{language_module.configOption2} {config.get('main', 'showtips')}")
    print(f"{language_module.configOption3} {config.get('main', 'defaultdlpath')}")
    print(f"{language_module.configOption4} {config.get('main', 'browser')}")
    print(f"{language_module.configOption5} {config.get('main', 'language')}")
    print(f"{language_module.configOptionA} ")
    print(f"{language_module.configOptionB} ")
    print("=====================================")

def update_config(config, option_key, new_value):
    config.set("main", option_key, str(new_value))
    with open("./config/config.ini", "w") as f:
        config.write(f)

def config_editor(config, language_module):
    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    edit_config_answer = input(language_module.config5)

    if edit_config_answer.lower() == "y":
        display_options(config, language_module)

        edit_config_index = input(language_module.config6)
        selected_option_key = {
            "1": "checkforupdates",
            "2": "showtips",
            "3": "defaultdlpath",
            "4": "browser",
            "5": "language",
            "A": "option_A",
            "B": "option_B",
            "a": "option_A",
            "b": "option_B",
        }.get(edit_config_index)

        if selected_option_key in VALID_CHOICES:
            valid_choices = VALID_CHOICES[selected_option_key]
            if not valid_choices:  # Allow any input for "defaultdlpath"
                new_value = input(f"{selected_option_key.capitalize()}: ⤷ ")
                update_config(config, selected_option_key, new_value)
            else:
                new_value = input(f"{selected_option_key.capitalize()} ({'/'.join(valid_choices)}): ⤷ ")
                if new_value.lower() in valid_choices:
                    update_config(config, selected_option_key, new_value.lower())
                else:
                    print(f"Invalid choice. Please choose from {', '.join(valid_choices)}")
        elif selected_option_key == "option_A":
            dirDump(str(config.get("main", "defaultdlpath")))
            delete_pycache("./")
        elif selected_option_key == "option_B":
            syskeys(config)
        else:
            print("Invalid option selected.")
        return True

    elif edit_config_answer.lower() == "n":
        print("Aww ok")


def globalPath(config):

    config.read("./config/config.ini")
    path = config.get("main", "defaultDlPath")
    return path


def dirDump(mydir):
    filelist = [f for f in os.listdir(mydir)]
    for f in filelist:
        os.remove(os.path.join(mydir, f))


def create_folders(folder_list, language_module):
    for folder in folder_list:
        if not os.path.exists(folder):
            print(f"{language_module.config7}{folder}")
            os.makedirs(folder)
        else:
            print(f"{language_module.config8}{folder}")
