import os


#
#This Module does config stuff
#
def configC():
    # checks if the nesasary files exist
 if os.path.exists("./config/config.ini") == True:
    print("Config File exists")
 else:
    print("Cant Find Nesasary Files. Trying To Reinstall Alfred")
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