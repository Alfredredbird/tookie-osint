#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import urllib.request
import platform
from timeit import default_timer
from colorama import Fore, Back, Style
import logging
import json
import requests
from pathlib import Path
import time
import site
import random
from time import sleep
from rich.console import Console
from alive_progress import *
import string

alist = True
fastMode = 0
cError = 0
siteProgcounter = 0
console = Console()
testall = False
slectpath = ""
def update_progress(progress):
     print("\r [{0}] {1}%".format('#'*(progress//10), progress), end='')

def get_random_string(length):
    # choose from all lowercase letter
    
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
     


#site lists
siteList = []
siteNSFW = []

ec = 0
os.system('cls' if os.name == 'nt' else 'clear')
print (Fore.RED +'''
 █████╗ ██╗     ███████╗██████╗ ███████╗██████╗ 
██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔══██╗           __,---.
███████║██║     █████╗  ██████╔╝█████╗  ██║  ██║          /__|o\  )
██╔══██║██║     ██╔══╝  ██╔══██╗██╔══╝  ██║  ██║           `-\ / /
██║  ██║███████╗██║     ██║  ██║███████╗██████╔╝            ,) (,
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝            //   \\
                                                          {(     )}
===========================================================""===""=========
                                                            |||||
                 By Jeffrey Montanari                        |||
                 Twiter: @alfredredbird1                      |

             Thanks To Our Sponsor: Smoke-wolf
''');

## prints os infomation
if platform.system() == 'Windows':
    
    print (Fore.RED + '     Desclaimer: Not All Sites And Or Proxys Are Garineteed To Work! \n By Using You Take Full Account Of Your Actions')
    print (Fore.RESET + 'Type -h twice ')
   

    
    print ('')
    print (Fore.RESET + "===========================================================================")
else:    
    print (Fore.RESET + '===========================================================================')
    print (Fore.RED + '     Desclaimer: Not All Sites And Or Proxys Are Garineteed To Work! \n     By Using You Take Full Account Of Your Actions')
    
    
    print (Fore.RESET + ' ')
    print(platform.system())
    print(platform.release())
    print ('')
    print (Fore.RESET + '===========================================================================')
 
 
print (' ')
uname = input('⤷ ')

test = False
# if "-t" in modes:
#     timeout = input('   ⤷ ')
#     timeout = int(timeout)
    
# test = False

#     #extra
# modes = modes + input('⤷ ')   
# 
#  
def prx_checker(prx):
	try:
		#Get proxy
		get = requests.get(prx)
		# if the request succeeds 
		if get.status_code == 200:
			return(f"{prx}: is reachable")
		else:
			return(f"{prx}: is Not reachable, status_code: {get.status_code}")

	#Exception
	except requests.exceptions.RequestException as e:
        # print proxy with Errs
		raise SystemExit(f"{prx}: is Not reachable \nErr: {e}")
modes = ""
inputnum = ""
ars = ""
while test != True:
    input1 = input('⤷ ')
    if input1 != "":
        if "-t" in input1:
  
         input2 = input("   ⤷ ")
         if (input2 == ""):
             lol = 1
         if(input2 != ""):
             modes += input1
        
             try:
                timeout = int(input2);
             except ValueError:
                print("Timeout Must Be A Number")
                if ("-t" in input2 ):
                    input1.replace("-t", "")
        if "-c" in input1:
         typeInput = input("TYPE: ⤷ ")
         if typeInput != "":

            input2 = input("    IP: ⤷  ")
            if (input2 == ""):
                print("    You Need An IP Silly.")    
                lol = 1
            if(input2 != ""):
                modes += input1
             
                input3 = input("     PORT: ⤷  ")
                if (input3 != ""):
                    try:
                     #finish adding connectton options
                     prxs = input2 + ":" + input3
                     proxies = {"{typeInput}": prxs}
                    #  print("Proxy: " + input2 + ":" + input3)
                     
                    except requests.exceptions.ProxyError:
                     print(Fore.RED + "Proxy Error!" + Fore.RESET)

                    print("")
                    print("     Save Proxy To File?")
                    saveProxy = input("         [Y/n]?  ⤷ " )
                    
                    if saveProxy == "Y" or saveProxy == "y":

                        with open("proxyList.txt", 'a') as fp:
                                fp.write(' \n' + input2 + ":" + input3 )
                                fp.close()
                                
                    elif saveProxy == "N" or saveProxy == "n":
                        print("Continuing" + Fore.RED + "." + Fore.GREEN + "." + Fore.YELLOW + "." + Fore.RESET)
                        
            
                if (input3 == ""):
                    print("     Wheres The Port? Lol")    
                    lol = 1  
                    
 
      


    
   
         if typeInput == "":
             print("Needs Proxy Type!")    
             if ("-c" in input1 ):
                    input1.replace("-c", "")     
                         
                     
        if("-q" in input1 or "--quit" in input1):
            exitInput = input("Exit? [Y/N]")
            if (exitInput == "Y" or exitInput == "y"):
                 exit(0)
            if (exitInput == "N" or exitInput == "n"):
             print("Continueing....")

        if "-gsl" in input1:
            input2 = input("CHAR: ⤷ ")
            trys = input("  TRYS: ⤷ ")
            siteType = input("     TYPE: ⤷ ")
            siteGenOPtions = input("       OPTIONS: ⤷ ")
            if(siteGenOPtions == ""):
                lol = 1
            if(siteGenOPtions != ""):
                if("-a" in siteGenOPtions):
                    testall = True
            if(input2 == ""):
                lol = 1
            if(input2 != ""):
             
             with console.status("Testing.....") as status:
    
                siteLst = []
                b = 0
                if testall == False:
                 if (siteType != ""):
                 
                  while b != int(trys):
                    b += 1
                    siteLst.append("https://" + str(get_random_string(int(input2))) + str(siteType))
                 if (siteType == ""):
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".com")   
                if testall == True:    
                 if (siteType != ""):
                 
                  while b != int(trys):
                    b += 1
                    siteLst.append("https://" + str(get_random_string(int(input2))) + str(siteType))
                 if (siteType == ""):
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".com")
                  b = 0 
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".net")
                  b = 0 
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".org")
                  b = 0  
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".xyz") 
                  b = 0  
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".edu") 
                  b = 0  
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".co")
                  b = 0  
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".org")
                  b = 0  
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".us")
                  b = 0  
                  while b != int(trys):
                   b += 1
                   gen = get_random_string(int(input2))
                   siteLst.append("https://" + str(gen) + ".uk")   
                  b = 0  
                  


                siteError = 0
