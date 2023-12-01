import os
import random
import time
from configparser import ConfigParser

from colorama import *

from lang.en import *
from modules.lang import *

# loads the language


#
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


# this is the module that edits the configuration file. needs to be cleaned up tho
def configEditor(config, language_module):
    # reads the config
    config.read("./config/config.ini")
    # gets input
    editConfigAwnser = input(language_module.config5)
    # decieds what to do
    if editConfigAwnser == "y" or editConfigAwnser == "Y":
        # options
        print("")
        print(
            "==========================================================================="
        )
        print(
            language_module.configOption1 + str(config.get("main", "checkforupdates"))
        )
        print(language_module.configOption2 + str(config.get("main", "showtips")))
        print(language_module.configOption3 + str(config.get("main", "defaultDlPath")))
        print(language_module.configOption4 + str(config.get("main", "browser")))
        print(language_module.configOption5 + str(config.get("main", "language")))
        print(
            "==========================================================================="
        )
        print(language_module.configOptionA)
        print(language_module.configOptionB)
        print("")
        # gets input
        editConfig = input(language_module.config6)
        # figures out what to do
        if editConfig == "1":
            # update config logic
            if config.get("main", "checkforupdates") == "yes":
                print(language_module.configOption1Message)
                config.set("main", "checkforupdates", "no")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
            # update config logic
            if config.get("main", "checkforupdates") == "no":
                print(language_module.configOption1Message2)
                config.set("main", "checkforupdates", "yes")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return False
        if editConfig == "2":
            # update config logic
            if config.get("main", "showtips") == "yes":
                print(language_module.configOption2Message)
                config.set("main", "showtips", "no")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
            # update config logic
            if config.get("main", "showtips") == "no":
                print(language_module.configOption2Message2)
                config.set("main", "showtips", "yes")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return False
        if editConfig == "3":
            # update config path logic
            if config.get("main", "defaultDlPath") != "":
                newpath = input(language_module.configOption3Message)
                config.set("main", "defaultDlPath", str(newpath))
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
        if editConfig == "4":
            # update config path logic
            if config.get("main", "browser") != "":
                print(language_module.configOption4Message)
                newbrowser = input("Browser: ⤷ ")
                config.set("main", "browser", str(newbrowser))
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
        if editConfig == "5":
            # update config path logic
            if config.get("main", "language") != "":
                print(language_module.configOption5Message)
                newbrowser = input("Language Code: ⤷ ")
                config.set("main", "language", str(newbrowser))
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
        if editConfig == "A" or editConfig == "a":
            # deletes the downloaded files
            dirDump(globalPath(config))
            print(language_module.configOptionAMessage)
            print(
                "==========================================================================="
            )
            print("")
        if editConfig == "B" or editConfig == "b":
            print(
                "==========================================================================="
            )
            print(language_module.configOptionBMessage)
            print("")
            print(language_module.configOptionBMessage2)
            print(
                language_module.configOptionBMessage3
                + str(config.get("main", "privatekey"))
            )
            print(
                language_module.configOptionBMessage4
                + str(config.get("main", "syscrypt"))
            )
            print("")
            print(
                "==========================================================================="
            )
    if editConfigAwnser == "n" or editConfigAwnser == "N":
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
