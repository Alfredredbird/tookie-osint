import configparser
import importlib
import os
import random
import shutil
import time

import requests
from colorama import *
import urllib

from lang.en import *
from modules.lang import *
from modules.webscrape import *

#does stuff involving plugins
class PluginManager:
    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    pluginFolder = config.get("main", "pluginfolder")
    
    def __init__(self, plugins_directory=pluginFolder):
        self._plugins_directory = plugins_directory
        self._plugins = {}

    def load_plugins(self):
        for plugin_name in self._get_plugin_files():
            self._load_single_plugin(plugin_name)

    # Get a list of all files in the plugins directory
    def _get_plugin_files(self):
        return [
            f[:-3] for f in os.listdir(self._plugins_directory)
            if f.endswith('.py') and not f.startswith("__")
        ]

    def _load_single_plugin(self, plugin_name):
        try:
            module = importlib.import_module(f"{self._plugins_directory}.{plugin_name}")
            self._plugins[plugin_name] = module
            print(f"Plugin '{plugin_name}' loaded successfully.")
        except ImportError as e:
            print(f"Failed to load plugin '{plugin_name}': {e}")
            pass  # Handle or log errors as needed
            
    def run_plugins(self):
        for module in self._plugins.values():
            module.run()

def pluginMangager():
    
    plugin_manager = PluginManager()

    # Load plugins from the specified directory
    plugin_manager.load_plugins()

    # Run loaded plugins
    plugin_manager.run_plugins()

# This Module does config stuff
#
def configC(language_module):
    # checks if the nesasary files exist
    if os.path.exists("./config/config.ini"):
        
         print(language_module.config1)
    else:
        # If not found, alert the user and attempt to update
        print(language_module.error5)
        time.sleep(4)
        with open("./config/version.cfg", "w") as f:
            f.write(language_module.status3)
        exec(open("./update.py").read())
        
    # Check if update.py script exists
    if os.path.exists("./update.py"):
        
         print(language_module.config2)
    else:
        print(language_module.error5)
        exit(1)

    # opens the config and gets the version number
    with open("./config/version.cfg", "r") as fp:
        version = fp.read()
        return version

# Get the color scheme from the config file
def colorSchemeGrabber(config, argument):
    if argument.debug == True:
     print("Grabbing Color Configuration")
    try:
        config.read("config/config.ini")
        color = config.get("Personalizations", "colorScheme").upper()
        color_code = getattr(Fore, color)
        return color_code
    except configparser.Error as e:
        print(f"Could not read configuration file: {e}")
        return Fore.RED

# Delete __pycache__ directories
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

# Ask user about update checks
def ask_update_check(config, colorScheme, language_module):
    try:
        cfu = input(language_module.config4)
        if cfu.lower() in ("y", "yes"):
            with open("config/version.cfg", "r") as f:
                url = "https://raw.githubusercontent.com/Alfredredbird/tookie-osint/refs/heads/main/config/version.cfg"

                response = requests.get(url)
                if response.status_code == 200:
                    data = response.text.strip()  # Remove any extra whitespace or newline characters
                    currentver = f.readline().strip()  # Read the first line and strip it too
                    print("")
                    print(f"Current version: {currentver}")
                    print(f"Remote version: {data}")

                    if currentver != data:
                        print("Download new version at https://github.com/Alfredredbird/tookie-osint")
                        print("")
                    else:
                        print("Latest version installed!")
                        print("")
                else:
                    print(f"Failed to fetch new version data. Status code: {response.status_code}")
                    print("")
        elif cfu.lower() in ("n", "no"):
            print(language_module.prompt5)
            print_separator()
        else:
            print(language_module.idk2)
            print_separator()
    except KeyboardInterrupt:
        broswer = config.get("main", "browser")
        saveBrowser(config,str(broswer))
        exit(1)

