#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import urllib.request
import platform
from timeit import default_timer
import logging
import json
import requests
from pathlib import Path
import time
import site
import requests
import random

cError = 0

# def check_proxy():
#     try:
#         r = requests.get('https://youtube.com', proxies=proxies, timeout=5)
#         if r.status_code == 200:
#             print("YAY")
#             return True
#         else:
#             print("BOO")
#             return False
#     except:
#         print("BOO")
#         return False 
# python -m PyInstaller brib.py --onefile



ec = 0
os.system('cls' if os.name == 'nt' else 'clear')
print ('''
 █████╗ ██╗     ███████╗██████╗ ███████╗██████╗ 
██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔══██╗
███████║██║     █████╗  ██████╔╝█████╗  ██║  ██║
██╔══██║██║     ██╔══╝  ██╔══██╗██╔══╝  ██║  ██║
██║  ██║███████╗██║     ██║  ██║███████╗██████╔╝
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ 

''');


ussage = ''' 
Ussage:

    Username without spaces:

'''



## prints os infomation
if platform.system() == 'Windows':
    print ( '===========================================================')
    print ('Desclaimer: Not All Sites Are Garineteed To Work!')
    print (' ')
   

    
    print ('')
    print ('===========================================================')
else:    
    print ('===========================================================')
    print (  'Desclaimer: Not All Sites Are Garineteed To Work!')
    
    
    print (  ' ')
    print(platform.system())
    print(platform.release())
    print ('')
    print ('===========================================================')
 
 
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
                     print(  "Proxy Error!" )

                    print("")
                    print("     Save Proxy To File?")
                    saveProxy = input("         [Y/n]?  ⤷ " )
                    if saveProxy == "Y" or "y":

                        with open("proxyList.txt", 'a') as fp:
                                fp.write(' \n' + input2 + ":" + input3 )
                                
                    if saveProxy == "N" or "n":
                        print("Continuing" +   "." +   "." +   "."   )
            
                if (input2 == ""):
                    lol = 1  
                    
 
      


    
   
         if typeInput == "":
             print("Needs Proxy Type!")    
             if ("-c" in input1 ):
                    input1.replace("-c", "")     
                         
                     

             

             


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
       
        if ("-r" in input1 or "--read" in input1):
            dir_path = Path.home() / "Downloads"
  
            file_name = "usernames.alfred"
            file_path = os.path.join(dir_path, file_name)
# check if the directory exists
            if os.path.exists (file_path): 
    # reads the file
       
                file = open(file_path, "r+")
        
                with open(file_path, 'r') as fp:
                    content = fp.readlines()
        
                with open(file_path, 'w') as fp:
                    for line in content:
                        fp.write(line.strip('') + ' \n')
                        print(content)
            #   lnum += 1
       
       
                file.close()
                exit(0)
            else:
                print(  "Cant Find The Save File!")
                print("" )
                exit(69) 
        if ("-p" in input1 or "--ping" in input1):    
         headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'}
         print(  "Defults To HTTPS" )
      
         print(  ' ')
     
         reqSite = input('⤷ ')

      
         try:
            print(  "Status Code:")
            print(urllib.request.urlopen(reqSite).getcode())
            
         except:
          print(  "Invalid Site!")  
          print(  " ")
          exit()
         exit()

        if "-a" in input1:
  
            # input4 = input("   ⤷ ")
            # if (input4 == ""):
            #      lol = 1
            # if(input4 != ""):
        
                modes += input1
        if "-N" in input1:
        
            modes += input1        

       
        if ("-h" in uname or "--help" in uname or "-h" in input1 or "--help" in input1):
            print ('''
██╗   ██╗███████╗ █████╗  ██████╗ ███████╗
██║   ██║██╔════╝██╔══██╗██╔════╝ ██╔════╝
██║   ██║███████╗███████║██║  ███╗█████╗  
██║   ██║╚════██║██╔══██║██║   ██║██╔══╝  
╚██████╔╝███████║██║  ██║╚██████╔╝███████╗
 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝



Usage: [USERNAME]   [Its Recommended To Use TWO At A Time]
       [OPTIONS]
========================================================

        -h  | --help |
------------+--------+----------------------------------
        -r  | --read | (Reads Last Search Results) 
        -p  | --ping | (pings website)
------------+--------+----------------------------------
        -a  |        | (Shows Everything) 
            |        | S ⥴ SSL Error  
            |        | H ⥴ HTTP Error  
            |        | T ⥴ Connection Timeout   
            |        | R ⥴ Retry Error  
            |        | P ⥴ Proxy Error  
            |        | C ⥴ Connection Error  
            |        | I ⥴ Invalid URL  
            |        | N ⥴ Header Error 
            |        | CE ⥴ Chunk Error  
        -N  | --nsfw | (Points Our NSFW Sites)    
        -ec |        | (Prints The Returned Status Code)
        -s  |        | (Starts The Program)
        -d  |        | (Allows Redirects "Might Not Be Accutate")
        
            


''')   
            exit()

        


        

    

   
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
#     print(  "Error: Space In Username!" )
#     exit()


         
# elif (" " in uname and nums != 1):
#      print(  "Error: Space In Username!" )
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

siteList = []
siteNSFW = []
try:
    with open('sites.json', 'r') as f:
        for jsonObj in f:
           siteDic = json.loads(jsonObj)
           siteList.append(siteDic)
except FileNotFoundError:
    print(  "Cant Find Site File")
    
    exit(-1)
except json.JSONDecodeError:
    print(  "Error With Site File"   )
    exit(-9)
