import os
import time
import sys


############### Banner ###############
banner2 = "\033[1;36m"+ """

        ░██████╗████████╗░█████╗░██████╗░██╗░░██╗  ░█████╗░███╗░░██╗███╗░░██╗░█████╗░███╗░░░███╗
        ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗████╗░██║████╗░██║██╔══██╗████╗░████║
        ╚█████╗░░░░██║░░░███████║██████╔╝█████═╝░  ███████║██╔██╗██║██╔██╗██║██║░░██║██╔████╔██║
        ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗██╔═██╗░  ██╔══██║██║╚████║██║╚████║██║░░██║██║╚██╔╝██║
        ██████╔╝░░░██║░░░██║░░██║██║░░██║██║░╚██╗  ██║░░██║██║░╚███║██║░╚███║╚█████╔╝██║░╚═╝░██║
        ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝ 

 """
banner1 = "\033[1;36m"+ """                                            

                ███╗░░██╗███████╗██████╗░████████╗██╗░░░██╗███╗░░██╗██╗░█████╗░
                ████╗░██║██╔════╝██╔══██╗╚══██╔══╝██║░░░██║████╗░██║██║██╔══██╗
                ██╔██╗██║█████╗░░██████╔╝░░░██║░░░██║░░░██║██╔██╗██║██║██║░░╚═╝
                ██║╚████║██╔══╝░░██╔═══╝░░░░██║░░░██║░░░██║██║╚████║██║██║░░██╗
                ██║░╚███║███████╗██║░░░░░░░░██║░░░╚██████╔╝██║░╚███║██║╚█████╔╝
                ╚═╝░░╚══╝╚══════╝╚═╝░░░░░░░░╚═╝░░░░╚═════╝░╚═╝░░╚══╝╚═╝░╚════╝░

"""
banner3 = "\033[1;36m"+ '''

                ███╗░░██╗███████╗██████╗░████████╗██╗░░░██╗███╗░░██╗██╗░█████╗░
                ████╗░██║██╔════╝██╔══██╗╚══██╔══╝██║░░░██║████╗░██║██║██╔══██╗
                ██╔██╗██║█████╗░░██████╔╝░░░██║░░░██║░░░██║██╔██╗██║██║██║░░╚═╝
                ██║╚████║██╔══╝░░██╔═══╝░░░░██║░░░██║░░░██║██║╚████║██║██║░░██╗
                ██║░╚███║███████╗██║░░░░░░░░██║░░░╚██████╔╝██║░╚███║██║╚█████╔╝
                ╚═╝░░╚══╝╚══════╝╚═╝░░░░░░░░╚═╝░░░░╚═════╝░╚═╝░░╚══╝╚═╝░╚════╝░

>>>>>>>>>>>>>>>>>>  Menu  <<<<<<<<<<<<<<<<<<

[0] | Nmap help  |  [00]  Nmap --- Scripts |   [000] Exit  |                          

[1]   Scan 1000 famous ports                    
[2]   Scan all existing ports                                       
[3]   Standard services scan                     
[4]   Aggressive service scan                                                   
[5]   Detailed Scan                            
[6]   OS scan                                   
[7]   SubRed scan                               
[8]   Scan a single port                         
[9]   Silent scan                               
[10]  Active hosts on the web + trace route     
[11]  Active hosts on a network (LH)
[12]  Identify IP
[13]  Confuse the firewall into releasing important data
[14]  Using lures
[15]  Detect Firewall
[16]  Exact Firewall Detection
[17]  Aggressive scan
[18]  Scan all ports - [TCP] 
[19]  Scan all ports - [UDP]
[20]  Send packages ICMP                                          
'''
############### Banner ###############

 # coded by  STARK ANNOM {MF LEACH WITH CREDITS}

############### Nmap code ###############