# Prompt user at random to enable updates
def random_enable_updates(config, language_module):
    getNum = random.randint(1, 10)
    # asks the user if they want to enable updates
    if getNum == 7 and config.get("main", "checkforupdates") == "no":
        changeconfig = input("Updates Are Disabed. Wanna Renable Them? [y/n]: ⤷ ")
        # pharses it
        if changeconfig.lower() in ("y", "yes"):
            config.set("main", "checkforupdates", "yes")
            print(language_module.updates)
            save_config(config)
        elif changeconfig.lower() in ("n", "no"):
            print(language_module.prompt5)
        else:
            print(language_module.idk2)

# Process various config-related tasks
def configUpdateStuff(colorScheme, config, browser, language_module, argument):
    config.read("./config/config.ini")
    print_first_launch_messages(config, colorScheme, language_module)
    decide_random_events(config, colorScheme, language_module)
    

    # Handle arguments to prevent update prompts
    if any(vars(argument).values()):
        return

    if config.get("main", "checkforupdates") == "yes" and config.get("main", "firstlaunch") == "no":
        ask_update_check(config, colorScheme, language_module)

    random_enable_updates(config, language_module)
    display_random_tip(config, language_module)
    is_first_launch(config, browser, language_module)

# Display a random tip if enabled in config
def display_random_tip(config, language_module):
    if config.get("Personalizations", "showtips") == "yes":
        # this gets the random tip to display on the screen
        randomTip = random.choice(open("./config/tips.txt").readlines())
        print(randomTip)

# Check if this is the first application launch
def is_first_launch(config, browser, language_module):
    if config.get("main", "firstlaunch") == "yes":
        saveBrowser(config, browser)

# Saves The Browser
def saveBrowser(config, browser=None):
    if browser == "MSEdgeHTM":
        config.set("main", "browser", "Edge")
    elif browser == "firefox_firefox.desktop":
        config.set("main", "browser", "Firefox")
    else:
        config.set("main", "browser", browser)    
    save_config(config)

def setfirstlaunch(config):
    config.set("main", "firstlaunch", "no")
    save_config(config)

# Make random decisions/events at app launch
def decide_random_events(config, colorScheme, language_module):
    x = random.randint(1, 4)
    if x == 3:
        print(language_module.prompt3)
    elif x == 2:
        print(language_module.prompt4)

# Print messages on the first launch
def print_first_launch_messages(config, colorScheme, language_module):
    if config.get("main", "firstlaunch") == "yes":
        print(
            colorScheme + language_module.note + Fore.RESET + language_module.warning3
        )
        print()
    if config.get("main", "prerelease") == "yes":
        print(
            colorScheme + language_module.note + Fore.RESET + language_module.warning4
        )
        print(language_module.prompt2)
        print()

# Print a separator in command line interface
def print_separator():
    print(
        Fore.RESET
        + """
===========================================================================
        """
    )

# Save the updated configuration 
def save_config(config):
    with open("./config/config.ini", "w") as f:
        config.write(f)

# Print system keys from configuration
def syskeys(config):
    print("Here are your system keys.")
    print(str(config.get("main", "privatekey")))
    print(str(config.get("main", "syscrypt")))

# Get global default download path from configuration
def globalPath(config):
    config.read("./config/config.ini")
    path = config.get("main", "defaultDlPath")
    return path

# Clearing directory contents
def dirDump(mydir):
    filelist = [f for f in os.listdir(mydir)]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

# Create needed folders on startup
def create_folders(folder_list, language_module):
    for folder in folder_list:
        if not os.path.exists(folder):
            print(f"{language_module.config7}{folder}")
            os.makedirs(folder)
        else:
            print(f"{language_module.config8}{folder}")


# VALID_CHOICES holds possible valid inputs for configuration
VALID_CHOICES = {
    "checkforupdates": ["yes", "no"],
    "showtips": ["yes", "no"],
    "browser": ["Firefox", "Edge", "Chrome"],
    "defaultdlpath": [],
    "language": ["en", "ar", "de", "es", "fr", "hi", "il", "it", "ru", "pt", 'id',"fi","tw","fa","ja","zh_cn"],
    "colorscheme": ["RED", "GREEN", "BLUE", "WHITE", "YELLOW", "BLACK"],
    "userandomuseragents": ["yes", "no"],
}

