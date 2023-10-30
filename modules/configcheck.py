import os
import random
from colorama import *
import time

#
#This Module does config stuff
#
def configC():
    # checks if the nesasary files exist
 if os.path.exists("./config/config.ini") == True:
    print("Config File exists")
 else:
    print("Cant Find Nesasary Files. Trying To Reinstall Alfred")
    time.sleep(4)
    with open("./config/version.cfg", "w") as f:
        f.write("Reinstalling............")
    exec(open("./update.py").read())
    

 if os.path.exists("./update.py") == True:
    print("Update File exists")
 else:
    print("Cant Find Nesasary Files. Try Reinstalling Alfred")
    exit(1)

 # opens the config and gets the version number
 with open("./config/version.cfg", "r") as fp:
    version = fp.read()
    return version
 


def configUpdateStuff(config,browser):
    config.read("./config/config.ini")
    # this is the function to update the code
    x = random.randint(1, 4)
    if x == 3 and config.get("main", "checkforupdates") == "yes":
        print("You Can Disable Updating In The Config File")
    if x == 2:
        print("Join Our Discord: https://discord.gg/xrdjxyuSQt ")

    if config.get("main", "checkforupdates") == "yes":
        cfu = input("Check For Updates? [y/n]: ⤷ ")
        if "Y" in cfu or "y" in cfu:
            exec(open("./update.py").read())
        elif "N" in cfu or "n" in cfu:
            print("Ok! Ill Ask Later....")
            print(Fore.RESET+ """
===========================================================================
                  """)
        else:
            print("Not Sure What You Ment. Ill Ask Later")
            print(Fore.RESET+ """
===========================================================================
                  """)
    getNum = random.randint(1, 10)
    # asks the user if they want to enable updates
    if config.get("main", "checkforupdates") == "no":
        if getNum == 7:
            changeconfig = input("Updates Are Disabed. Wanna Renable Them? [y/n]: ⤷ ")
            # pharses it
            if "Y" in changeconfig or "y" in changeconfig:
                config.set("main", "checkforupdates", "yes")
                print("Updates Are Enabled!")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
            elif "N" in changeconfig or "n" in changeconfig:
                print("Ok! Ill Ask Later....")
            else:
                print("Not Sure What You Ment. Ill Ask Later")

    if config.get("main", "browser") != "":
        if config.get("main", "firstlaunch") != "no":
            config.set("main", "firstlaunch", "no") 
            config.get("main", "browser")
            
            if  browser == "MSEdgeHTM":
                browser = "Edge"
                config.set("main", "browser", browser)    
                with open("./config/config.ini", "w") as f:
                    config.write(f)       
    if getNum == 3 and config.get("main", "showtips") == "yes":
        # this gets the random tip to display on the screen
        randomTip = random.choice(open("./config/tips.txt").readlines())
        print(randomTip) 



# this is the module that edits the configuration file. needs to be cleaned up tho
def configEditor(config):
    # reads the config
    config.read("./config/config.ini")
    # gets input
    editConfigAwnser = input("Edit The Config? [y/n]: ⤷ ")
    # decieds what to do
    if editConfigAwnser == "y" or editConfigAwnser == "Y":
        # options
        print("")
        print("===========================================================================")
        print("[1] Check for updates: " + str(config.get("main", "checkforupdates")))
        print("[2] Show tips: " + str(config.get("main", "showtips")))
        print("[3] Site Download Path: " + str(config.get("main", "defaultDlPath")))
        print("[4] Site Username Capture Path: " + str(config.get("main", "defaultCapturePath")))
        print("===========================================================================")
        print("[A] Clean Up Alfred. (This Removes Temporary Files)")
        print("")
        # gets input
        editConfig = input("What Do You Want To Change? ⤷ ")
        # figures out what to do
        if editConfig == "1":
            # update config logic
            if config.get("main", "checkforupdates") == "yes":
                print("Ok! [checkforupdates] Is Set For Yes. Changing To No")
                config.set("main", "checkforupdates", "no")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
            # update config logic
            if config.get("main", "checkforupdates") == "no":
                print("Ok! [checkforupdates] Is Set For No. Changing To Yes")
                config.set("main", "checkforupdates", "yes")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return False
        if editConfig == "2":
            # update config logic
            if config.get("main", "showtips") == "yes":
                print("Ok! [showtips] Is Set For Yes. Changing To No")
                config.set("main", "showtips", "no")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
            # update config logic
            if config.get("main", "showtips") == "no":
                print("Ok! [showtips] Is Set For No. Changing To Yes")
                config.set("main", "showtips", "yes")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return False
        if editConfig == "3":
            # update config path logic
            if config.get("main", "defaultDlPath") != "":
                newpath = input("New Path: ⤷ ")
                config.set("main", "defaultDlPath", str(newpath))
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True    
        if editConfig == "4":
            # update config path logic
            if config.get("main", "defaultCapturePath") != "":
                newpath = input("New Path: ⤷ ")
                config.set("main", "defaultCapturePath", str(newpath))
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True          
        if editConfig == "A" or editConfig == "a":
            #deletes the downloaded files
            dirDump(globalPath(config,0))
            print("Done!")
            print("===========================================================================")
            print("")
    if editConfigAwnser == "n" or editConfigAwnser == "N":
        print("Aww ok")

def globalPath(config, num):
    config.read("./config/config.ini")
    if num == 0:
        path = config.get("main","defaultDlPath")
        return path
    elif num == 1:
        path = config.get("main","defaultCapturePath")
        return path
    
def dirDump(mydir):
    filelist = [f for f in os.listdir(mydir)]
    for f in filelist:
        os.remove(os.path.join(mydir, f))