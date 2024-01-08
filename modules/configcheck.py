import configparser
import os
import random
import shutil
import time

import requests
from colorama import *

from lang.en import *
from modules.lang import *
from modules.webscrape import *

#does stuff involving plugins
class PluginManager:
    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    pluginFolder = config.get("main", "pluginfolder")
    def __init__(self, plugins_directory=pluginFolder):
        self.plugins = {}
        self.plugins_directory = plugins_directory

    def load_plugins(self):
        # Get a list of all files in the plugins directory
        plugin_files = [f[:-3] for f in os.listdir(self.plugins_directory) if f.endswith('.py')]

        for plugin_name in plugin_files:
            try:
                module = importlib.import_module(f"{self.plugins_directory}.{plugin_name}")
                self.plugins[plugin_name] = module
                print(f"Plugin '{plugin_name}' loaded successfully.")
            except ImportError as e:
                print(f"Failed to load plugin '{plugin_name}': {e}")

    def run_plugins(self):
        for plugin_name, module in self.plugins.items():        
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
def colorSchemeGrabber(config):
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
            exec(open("./update.py").read())
        elif cfu.lower() in ("n", "no"):
            print(language_module.prompt5)
            print_separator()
        else:
            print(language_module.idk2)
            print_separator()
    except KeyboardInterrupt:
        saveBrowser(config,str(get_default_browser()))
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
    is_first_launch(config, browser, language_module)

    # Handle arguments to prevent update prompts
    if any(vars(argument).values()):
        return

    if config.get("main", "checkforupdates") == "yes":
        ask_update_check(config, colorScheme, language_module)

    random_enable_updates(config, language_module)
    display_random_tip(config, language_module)

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
    else:
        config.set("main", "browser", browser)    
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
    "language": ["en", "ar", "de", "es", "fr", "hi", "il", "it", "ru"],
    "colorscheme": ["RED", "GREEN", "BLUE", "WHITE", "YELLOW", "BLACK"],
}

# Display config options
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
    #proper translations will be added soon
    print(f"[7] Plugin Folder: {config.get('main','pluginfolder')}")
    print("=====================================================")
    print(f"{language_module.configOptionA} ")
    print(f"{language_module.configOptionB} ")
    print("=====================================================")

# Update configuration with new values
def update_config(config, section, option_key, new_value):
    config.set(section, option_key, str(new_value))
    save_config(config)

# Editor function to modify config settings
def config_editor(config, language_module):
    selected_option_key = {
        "1": ("main", "checkforupdates"),
        "2": ("Personalizations", "showtips"),
        "3": ("main", "defaultdlpath"),
        "4": ("main", "browser"),
        "5": ("main", "language"),
        "6": ("Personalizations", "colorscheme"),
        "7": ("main","pluginfolder"),
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