# Display config options
def display_options(config, section, language_module):
    print("")
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
    #proper translations will be added soon
    print(f"[7] Plugin Folder: {config.get('main','pluginfolder')}")
    print(f"[8] Use Random User Agents: {config.get('main','userandomuseragents')}")
    print("=====================================================")
    print(f"{language_module.configOptionA} ")
    print(f"{language_module.configOptionB} ")
    print("=====================================================")

# Update configuration with new values
def update_config(config, section, option_key, new_value):
    config.set(section, option_key, str(new_value))
    save_config(config)

# Editor function to modify config settings
def config_editor(config: configparser.ConfigParser, language_module) -> bool:
    """
    Edits configuration options based on user input.
    """

    OPTION_MAPPING = {
        "1": ("main", "checkforupdates"),
        "2": ("Personalizations", "showtips"),
        "3": ("main", "defaultdlpath"),
        "4": ("main", "browser"),
        "5": ("main", "language"),
        "6": ("Personalizations", "colorscheme"),
        "7": ("main", "pluginfolder"),
        "8": ("main", "userandomuseragents"),
        "A": ("main", "option_A"),
        "B": ("main", "option_B"),
        "a": ("main", "option_A"),
        "b": ("main", "option_B"),
    }

    if input(language_module.config5).lower() == "y":
        display_options(config, "main", language_module)  # Display initial options

        while True:
            edit_config_index = input(language_module.config6)
            selected_option = OPTION_MAPPING.get(edit_config_index)

            if selected_option:
                section, option_key = selected_option

                if option_key == "custom_config":
                    handle_custom_config(config)
                elif option_key in ("option_A", "option_B"):
                    handle_special_options(config, option_key)
                else:
                    handle_standard_option(config, section, option_key)

                break  # Exit loop after successful option handling

            else:
                print("Invalid option selected.")

        return True

    else:
        print("Aww ok")
        return False

# Helper functions for clarity
def handle_custom_config(config):
    custom_section = input("Enter the custom configuration section: ")
    custom_config_key = input("Enter the custom configuration key: ")
    value = config.get(custom_section, custom_config_key)
    print(f"Custom Configuration: {custom_section}.{custom_config_key}: {value}")

def handle_special_options(config, option_key):
    if option_key == "option_A":
        handle_option_A(config)
    elif option_key == "option_B":
        handle_option_B(config)

def handle_standard_option(config, section, option_key):
    valid_choices = VALID_CHOICES.get(option_key)
    new_value = get_user_input_with_choices(option_key, valid_choices)
    update_config(config, section, option_key, new_value)

def get_user_input_with_choices(option_key, valid_choices):
    choices_str = f"({'/'.join(valid_choices)})" if valid_choices else ""
    new_value = input(f"{option_key.capitalize()} {choices_str}: ⤷ ")
    if valid_choices and new_value not in valid_choices:
        print(f"Invalid choice. Please choose from {', '.join(valid_choices)}")
        new_value = get_user_input_with_choices(option_key, valid_choices)  # Recurse until valid
    return new_value

# Your function for option A
def handle_option_A(config):
    dirDump(str(config.get("main", "defaultdlpath")))
    dirDump("captured")
    delete_pycache("./")
    try:
     req = requests.get("https://raw.githubusercontent.com/Alfredredbird/tookie-osint/refs/heads/main/config/config.ini")
    except Exception:
     print("Couldnt fetch default config.")
    try:
     with open("./config/config.ini", "w") as f:
         if req.status_code == 200:
          f.writelines(req.text)
          f.close()
          print("Reset config.ini")
         else:
          f.close()
    except Exception:
     print("Error resetting config.ini")

# Your function for option B
def handle_option_B(config):
    syskeys(config)
