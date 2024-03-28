import random
import string
import requests

def get_header():
    headers = []
    try:
     with open("proxys/headers.txt") as h:
        for line in h:
            headers.append(line.strip())
     return headers
    except Exception:
       print("Problem With User Agents. Please Download The User Agent File!")
       exit(1)
    

def replace_all_placeholders(url_pattern, i):
    """
    Replace all placeholders in the URL pattern with appropriate values.
    """
    # Replace {i} with the generated number
    url_pattern = url_pattern.replace('{i}', str(i))
    
    # Generate random text for {t}
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    url_pattern = url_pattern.replace('{t}', random_text)

    return url_pattern


print("""
         Tip! This Plugin Is Still In Beta.
         [1] Facebook ID
         [2] Twitter Handle
         [3] Reddit Username
         [9] Other Site With Number  
      """)
uname = input("What Do You Want To Brute? ")

if uname == "1":
    url_pattern = input("Enter the Facebook URL (e.g., https://www.facebook.com/profile.php?id={i}): ")
    num = input("Facebook ID to start at: ")
    i = int(num)
    while True:
        randomheaders = get_header()
        header = {"User-Agent": str(random.choice(randomheaders))}
    # Format the URL with the generated number
    
        req = requests.get(url_pattern + str(i),headers=header)
        if req.status_code == 200:
            print(url_pattern + " Site Is Valid" )
        i += 1

if uname == "2":
    url_pattern = input("Enter the Twitter URL (e.g., https://twitter.com/{t}): ")
    while True:
        randomheaders = get_header()
        header = {"User-Agent": str(random.choice(randomheaders))}
    # Format the URL with the generated number
        url = replace_all_placeholders(url_pattern, 10)
        req = requests.get(url,headers=header)
        if req.status_code == 200:
            print(url + " Site Is Valid" )
        else:
            print(url + " Site Is Invalid " + str(req.status_code))

if uname == "3":
    url_pattern = input("Enter the Reddit URL (e.g., https://www.reddit.com/user/{t}): ")
    while True:
        randomheaders = get_header()
        header = {"User-Agent": str(random.choice(randomheaders))}
    # Format the URL with the generated number
        url = replace_all_placeholders(url_pattern, 10)
        req = requests.get(url,headers=header)
        if req.status_code == 200:
            print(url + " Site Is Valid" )
        else:
            print(url + " Site Is Invalid " + str(req.status_code))

if uname == "9":

 # Get the URL pattern from the user
 url_pattern = input("Enter the URL pattern with '{i}' as a placeholder for numbers and '{t}' for text (e.g., https://www.facebook.com/profile.php?id={i}): ")
 num = input("ID to start at: ")
 i = int(num)
 while True:
    randomheaders = get_header()
    header = {"User-Agent": str(random.choice(randomheaders))}
    # Format the URL with the generated number
    url = replace_all_placeholders(url_pattern, i)
    req = requests.get(url,headers=header)
    if req.status_code == 200:
        print(url + " Site Is Valid ")
    else:
       print(url + " Site Invalid ") 
    i += 1