# print(siteLst)
                i = 0
                f = open("working.txt", "w")
                while i != len(siteLst) :
                    
                     
                     try:
                      r = requests.get(siteLst[i], timeout=1)            
                      print('[' + Fore.GREEN + "+" + Fore.RESET + "] " + str(siteLst[i]) + " " + str(i) + "/" + str(trys))
                      if r.status_code >= 200 and r.status_code <= 500:
                           #f.write(str(siteLst[i])+ "\n")
                           f.write('{"site": "' + str(siteLst[i])+"/"+ '", "nsfw": "False"}' + "\n")
                     except requests.exceptions.ConnectionError:
                         siteError += 1   
                         print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + " " + str(i) + "/" + str(trys)) 
                                  
                     except IndexError:
                         i = len(siteLst) + 1
                         print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + " " + str(i) + "/" + str(trys))
                     except requests.exceptions.Timeout:
                        siteError += 1
                        print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + " " + str(i) + "/" + str(trys))
                     except requests.exceptions.HTTPError():
                         siteError += 1
                         print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + " " + str(i) + "/" + str(trys))
                     except requests.exceptions.SSLError():
                      siteError += 1
                      print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + " " + str(i) + "/" + str(trys))
                     except requests.exceptions.RetryError():
                        siteError += 1
                        print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + " " + str(i) + "/" + str(trys))
                     except requests.exceptions.TooManyRedirects():
                         siteError += 1     
                         print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + + " " + str(i) + "/" + str(trys)) 
                     except TypeError():
                         siteError += 1     
                         print('[' + Fore.RED + "-" + Fore.RESET + "] " + "?" + + " " + str(i) + "/" + str(trys))
                     except KeyboardInterrupt():
                         print("Stopping..... Saved To ./working.txt")


                     i += 1   
                     
                print(str(siteError) + " Not Working Sites..." )
                

        if "-d" in input1:
  
         input2 = input("   ⤷ ")
         if (input2 == ""):
             lol = 1
         if(input2 != ""):
             modes += input1
        
             try:
                
                ars = bool(input2)
             except ValueError:
                print("Timeout Must Be A Number")
                if ("-d" in input2 ):
                    input1.replace("-d", "")     
                         
        if "-s" in input1:
  
          input2 = input("[Y/N]? ⤷ ")
          if (input2 == ""):
             lol = 1
          if(input2 != ""):
             if (input2 == "Y" or input2 == "y"):
                 modes += input1
                 inputnum += input2
             if (input2 == "N" or input2 == "n"):
                
                 modes = ""
                 inputnum = "" 
                 uname = input('⤷ ')
                 test = False   
                 input2 = ""
                 input1 = ""
   
        if ("-ec" in input1 ):
            ec = 1   
        if ("-lp" in input1):
            input2 = input("TYPE:  ⤷ ")
