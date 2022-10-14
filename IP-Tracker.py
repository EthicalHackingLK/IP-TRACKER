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

make=Center.XCenter(Box.Lines("Tool By Ethical Hacking LK"))

menu_note =Center.XCenter(
Box.DoubleCube( """             
                [01] Track IP Address
                [02] Track My IP
                [03] Auther
                [04] Update
                [05] Exit                               
    """))
     
     
auther_note="""
    Auther : Ethical Hacking LK
    About : Ip Adrdess Tracking Tool
    """[1:]

def update():
    print("Updataing IP-TRACKER.....")
    os.system("bash update.sh")


def auther():
    Write.Print(auther_note,Colors.red_to_yellow)
    return menu

def ip_track():
    os.system("clear")
    ip = input(Y+"Enter target ip >>"+E)
    url = f"https://ipapi.co/{ip}/json/"
    rb = requests.get(url)
    pprint.pprint(rb.json())
    os.system("clear")
    return menu()

def my_ip():
    os.system("clear")
    ip = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
    url = f"https://ipapi.co/{ip}/json/"
    r = requests.get(url)
    pprint.pprint(r.json())
    os.system("clear")
    return menu()


def menu():
    Write.Print(make,Colors.red_to_yellow,interval=0.005)
    print('')
    Write.Print(menu_note,Colors.red_to_purple,interval=0.005)
    lk=input(G+"\nIP-TRACKER >>"+E+'')
    if(lk==1 or '01'):
        ip_track() 
    elif(lk==2 or '02'):
        my_ip()
    elif(lk==3 or '03'):
        auther()
    elif(lk==4 or '04'):
        update()
    elif(lk==5 or '05'):
        print("Exiting.....")
        exit
    else:
        print(R+"Worng Input"+E)
        return menu()


if __name__=="__main__":
    Anime.Fade(Center.Center(main), Colors.blue_to_white, Colorate.Vertical, enter=True)
    Write.Print(Center.XCenter(banner), Colors.red_to_yellow, interval=0.005)
    print("")
    menu()