import time
import requests
import pprint
from pystyle import Center, Anime, Colors, Colorate, Write, Box
import os

B   = '\033[30m'
R     = '\033[31m'
G   = '\033[32m'
Y  = '\033[33m'
B    = '\033[34m'
M = '\033[35m'
C    = '\033[36m'
W   = '\033[37m'
E   = '\033[39m'

def my_ip():
    os.system("clear")
    ip = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
    url = f"https://ipapi.co/{ip}/json/"
    r = requests.get(url)
    p = r.json()
    os.system("clear")
    Write.Print("Tracking.......",Colors.red_to_purple, interval=0.09)
    os.system("clear")
    Write.Print("Tracking.......",Colors.red_to_purple, interval=0.09)
    os.system("clear")
    Write.Print("Tracking.......",Colors.red_to_purple, interval=0.09)
    os.system("clear")
    print(B+"\nYouer IP Address \033[39m = "+G,p['ip'])
    print(B+"\nNetwork \033[39m = "+G,p['network'])
    print(B+"\nIp Version \033[39m = "+G,p['version'])
    print(B+"\nORG \033[39m = "+G,p['org'])
    print(B+"\nCountry Name \033[39m = "+G,p['country_name'])
    print(B+"\nCapital City \033[39m = "+G,p['country_capital'])
    print(B+"\nCountry Area \033[39m = "+G,p['country_area'],'km²')
    print(B+"\nCountry Population \033[39m = "+G,p['country_population'])
    print(B+"\nCountry Code \033[39m = "+G,p['country_code'])
    print(B+"\nCountry iso3 Code \033[39m = "+G,p['country_code_iso3'])
    print(B+"\nCountry Calling Code \033[39m = "+G,p['country_calling_code'])
    print(B+"\nCurrency \033[39m = "+G,p['currency'])
    print(B+"\nCurrency Name \033[39m = "+G,p['country_name'],p['currency_name'])
    print(B+"\nLanguages of The Country \033[39m = "+G,p['languages'])
    print(B+"\nTime Zone \033[39m = "+G,p['timezone'])
    print(B+"\nUTC Offset \033[39m = "+G,p['utc_offset'])
    print(B+"\nCity of The User \033[39m = "+G,p['city'])
    print(B+"\nLatitude \033[39m = "+G,p['latitude'])
    print(B+"\nLongitude \033[39m = "+G,p['longitude'])
    print(B+"\nRegion \033[39m = "+G,p['region'])
    print(B+"\nRegion Code \033[39m = "+G,p['region_code'])

def update():
    print("Updataing IP-TRACKER.....")
    os.system("bash update.sh")

def ip_track():
    os.system("clear")
    ip = input(Y+"Enter target ip \033[39m>>")
    if ip == '':
        print("Plese Input The IP Address..")
        time.sleep(3)
        return ip_track()
    url = f"https://ipapi.co/{ip}/json/"
    rb = requests.get(url)
    p = rb.json()
    os.system("clear")
    Write.Print("Tracking.......",Colors.red_to_purple, interval=0.09)
    os.system("clear")
    Write.Print("Tracking.......",Colors.red_to_purple, interval=0.09)
    os.system("clear")
    Write.Print("Tracking.......",Colors.red_to_purple, interval=0.09)
    os.system("clear")
    print(B+"\nIP Address \033[39m = "+G,p['ip'])
    print(B+"\nNetwork \033[39m = "+G,p['network'])
    print(B+"\nIp Version \033[39m = "+G,p['version'])
    print(B+"\nORG \033[39m = "+G,p['org'])
    print(B+"\nCountry Name \033[39m = "+G,p['country_name'])
    print(B+"\nCapital City \033[39m = "+G,p['country_capital'])
    print(B+"\nCountry Area \033[39m = "+G,p['country_area'],'km²')
    print(B+"\nCountry Population \033[39m = "+G,p['country_population'])
    print(B+"\nCountry Code \033[39m = "+G,p['country_code'])
    print(B+"\nCountry iso3 Code \033[39m = "+G,p['country_code_iso3'])
    print(B+"\nCountry Calling Code \033[39m = "+G,p['country_calling_code'])
    print(B+"\nCurrency \033[39m = "+G,p['currency'])
    print(B+"\nCurrency Name \033[39m = "+G,p['country_name'],p['currency_name'])
    print(B+"\nLanguages of The Country \033[39m = "+G,p['languages'])
    print(B+"\nTime Zone \033[39m = "+G,p['timezone'])
    print(B+"\nUTC Offset \033[39m = "+G,p['utc_offset'])
    print(B+"\nCity of The User \033[39m = "+G,p['city'])
    print(B+"\nLatitude \033[39m = "+G,p['latitude'])
    print(B+"\nLongitude \033[39m = "+G,p['longitude'])
    print(B+"\nRegion \033[39m = "+G,p['region'])
    print(B+"\nRegion Code \033[39m = "+G,p['region_code'])