# check if the directory exists
            if (input2 == ""):
                lol = 1
            if (input2 == "http"):
                
                if os.path.exists ("./proxys/http.txt"): 
                    
                    file1 = open("./proxys/http.txt", 'r')
                    Lines = file1.readlines()
 
                    count = 0
                    L = [Lines]

                
                    for line in Lines:
                         count += 1
                         print("Proxy {}: {}".format(count, line.strip()))
                else:
                    print(Fore.RED + "Cant Find The Proxy File!")
                    print(Fore.RESET)

                
                    
            elif (input2 == "socks4"):
                
                if os.path.exists ("./proxys/socks4.txt"): 
                    
                    file1 = open("./proxys/socks4.txt", 'r')
                    Lines = file1.readlines()
 
                    count = 0
                    L = [Lines]

                
                    for line in Lines:
                         count += 1
                         print("Proxy {}: {}".format(count, line.strip()))
                else:
                    print(Fore.RED + "Cant Find The Proxy File!")
                    print(Fore.RESET)

            elif (input2 == "socks5"):
                
                if os.path.exists ("./proxys/socks5.txt"): 
                    
                    file1 = open("./proxys/socks5.txt", 'r')
                    Lines = file1.readlines()
 
                    count = 0
                    L = [Lines]

                
                    for line in Lines:
                         count += 1
                         print("Proxy {}: {}".format(count, line.strip()))
                
                      
                else:
                    print(Fore.RED + "Cant Find The Proxy File!")
                    print(Fore.RESET)
        if ("-O" in input1 or "-o" in input1):
             
            slectpath = Path.home() / str(input("PATH: ⤷ "))
            file_path = os.path.join(slectpath)
# check if the directory exists
            fastMode = 2
            
            if os.path.exists (file_path): 
    # reads the file
               
               try:
                file = open(file_path, "r+")
                
                # with open(file_path, 'r') as fp:
                #     content = fp.readlines()
        
                # with open(file_path, 'w') as fp:
                #     for line in content:
                #         fp.write(line.strip('') + ' \n')
                #         print(content)
            #   lnum += 1
                file1 = open(file_path, 'r')
                Lines = file1.readlines()
 
                count = 0
                L = [Lines]

                for line in Lines:
                    count += 1
                    print("Lines {}: {}".format(count, line.strip()))    
       
                
                file.close()
                
               except PermissionError():
                print("Permission Error")  
               except TypeError():
                   print("Type Error") 
            else:
                print(Fore.RED + "Cant Find The Save File!")
                print(Fore.RESET)
                exit(69)             

        if ("-r" in input1 or "--read" in input1):
            if (slectpath == ""):
             dir_path = Path.home() / "Downloads"
  
             file_name = "usernames.alfred"
             file_path = os.path.join(dir_path, file_name)
            if(slectpath != ""):
                 file_path = os.path.join(slectpath)
