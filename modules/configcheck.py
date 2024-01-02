import configparser
import os
import random
import shutil
import time

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


def colorSchemeGrabber(config):
    print("Grabbing Color Configuration")
    try:
        config.read("config/config.ini")
        color = config.get("Personalizations", "colorScheme").upper()
        color_code = getattr(Fore, color)
        return color_code
    except:
        print("Could not read configuration file")
        return "RED"


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


def configUpdateStuff(colorScheme, config, browser, language_module, argument):
    config.read("./config/config.ini")
    # this is just something Alfred can use to return something when it needs to return nothing
    holder = 0

    # checks to see if the user is running a Pre or if its Alfreds first launch.
    if config.get("main", "firstlaunch") == "yes":
        print(
            colorScheme + language_module.note + Fore.RESET + language_module.warning3
        )
        print("")
    if config.get("main", "prerelease") == "yes":
        print(
            colorScheme + language_module.note + Fore.RESET + language_module.warning4
        )
        print(language_module.prompt2)
        print("")
    # this is the function to update the code
    x = random.randint(1, 4)
    if x == 3 and config.get("main", "checkforupdates") == "yes":
        print(language_module.prompt3)
    if x == 2:
        print(language_module.prompt4)
    # desides if arguments are being used. if so, it wont ask to update.
    if any(vars(argument).values()):
        holder = 1
    else:
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
    if any(vars(argument).values()):
        holder = 1
    else:
        # asks the user if they want to enable updates
        if config.get("main", "checkforupdates") == "no":
            if getNum == 7:
                changeconfig = input(
                    "Updates Are Disabed. Wanna Renable Them? [y/n]: ⤷ "
                )
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

    if (
        getNum == 3
        or getNum == 5
        and config.get("Personalizations", "showtips") == "yes"
    ):
        # this gets the random tip to display on the screen
        randomTip = random.choice(open("./config/tips.txt").readlines())
        print(randomTip)


def syskeys(config):
    print("Here are your system keys.")
    print(str(config.get("main", "privatekey")))
    print(str(config.get("main", "syscrypt")))


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


# this is the module that edits the configuration file. needs to be cleaned up tho
VALID_CHOICES = {
    "checkforupdates": ["yes", "no"],
    "showtips": ["yes", "no"],
    "browser": ["Firefox", "Edge", "Chrome"],
    "defaultdlpath": [],
    "language": ["en", "ar", "de", "es", "fr", "hi", "il", "it", "ru"],
    "colorscheme": ["RED", "GREEN", "BLUE", "WHITE", "YELLOW", "BLACK"],
}


def display_options(config, section, language_module):
    print("Options:")
    print("=====================================================")
    print(f"{language_module.configOption1} {config.get('main', 'checkforupdates')}")
    print(
        f"{language_module.configOption2} {config.get('Personalizations', 'showtips')}"
    )
    print(f"{language_module.configOption3} {config.get('main', 'defaultdlpath')}")
    print(f"{language_module.configOption4} {config.get('main', 'browser')}")
    print(f"{language_module.configOption5} {config.get('main', 'language')}")
    print(
        f"{language_module.configOption6} {config.get('Personalizations', 'colorscheme')}"
    )
    print("=====================================================")
    print(f"{language_module.configOptionA} ")
    print(f"{language_module.configOptionB} ")
    print("=====================================================")


def update_config(config, section, option_key, new_value):
    config.set(section, option_key, str(new_value))
    with open("./config/config.ini", "w") as f:
        config.write(f)


def config_editor(config, language_module):
    selected_option_key = {
        "1": ("main", "checkforupdates"),
        "2": ("main", "showtips"),
        "3": ("main", "defaultdlpath"),
        "4": ("main", "browser"),
        "5": ("main", "language"),
        "6": ("Personalizations", "colorscheme"),
        "A": ("main", "option_A"),
        "B": ("main", "option_B"),
        "a": ("main", "option_A"),
        "b": ("main", "option_B"),
    }
    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    edit_config_answer = input(language_module.config5)

    if edit_config_answer.lower() == "y":
        display_options(
            config, "main", language_module
        )  # Use 'main' as default section

        edit_config_index = input(language_module.config6)
        selected_option = selected_option_key.get(edit_config_index)

        if selected_option:
            section, option_key = selected_option
            if option_key == "custom_config":
                custom_section = input("Enter the custom configuration section: ")
                custom_config_key = input("Enter the custom configuration key: ")
                value = config.get(custom_section, custom_config_key)
                print(
                    f"Custom Configuration: {custom_section}.{custom_config_key}: {value}"
                )
            elif option_key == "option_A":
                handle_option_A(config)
            elif option_key == "option_B":
                handle_option_B(config)
            else:
                valid_choices = (
                    VALID_CHOICES[option_key] if option_key in VALID_CHOICES else None
                )
                if not valid_choices:
                    new_value = input(f"{option_key.capitalize()}: ⤷ ")
                    update_config(config, section, option_key, new_value)
                else:
                    new_value = input(
                        f"{option_key.capitalize()} ({'/'.join(valid_choices)}): ⤷ "
                    )
                    if new_value in valid_choices:
                        update_config(config, section, option_key, new_value)
                    else:
                        print(
                            f"Invalid choice. Please choose from {', '.join(valid_choices)}"
                        )
        else:
            print("Invalid option selected.")
        return True

    elif edit_config_answer.lower() == "n":
        print("Aww ok")


# Your function for option A
def handle_option_A(config):
    dirDump(str(config.get("main", "defaultdlpath")))
    delete_pycache("./")


# Your function for option B
def handle_option_B(config):
    syskeys(config)