connection_error = 0  


print(  "searching for sites with: " + uname   ) 
  
with open(file_path, "w") as f:
 for site in siteList:
    #    prints the sites
    #    print(site["site"], site[uname])
 
       siteN = site["site"]
       siteNSFW = site["nsfw"]
      
       

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
        #             print('[' + Fore.LIGHTMAGENTA_EX + "+" +   "] " + siteN  + uname + "     " +   siteNSFW +  )
        #             f.write('[' + "+" + "] " + siteN  + uname + "NSFW" + "\n")
        #  checks for connection error
       except requests.exceptions.SSLError:
            connection_error = 1  
            #  print(requests.exceptions.HTTPError)
            if "-a" or "--all" in modes: 
                print('[' +   "S" +   "] " + siteN  + uname) 
                f.write('[' + "S" + "] " + siteN  + uname +  "\n") 
       except requests.exceptions.HTTPError:
             if "-a" or "--all" in modes: 
                print('[' +   "H" +   "] " + siteN  + uname) 
                f.write('[' + "H" + "] " + siteN  + uname +  "\n") 
       except requests.exceptions.ConnectTimeout:
             if "-a" or "--all" in modes: 
                print('[' +   "T" +   "] " + siteN  + uname) 
                f.write('[' + "T" + "] " + siteN  + uname +  "\n")       
       except requests.exceptions.ReadTimeout:
             if "-a" or "--all" in modes: 
                print('[' +   "T" +   "] " + siteN  + uname) 
                f.write('[' + "T" + "] " + siteN  + uname +  "\n")                  
       except requests.exceptions.RetryError:
             if "-a" or "--all" in modes: 
                print('[' +   "R" +   "] " + siteN  + uname) 
                f.write('[' + "R" + "] " + siteN  + uname +  "\n")     
       except requests.exceptions.ProxyError:
             if "-a" or "--all" in modes: 
                print('[' +   "p" +   "] " + siteN  + uname) 
                f.write('[' + "P" + "] " + siteN  + uname +  "\n")     
       except requests.exceptions.ConnectionError:
             cError += 1
             if "-a" or "--all" in modes: 
                print('[' +   "C" +   "] " + siteN  + uname) 
                f.write('[' + "C" + "] " + siteN  + uname +  "\n")                 
       except requests.exceptions.InvalidURL:
             if "-a" or "--all" in modes: 
                print('[' +   "I" +   "] " + siteN  + uname) 
                f.write('[' + "I" + "] " + siteN  + uname +  "\n")   
       except requests.exceptions.InvalidHeader:
             if "-a" or "--all" in modes: 
                print('[' +   "N" +   "] " + siteN  + uname) 
                f.write('[' + "N" + "] " + siteN  + uname +  "\n")
       except requests.exceptions.ChunkedEncodingError:
             if "-a" or "--all" in modes: 
                print('[' +   "CE" +   "] " + siteN  + uname) 
                f.write('[' + "CE" + "] " + siteN  + uname +  "\n")                                                  
       else:            
             
                
                    
           
     
          
            if "-a" in modes:
                # if connection_error == 1:
                #     print('[' +   "R" +   "] " + siteN  + uname ) 
                #     f.write('[' + "R" + "] " + siteN  + uname +  "\n")        
                        
                if response.status_code >= 300 or response.status_code >= 510:
                    print('[' +   "-" +   "] " + siteN  + uname) 
                    f.write('[' + "-" + "] " + siteN  + uname +  "\n")
                # if response.status_code >= 301 and response.status_code <= 400 :
                #     print('[' +   "-" +   "] " + siteN  + uname) 
                #     f.write('[' + "-" + "] " + siteN  + uname +  "\n")
                # if response.status_code == 308:
                #     print('[' +   "-" +   "] " + siteN  + uname) 
                #     f.write('[' + "-" + "] " + siteN  + uname +  "\n")   
                # if response.status_code == 204:
                #     print('[' +   "-" +   "] " + siteN  + uname) 
                #     f.write('[' + "-" + "] " + siteN  + uname +  "\n")
                
                # if response.status_code == 302:
                #     print('[' +   "-" +   "] " + siteN  + uname) 
                #     f.write('[' + "-" + "] " + siteN  + uname +  "\n")               
                # if response.status_code == 500 or response.status_code == 503 or response.status_code == 510:
               
                #     print('[' + Fore.LIGHTRED_EX + "E" +   "] " + siteN  + uname) 
                #     f.write('[' + "E" + "] " + siteN  + uname +  "\n")

                
                   
                # else:
                #     print('lol')         

            if "-N" in modes:
               
                  if response.status_code == 200 and siteNSFW == "true":
                    print('[' + "NSFW" +   "] " + siteN  + uname + "     ")
                    f.write('[' + "+" + "] " + siteN  + uname + "             NSFW" + "\n")

                  if response.status_code == 200 and siteNSFW == "false":
                    print('[' +   "+" +   "] " + siteN  + uname )
                    f.write('[' + "+" + "] " + siteN  + uname +  "\n")   
            if response.status_code == 200 and "-N" not in modes:
                    print('[' +   "+" +   "] " + siteN  + uname )
                    f.write('[' + "+" + "] " + siteN  + uname +  "\n")
           
            
        # elif " " in uname and nums != 1:
        #  print(  "Error: Space In Username!" )
        #  exit()
if cError >= 5:
    print(  "Uh Oh Error! Looks Like The Connection Dont Seem To Be Working. Check your connection Or Proxy, Then Try Again")        
f.close 
print("Saved Results To File")        