def nmap():
    os.system('clear') 
    print(banner3) 
  ######################## All optiones - Nmap ##########################
    option = input("\033[1;36m"+'Select an option\n>> ')
    if option == "1":
        os.system("clear")
        print("\033[1;36m"+ banner1)
        normal = input("\033[1;36m" + "What ip do you want to scan?\n>> " )        
        os.system("nmap --top-ports 1000 " + (normal))
        time.sleep(15)
        input('Press Any Button To Return To The Menu\n>> ') 
        nmap()

 ######################## option 2 ##########################

    elif option == "2":
        os.system("clear")
        print("\033[1;36m"+ banner1)
        psa = input("\033[1;36m" +"Introduzca una IP\n>> " "")
        os.system("nmap -p- " + (psa))
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ')
        nmap()

 ######################## option 3 ##########################

    elif option == "4":
        os.system("clear")
        print("\033[1;36m"+ banner1)
        agresivo = input("\033[1;36m" +"Enter an ip or web page ( e.j scanme.nmap.org )\n>> ")
        os.system("nmap -sV -T5"+agresivo)
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ') 
        nmap()

 ######################## option 4 ##########################

    elif option == "3":
        os.system("clear")
        print("\033[1;36m" + banner1)
        normal = input("\033[1;36m" +"Enter an ip or web page ( e.j scanme.nmap.org )\n>> ")      
        os.system("nmap -sV  "+normal)  
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ') 
        nmap()

 ######################## option 5 ##########################

    elif option == "5":
        os.system("clear")
        print("\033[1;36m" + banner1)
        s = input("\033[1;36m" +"Enter an ip \n>> ")
        os.system(f'nmap -Pn -A  {s}')
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ') 
        nmap()

 ######################## option 6 ##########################

    elif option == "6":
        os.system("clear")
        print("\033[1;36m" + banner1)
        systemx4 = input("\033[1;36m" + "Enter an ip or web page ( e.j scanme.nmap.org )\n>> ")
        os.system("nmap -O "+systemx4)
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ') 
        nmap()

 ######################## option 7 ##########################

    elif option == "7":
        os.system("clear")
        print("\033[1;36m" + banner1)
        subred = input("\033[1;36m" +"Enter an ip \n>> ")
        puertoSub = input("\033[1;36m" + "Enter a port (use below 32)\n>> ")
        os.system(f'nmap -sP {subred}/{puertoSub}')
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ') 
        nmap()

 ######################## option 8 ##########################

    elif option == "8":
        os.system("clear")
        print("\033[1;36m" + banner1)
        ip = (input("\033[1;36m" + "Enter an ip \n>> "))
        port = str(input("\033[1;36m" + "Enter the ports you are going to use \n>> "))
        os.system(f'nmap -p{port} {ip} ')
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ') 
        nmap()

 ######################## option 9 ##########################

    elif option == "9":
        os.system("clear")
        print("\033[1;36m" + banner1)
        ipyp = input("\033[1;36m" + "Enter an ip or web page ( e.j scanme.nmap.org )\n>> ")
        print("\033[1;36m" )
        os.system(f'nmap --script safe {ipyp}')
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ') 
        nmap() 

 ######################## option 10 ##########################

    elif option == "10":
        os.system("clear")
        print("\033[1;36m" + banner1)
        slut = input("\033[1;36m" +"Enter an ip or web page ( e.j scanme.nmap.org )\n>> ")
        os.system(f'nmap -sn --packet-trace --send-ip -v {slut}')
        time.sleep(15)
        input("\033[1;36m" + 'Enter an ip or web page ( e.j scanme.nmap.org )\n>> ') 
        nmap() 

 ######################## option 11 ##########################

    elif option == "11":
        os.system("clear")
        print("\033[1;36m" + banner1)
        njs = input("\033[1;36m" +"Enter an ip \n>> ")         
        os.system(f'nmap -sn -v {njs}')
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ')
        nmap()

 ######################## option 12 ##########################

    elif option == "12":
        os.system("clear")
        print("\033[1;36m" +banner1)
        ping = input("\033[1;36m" +("Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        os.system(f'ping {ping}')
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ')
        nmap()

 ######################## option 13 ##########################

    elif option == "13":
        os.system("clear")
        print("\033[1;36m" + banner1)
        ConfundirFirewall = input("\033[1;36m" + ("Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        os.system(f' nmap --mtu 24 -sV {ConfundirFirewall}')
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ')
        nmap()

 ######################## option 14 ##########################

    elif option == "14":
        os.system("clear")
        print("\033[1;36m" + banner1)
        senuelo = input("\033[1;36m" + ("Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        os.system(f'nmap -n -D 172.67.131.21,104.21.3.183 {senuelo}')
        time.sleep(15)
        input("\033[1;36m" +'Press Any Button To Return To The Menu\n>> ')
        nmap()

 ######################## option 15 ##########################

    elif option == "15":
        os.system("clear")
        print("\033[1;36m" + banner1)
        senuelo = input("\033[1;36m" +( "Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        Port = input("\033[1;36m" +  ("Enter the ports you are going to use (If you don't know which ones, try 80,443\n>> "))
        os.system(f'nmap -p{Port} --script http-waf-detect --script-args="http-waf-detect.aggro,http-waf-detect.detectBodyChanges" {senuelo}')
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ')
        nmap()

 ######################## option 16 ##########################
    elif option == "16":
        os.system("clear")
        print("\033[1;36m" + banner1)
        senuelo = input("\033[1;36m" + ( "Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        Port = input("\033[1;36m" +("Enter the ports you are going to use (If you don't know which ones, try 80,443)\n>> "))
        os.system(f"nmap -p{Port} --script http-waf-fingerprint {senuelo}")
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ')
        nmap()


 ######################## option 17 ##########################

    elif option == "17":
        os.system("clear")
        print("\033[1;36m" + banner1)
        AgresivC = input("\033[1;36m" + ("Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        os.system(f"nmap -sS -T insane {AgresivC}")
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ')
        nmap()


 ######################## option 18 ##########################

    elif option == "18": 
        os.system("clear")
        print("\033[1;36m" + banner1)
        tcpP = input("\033[1;36m" + ("Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        os.system(f"nmap -n -Pn -sS -p- {tcpP}")
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ')
        nmap()

  ######################## option 19 ##########################

    elif option == "19": 
        os.system("clear")
        print("\033[1;36m" + banner1)
        Udp = input("\033[1;36m" + ("Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        os.system(f" nmap -n -Pn -sU -p- {Udp}")
        time.sleep(15)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ')
        nmap()

  ######################## option 20 ##########################   
    
    elif option == "20":
        os.system("clear")
        print("\033[1;36m" + banner1)
        icmp = input("\033[1;36m" + ("Enter an ip or web page ( e.j scanme.nmap.org )\n>> "))
        paquetes = int(input("\033[1;36m" +("Enter the number of packages\n>>")))
        os.system(f"nping -c {paquetes} {icmp}") 
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        nmap()  

    elif option == "0":
        os.system('clear')
        print('Looking for assistance....')
        time.sleep(2)
        os.system('nmap -help')
        time.sleep(5)
        input("\033[1;36m" + 'Press Any Button To Return To The Menu\n>> ')
        nmap()
    elif option == "00":
        script()    
    elif option == "000":
        exit()    
    else: 
        print("\033[1;36m" + ("you have not put a correct option!"))
        print("\033[1;36m" + ("Returning to the Menu..."))   
        time.sleep(2)
        (nmap()) 
 ######################### Nmap-Scripts ###############################
def script():
    os.system('clear')
    banner = ("\033[1;36m"+ '''


        ░██████╗░█████╗░██████╗░██╗██████╗░████████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝
        ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░╚█████╗░
        ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░░╚═══██╗
        ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░██████╔╝
        ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░ 
                                                                                             
 [001] FTP brute force - (Script used for brute force in ftp protocol)
 [002] Safe script nmap - (Script that allows silent scanning)
 [003] heartbleed - (Script that Detects if a server is vulnerable to Heartbleed)
 [004] Dns Search - (Script used to search for subdomains)
 [005] MySql DB - (Script that allows us to search for passwords in mysql services) 
 [006] Malware - (Script to detect if a remote host has some kind of malware)
 [007] Version - (Script that extends the functionality of version detection)
 [008] Enum - (Script Enumerates the directories used in web servers)     
 [009] Vulnscan - (Script that looks for vulnerabilities Most recommended) 
 [010] For the correct operation of all the scripts execute this first   
 [000] Back to Main Menu                                                                            
    ''')
    print(banner)
    option = input("\033[1;36m"+' Select an option\n>> ')     

    if option == "001":
        print('Disclaimer: This can take a long time as it is a brute force attack ')
        time.sleep(3)
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 21)\n>> "))
        os.system(f'nmap --script ftp-brute -p 21 {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script() 

    elif option == "002":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        os.system(f'nmap -f --script safe {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()

    elif option == "003":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" +'Enter an ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 443)\n>> "))
        os.system(f'nmap -p 443 --script ssl-heartbleed {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()  

    elif option == "004":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f'nmap -p{Port} --script dns-brute {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()

    elif option == "005":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap -p{Port} --script mysql-empty-password {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()

    elif option == "006":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        os.system(f'nmap -sV --script=http-malware-host  {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()
    elif option == "007":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        os.system(f'nmap -sV --script="version,discovery"  {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()
    elif option == "008":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        os.system(f'nmap --script http-enum  {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()
    elif option == "009":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Enter an ip\n>>')
        os.system(f'nmap -sV --script=vulscan/vulscan.nse {target}')
        time.sleep(15)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()
    elif option == "010":
        os.system('clear')
        print('Installing Script please wait')
        time.sleep(1)
        os.system('git clone https://github.com/scipag/vulscan scipag_vulscan')
        time.sleep(5)
        os.system('ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan')
        time.sleep(5)
        input("\033[1;36m" + "Press Any Button To Return To The Menu\n>> ")
        script()        

    elif option == "000":
        os.system('clear')
        (nmap())
    
    else:
        print("\033[1;36m" + ("you have not put a correct option!"))
        print("\033[1;36m" + ("Returning to the Menu..."))   
        time.sleep(2)
        (script())    

 ######################## Panel de ayuda - Nmap ##########################

def exit():
    print('Coming out...... Tool By StarkAnnom')
    time.sleep(1)
    os.system("clear")
    sys.exit(1)


nmap()

