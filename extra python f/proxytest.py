import requests, random

s = requests.session()
proxy = set()

with open("proxys.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())
        
        
proxies = {
    'http': 'http://'+random.choice(list(proxy))
}
 
def check_proxy():
    try:
        r = requests.get('https://youtube.com', proxies=proxies, timeout=5)
        if r.status_code == 200:
            print("YAY")
            return True
        else:
            print("BOO")
            return False
    except:
        print("BOO")
        return False       

while True:
    check_proxy()
    if check_proxy() == True:
        print("YAY")
    if check_proxy() == False:
        print("BOO")    
    