# check if the directory exists
            if os.path.exists (file_path): 
    # reads the file
                file = open(file_path, "r+")
                
                # with open(file_path, 'r') as fp:
                #     content = fp.readlines()
        
                # with open(file_path, 'w') as fp:
                #     for line in content:
                #         fp.write(line.strip('') + ' \n')
                #         print(content)
            #   lnum += 1
                file1 = open(file_path, 'r')
                Lines = file1.readlines()
 
                count = 0
                L = [Lines]

                for line in Lines:
                    count += 1
                    print("Captured {}: {}".format(count, line.strip()))    
       
                file.close()
                
            else:
                print(Fore.RED + "Cant Find The Save File!")
                print(Fore.RESET)
                
        #code to read and check files        
         
               

        if ("-p" in input1 or "--ping" in input1):    
         headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'}
         print(Fore.RED + "Defults To HTTPS" )
      
         print(Fore.RESET + ' ')
     
         reqSite = input('⤷ ')

      
         try:
            print(Fore.RESET + "Status Code:")
            test = requests.get(reqSite) 
            print(test.status_code)
            
         except:
          print(Fore.RED + "Error!")  
          print(Fore.RESET + " ")
          exit()
         exit()

        if "-a" in input1:
  
            # input4 = input("   ⤷ ")
            # if (input4 == ""):
            #      lol = 1
            # if(input4 != ""):
        
                modes += input1

        if "-f" in input1:
                fastMode = 1;    

        if "-N" in input1:
        
            modes += input1        

       
        if ("-h" in uname or "--help" in uname or "-h" in input1 or "--help" in input1):
            print ('''
██╗   ██╗███████╗ █████╗  ██████╗ ███████╗
██║   ██║██╔════╝██╔══██╗██╔════╝ ██╔════╝
██║   ██║███████╗███████║██║  ███╗█████╗  
██║   ██║╚════██║██╔══██║██║   ██║██╔══╝  
╚██████╔╝███████║██║  ██║╚██████╔╝███████╗                      
 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      \      \    
                                                (o>    (o>
Usage: [USERNAME]                               //\    //\ 
       [OPTIONS]                                V_/    V_/ 
================================================================
                                                ||     ||
                                                ||     ||
   [COMMAND]  [ALIAS]  [INFO]

        -h  | --help |
------------+--------+------------------------------------------
        -r  | --read | (Reads Last Search Results) 
        -p  | --ping | (pings website)
        -q  | --quit | (Quits)
        -lp |        | (Gives A List Of Posible Working Proxys)
            |        | Types:
            |        |
            |        |       http   ⥴ /http.txt
            |        |       socks4 ⥴ /socks4.txt
            |        |       socks5 ⥴ /socks5.txt
            |        |
        -gsl|        | (Generates Random Sites And Tests Them)
            |        |  Ussage:
            |        |     [LENGTH]
            |        |        [AMOUNT]
            |        |           [TYPE] 
            |        |              [OPTIONS]
------------+--------+------------------------------------------
        -a  |        | (Shows Everything) 
            |        | Error ID's:
            |        |   
            |        |      S ⥴ SSL Error  
            |        |      H ⥴ HTTP Error  
            |        |      T ⥴ Connection Timeout   
            |        |      R ⥴ Retry Error  
            |        |      P ⥴ Proxy Error  
            |        |      C ⥴ Connection Error  
            |        |      I ⥴ Invalid URL  
            |        |      N ⥴ Header Error 
            |        |      CE ⥴ Chunk Error  
            |        |
            |        +-----------------------------------------
        -N  | --nsfw | (Points NSFW Sites)    
        -ec |        | (Prints The Returned Status Code)
        -s  |        | (Starts The Program)
        -d  |        | (Allows Redirects "Might Not Be Accutate")
        -c  |        | (Connects To A Proxy Server)
            |        | Format [Type] [Ip] [Port] 
        -f  |        | Runs A Fast Scan    
        -O  |        | Checks Accounts From A List
''')   
            

        


        

    

   
    if "" in input1 and inputnum != "":
        test = True
    inputnum = ""     