main = r"""                                                                      
               /                                                      
    /  /#(#%@@@@@                                                     
,*@@/@@ @@ . ,/**@/                               ,* /.*  ,%* * *     
 %/@@%@@ @@   , &@@/            ,@@@@@            *# #@,  ./*(/#(#,   
  @ @@@@@**@@@@@@.*          %@/*****//(@(        %%   #(((           
   #/.,,                    @/**, @@ *(//(@       &@                  
    .                      @**,@/    .//@/(@      .#   (        .     
                         .@** .   ///////&/(@         ,,/    /.@*(    
     (                   @**. *//////////#@//@                        
                        @**///////////////////@                       
                        @*/////@////(///@/////@                       
                      @@@@//////@@@@@@@@/////@@@@                     
                    @(////&///////&@@@//////@////#@                   
                  @@///@@%///////////////#///// /((@@                 
                 @#///////@@////////////////  /(((((&@                
                   &@@@#/////////////////////((%@@@&                  
                           #@@@@&%#(((%@@@@(                          
                                                                      
                                                                      
                                                                      
                           ##/        ###  ###                        
                           ##/        ### ###                         
                           ##/        ##### (                         
                           ##/####    ###  ###                        
                                                                      
                                                                      
"""[1:]



banner = f"""
    ▀█▀ █▀▀█   ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀█ █ ▄▀ █▀▀▀ █▀▀█ 
     █  █▄▄█ ▀▀  █   █▄▄▀ █▄▄█ █    █▀▄  █▀▀▀ █▄▄▀ 
    ▄█▄ █        █   █  █ █  █ █▄▄█ █  █ █▄▄▄ █  █
        """[1:]

make="""
─══════════════════════════ቐቐ══════════════════════════─
            Tool By Ethical Hacking LK
─══════════════════════════ቐቐ══════════════════════════─

"""

menu_note =Box.DoubleCube( """  
            [01] Track IP Address
            [02] Track My IP
            [03] Auther
            [04] Update
            [05] Exit                           

""")
     
     
auther_note="""
    Auther : Ethical Hacking LK
    About : Ip Adrdess Tracking Tool
    
    """[1:]



def auther():
    Write.Print(auther_note,Colors.red_to_yellow)
    os.system("clear")
    menu()

def menu():
    Write.Print((banner), Colors.red_to_yellow, interval=0.005)
    print('')
    Write.Print(make,Colors.red_to_yellow,interval=0.005)
    print('')
    Write.Print(menu_note,Colors.red_to_purple,interval=0.005)
    lk=int(input("\n\n[\033[31m+\033[39m]\033[32m IP-TRACKER"+E+" >>"))
    if(lk==1):
        ip_track() 
    elif(lk==2):
        my_ip()
    elif(lk==3):
        auther()
    elif(lk==4):
        update()
    elif(lk==5):
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        os.system("clear")
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        os.system("clear")
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        os.system("clear")
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        exit
    else:
        print(R+"Worng Input"+E)
        return menu()


if __name__=="__main__":
    Anime.Fade(Center.Center(main), Colors.blue_to_white, Colorate.Vertical, enter=True)
    print("")
    menu()