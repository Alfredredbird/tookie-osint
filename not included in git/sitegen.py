import random
import string
import requests
from colorama import Fore

lol = input("length ")
testNum = input(": ")
def get_random_string(length):
    # choose from all lowercase letter
    
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
siteLst = []
b = 0
num = lol * 10
while b != int(testNum):
    b += 1
    siteLst.append("https://" + str(get_random_string(int(lol))) + ".com")

siteError = 0
# print(siteLst)
i = 0
f = open("working.txt", "w")
while i != len(siteLst) + 2:
            
            try:
                response = requests.get(siteLst[i], timeout = 1)            
                print('[' + Fore.GREEN + "+" + Fore.RESET + "] " + str(siteLst[i]) + " " + str(response.status_code) + " " + str(i) + "/" + str(testNum))
                if response.status_code >= 200 and response.status_code <= 300:
                    f.write(str(siteLst[i])+ "\n")
            except requests.exceptions.ConnectionError:
                siteError += 1            
            except IndexError:
                i = len(siteLst) + 1
            except requests.exceptions.Timeout:
                siteError += 1
            except requests.exceptions.HTTPError():
                siteError += 1
            except requests.exceptions.SSLError():
                 siteError += 1
            except requests.exceptions.RetryError():
                 siteError += 1
            except requests.exceptions.TooManyRedirects():
                 siteError += 1      


            i += 1    
print("Not Working: " + str(siteError))