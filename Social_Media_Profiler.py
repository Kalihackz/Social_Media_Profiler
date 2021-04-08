from bs4 import BeautifulSoup
import requests,os,time
from termcolor import cprint
from datetime import datetime


URL="https://www.google.com/"
FOLDER = False

def social_media(search_term,headers,site,delimiter,site_name,option):
    DORK = URL+'search?q=site:'+site+'+'+search_term
    r=requests.get(DORK,None,headers=headers)
    s=BeautifulSoup(r.text,"html.parser")
    h3s = s.find_all('h3', class_="LC20lb DKV0Md")
    if (len(h3s) != 0):
        cprint("[+] Showing "+site_name+" IDS from first page of Google ... ","yellow")
        i=1
        for h3 in h3s:
            value = h3.get_text()[0:(h3.get_text().find(delimiter)-1)]
            if h3.get_text().startswith(site_name,h3.get_text().find(delimiter)+2):
                print(i,". ",value)
                if ((option.lower() == "yes" or option.lower() == "y") and FOLDER == False):
                    with open((DIR+"/"+site_name+".txt"), 'a') as f:
                        f.write(str(i)+". "+value+"\n")
                i=i+1
    else:
        cprint("[-] Three reasons for not finding info : ","red")
        cprint("[*] No Valid Info !!!","red")
        cprint("[*] Network Error !!!","red")
        cprint("[*] Google blocking your query requests !!!","red")
    print("\n")


if __name__=="__main__":
    try:
        cprint('''   _____            _       _   __  __          _ _         _____            __ _ _           
  / ____|          (_)     | | |  \/  |        | (_)       |  __ \          / _(_) |          
 | (___   ___   ___ _  __ _| | | \  / | ___  __| |_  __ _  | |__) | __ ___ | |_ _| | ___ _ __ 
  \___ \ / _ \ / __| |/ _` | | | |\/| |/ _ \/ _` | |/ _` | |  ___/ '__/ _ \|  _| | |/ _ \ '__|
  ____) | (_) | (__| | (_| | | | |  | |  __/ (_| | | (_| | | |   | | | (_) | | | | |  __/ |   
 |_____/ \___/ \___|_|\__,_|_| |_|  |_|\___|\__,_|_|\__,_| |_|   |_|  \___/|_| |_|_|\___|_|''',"red")
        cprint("                                                                                   By Kalihackz","green")
        cprint("                                                                                   Version : Final","yellow")              
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.2171.95 Safari/537.36'}
        cprint("[+] Enter the User Name : ","green" ,end='')
        username= input()
        username = username.replace(" ","+")
        cprint("[+] Want to make a Folder of User Info ? (Yes/No) ","green" ,end='')
        option= input()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        cprint("\n[*] Started at "+dt_string,"yellow")
        if(option.lower() == "yes" or option.lower() == "y"):
            if not os.path.exists(DIR):
                DIR = os.getcwd()+"/Users/"+username.replace("+","_")
                cprint("[*] Generating Username Folder : "+DIR,"yellow")    
                os.mkdir(DIR)
            else:
                cprint("\n[-] Victim User folder already exists ! Please delete manually to get fresh stored data.","red")
                FOLDER = True
        cprint("\n[*] Searching valid Instagram , Twitter , Facebook IDs...\n","yellow")
        social_media(username,headers,"instagram.com","•","Instagram",option)
        time.sleep(3)
        social_media(username,headers,"twitter.com","|","Twitter",option)
        time.sleep(3)
        social_media(username,headers,"facebook.com","|","Facebook",option)
    except KeyboardInterrupt:
        cprint("\n[-] Program Exited!!!","red")
