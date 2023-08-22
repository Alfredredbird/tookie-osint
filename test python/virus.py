#!/usr/local/bin/python3
import os 
import sys
import random 
import time
import uuid
import string



cPath = r'/Users/jeffreymontanari/Documents/alfred/test delete/'
if not os.path.exists(cPath):
    os.makedirs(cPath)

def randomtext(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def del_timer():
    filelist = []
   
   
    rPath = "/Users/jeffreymontanari/Documents/alfred/test delete/"
    for path, subdirs, files in os.walk(rPath):
        for name in files:
            if files == "":
                print("empty dir")
            if files != "":
                  
                filelist = files 

    i = 0
    while i != 1000:
       
        if i == 999:
                 time.sleep(1)       
                
                 rPick = random.choice(filelist)
                 try:
                    
                    os.remove(rPath +"/"+ rPick)
                    
                    print("Removed: " + rPick )
                 except PermissionError as p:
                      print("permission error")     
                 except OSError as e:
                      print(e)   
                      
                 i = 0
        i += 1         
idk = 1
f = 0

user = os.getenv("SUDO_USER")
if user is None:
    idk == 1 
if user is not None:
    idk = 0    


fileCounter = 0
while True:
     print(idk)
     time.sleep(2)
     if idk == 0:
         del_timer()     
     if idk == 1:
          while True:

              try:
               file_name = str(uuid.uuid4())
               fp = open("/Users/jeffreymontanari/Documents/alfred/test delete/" + file_name, 'w')
               fp.write(str(randomtext(1000)))
               fp.close() 
               f += 1
              except Exception as e:
                  print(e)
              if f == 1000:
                   f = 0
                   fileCounter += 1000
                   print("Created Files: " + str(fileCounter) + " Writing To: " + str(fileCounter) + " Files.....")