# print (modes)
# test = False
# lol = 0
# uname = input('⤷ ')


# while test != True:
#  modes = input("⤷")
#  if "-t" in modes:
  
#   input2 = input("   ⤷ ")
#   if (input2 == ""):
#    lol = 1
#   if(input2 != ""):
#    modes += input1
   
#    timeout = int(input2);
#    lol = 2


#  if "-a" in input1:
  
#   input4 = input("   ⤷ ")
#   if (input4 == ""):
#    lol = 1
#   if(input4 != ""):
#    modes += input1
#    modes += input4

# print(lol)
# print(uname)
# print(modes)





  






# if (" " in uname ):
#     print(Fore.RED + "Error: Space In Username!" )
#     exit()


         
# elif (" " in uname and nums != 1):
#      print(Fore.RED + "Error: Space In Username!" )
#      exit()


# else:
      
#   if ("-a" in uname):    
#     uname = uname.replace("-a","")
  
 
 
  
# replace with your preferred directory and file path
dir_path = Path.home() / "Downloads"
  
file_name = "usernames.alfred"
file_path = os.path.join(dir_path, file_name)
# check if the directory exists
if os.path.exists (dir_path):
    # create the file
        print(' ')
        print('Creating / Overwriting Save File.')

else:
    print("Directory doesn\'t exist.")



if fastMode == 0: 
    try:
        with open('sites.json', 'r') as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")
    
        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)

if fastMode == 1:
    try:
        with open('fsites.json', 'r') as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                siteList.append(siteDic)
    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")
    
        exit(-1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)
        exit(-9)
if fastMode == 2:
    
    try:
                    with open(slectpath, 'r') as f:
                     for jsonObj in f:
                         siteDic = json.loads(jsonObj)
                         siteList.append(siteDic)
    except FileNotFoundError:
            print(Fore.RED + "Cant Find Site File")
    
            exit(-1)
    except json.JSONDecodeError:
            print(Fore.RED + "Error With Site File" + Fore.RESET)
            exit(-9)
                    
connection_error = 0  


print(Fore.GREEN + "searching for sites with: " + uname + Fore.RESET) 
print("")
siteCount = 0
with open(file_path, "w") as f:
  
     
     
  for site in siteList:
    siteCount += 1
    with console.status("Working....") as status:
    #    prints the sites
    #    print(site["site"], site[uname])
 
       siteN = site["site"]
       siteNSFW = site["nsfw"]
    #    update_progress(siteProgcounter) 
       
       
        
       try:   
         headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'}
         if "-t" in modes :
           
            response = requests.get(siteN + uname, headers=headers, timeout=timeout, allow_redirects = False, proxies=False, json=False)#35
         if "-d" in modes :
           
            response = requests.get(siteN + uname, headers=headers, timeout=1.5, allow_redirects = ars, proxies=False, json=False)   
         if "-c" in modes :
            
            response = requests.get(siteN + uname, headers=headers, timeout=1.5, allow_redirects = False, proxies=proxies, json=False) 
            
         else:
             
             response = requests.get(siteN + uname, headers=headers, timeout=1.5, allow_redirects = False, proxies=False, json=False)
  
         if (ec ==1): 
          print(response.status_code)
        #   if siteNSFW == "true":
        #             print('[' + Fore.LIGHTMAGENTA_EX + "+" + Fore.WHITE + "] " + siteN  + uname + "     " + Fore.YELLOW + siteNSFW + Fore.RESET)
        #             f.write('[' + "+" + "] " + siteN  + uname + "NSFW" + "\n")
        #  checks for connection error
         if(response.status_code == 200):
             siteProgcounter += 1       
       except requests.exceptions.SSLError:
            connection_error = 1  
            #  print(requests.exceptions.HTTPError)
            if "-a" in modes: 
                print('[' + Fore.YELLOW + "S" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "S" + "] " + siteN  + uname +  "\n") 
       except requests.exceptions.HTTPError:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "H" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "H" + "] " + siteN  + uname +  "\n") 
       except requests.exceptions.ConnectTimeout:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "T" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "T" + "] " + siteN  + uname +  "\n")       
       except requests.exceptions.ReadTimeout:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "T" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "T" + "] " + siteN  + uname +  "\n")                  
       except requests.exceptions.RetryError:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "R" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "R" + "] " + siteN  + uname +  "\n")     
       except requests.exceptions.ProxyError:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "p" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "P" + "] " + siteN  + uname +  "\n")     
       except requests.exceptions.ConnectionError:
             cError += 1
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "C" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "C" + "] " + siteN  + uname +  "\n")                 
       except requests.exceptions.InvalidURL:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "I" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "I" + "] " + siteN  + uname +  "\n")   
       except requests.exceptions.InvalidHeader:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "N" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "N" + "] " + siteN  + uname +  "\n")
       except requests.exceptions.ChunkedEncodingError:
             if "-a" in modes: 
                print('[' + Fore.YELLOW + "CE" + Fore.RESET + "] " + siteN  + uname) 
                f.write('[' + "CE" + "] " + siteN  + uname +  "\n")     
       except KeyboardInterrupt:
                        
                        print('''
===========================================================

''')
                        print("Stopping........")
                        print("Found: " + str(siteProgcounter) + " Posible Accounts")
                        f.close 
                        print("Saved Results To File")                  
                        exit(99)         
       else:            
             
                
                    
           
     
          
            if "-a" in modes:        
                        
                if response.status_code >= 300 or response.status_code >= 510:
                    print('[' + Fore.RED + "-" + Fore.RESET + "] " + siteN  + uname) 
                    f.write('[' + "-" + "] " + siteN  + uname +  "\n")  
                if response.status_code == 406:
                    print('[' + Fore.RED + "-" + Fore.RESET + "] " + siteN  + uname) 
                    f.write('[' + "-" + "] " + siteN  + uname +  "\n")          

            if "-N" in modes:
               
                  if response.status_code == 200 and siteNSFW == "true":
                    print('[' + Fore.LIGHTMAGENTA_EX + "NSFW" + Fore.RESET + "] " + siteN  + uname + "     " + Fore.RESET)
                    f.write('[' + "+" + "] " + siteN  + uname + "             NSFW" + "\n")

                  if response.status_code == 200 and siteNSFW == "false":
                    print('[' + Fore.GREEN + "+" + Fore.RESET + "] " + siteN  + uname )
                    f.write('[' + "+" + "] " + siteN  + uname +  "\n")   
            if response.status_code == 200 and "-N" not in modes:
                    print('[' + Fore.GREEN + "+" + Fore.RESET + "] " + siteN  + uname )
                    f.write('[' + "+" + "] " + siteN  + uname +  "\n")
            if response.status_code == 406 and "-N" not in modes:
                    print('[' + Fore.GREEN + "+" + Fore.RESET + "] " + siteN  + uname )
                    f.write('[' + "+" + "] " + siteN  + uname +  "\n")        
           
            
        # elif " " in uname and nums != 1:
        #  print(Fore.RED + "Error: Space In Username!" )
        #  exit()
if cError >= 5:
    print(Fore.RED +'''
===========================================================

''')
    print(Fore.RED + "Uh Oh Error! Looks Like The Connection Dont Seem To Be Working. Check your connection Or Proxy, Then Try Again :(")   
    print(Fore.RED +'''

===========================================================
''')
if cError <= 5:         
    f.close 
    print('''
===========================================================

''')

def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100
    
print("Found: " + str(siteProgcounter) + '/' + str(siteCount) + " Posible Accounts With " + str(is_what_percent_of(siteProgcounter, siteCount).__round__()) + "% Acuracy")
print("Saved Results To File")


startagain = input("Run Again?: [Y/N] ⤷ ")
if ("Y" in startagain or "y" in startagain):
    exec(open("brib.py").read())
elif("N" in startagain or "n" in startagain):
    exit() 