from termcolor import colored
from time import sleep
from os import system
sleep(1)
system("clear")
logo = (colored("""\t

        ███▄    █   ██████  ▄████▄   ▄▄▄       ███▄    █
         ██ ▀█   █ ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █
        ▓██  ▀█ ██▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
        ▓██▒  ▐▌██▒  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
        ▒██░   ▓██░▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
        ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
        ░ ░░   ░ ▒░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
        ░   ░ ░ ░  ░  ░  ░          ░   ▒      ░   ░ ░
         ░       ░  ░ ░            ░  ░         ░\n ""","red"))
print (logo)
sleep(1)
Nmap = ("\033[1;31;40m NOTE: If \"nmap\" tool is not installed your terminal.,\n \t\t Type \"n\" For installing\n")
print (Nmap)
sleep(2)
main = (colored("""
[1] Port Scan

[2] Version Scanning

[3] OS Detection

[4] Ping Scan

[5] Geolocation

[6] DNS loockup

[7] TCP scan

[8] UDP scan

[9] WHOIS

[10] Traceroute

[11] Aggressive Detection mode

[12] DNS bruteforcing Records

[13] ARP ping scan

[14] Brute Force Http Autentication

[15] Detecting Web applicatiin vulnerability to ShellShock

[16] Google Dorks for SQL vulnerable websites

[17] subdomain Scanner

[18] TCP SVN ping Scan

[19] Fast Scan

[20] ZoneTransfer

[21] Gather HTTP-Headers of web services

[22] Detect Heartbleed ssl vulnerability

[23] Enumerating Ethernet/IP Devices

[24] Enumerating Bacnet Devices

[25] Create a Network Topology Graph with Zenmap

[0] Exit\n""","green"))
print (main)
def Anon():
   x = input("[*] Select Option : ")
   sleep(1)
   system("clear")
   if x == "1":
      a = input(colored(" \n Website : ","green"))
      print (system("nmap " + a))
   elif x == "2":
      b = input(colored(" \n Website : ","green"))
      print (system("nmap -sV " + b))
   elif x == "3":
      c = input(colored(" \n Website : ","green"))
      sleep(1)
      print (colored("it Requires \"Root\" permission","red"))
      print (system("sudo nmap -v -Pn " + c))
   elif x == "4":
      d = input(colored(" \n Website : ","green"))
      print (system("nmap -sP " + d + " --disable-arp-ping"))
   elif x == "5":
      e = input(colored(" \n Website (or) ip address : ","green"))
      print (system("curl http://api.hackertarget.com/geoip/?q=" + e))
   elif x == "6":
      f = input(colored(" \n Website (or) ip address : ","green"))
      print (system("curl http://api.hackertarget.com/dnslookup/?q=" + f))
   elif x == "7":
      g = input(colored(" \n Website : ","green"))
      print (system("nmap -sT " + g))
   elif x == "8":
      h = input(colored(" \n Website : ","green"))
      print (colored("It Requires \"ROOT\" permission","red"))
      print (system("sudo nmap -sU " + h))
   elif x == "9":
      i = input(colored(" \n Website : ","green"))
      print (system("nmap -sn --script whois-* " + i))
   elif x == "10":
      j = input(colored(" \n Website (or) ip address : ","green"))
      print (system("curl http://api.hackertarget.com/mtr/?q=" + j))
   elif x == "11":
      k = input(colored(" \n Website : ","green"))
      print (colored("Please wait..,This scan take some time","blue"))
      print (system("nmap -A " + k))
   elif x == "12":
      l = input(colored(" \n Website : ","green"))
      print (colored("Plese Wait.., This scan take some time"))
      print (system("nmap --script dns-brute " + l))
   elif x == "13":
      m = input(colored(" \n ip Address : ","green"))
      print (system("nmap -sn -PR " + m + "/24"))
   elif x == "14":
      n = input(colored(" \n Website : ","green"))
      print (system("nmap -p80 --script http-brute " + n))
   elif x == "15":
      o = input(colored(" \n Website : ","green"))
      print (system("nmap -sV --script http-shellshock " + o))
   elif x == "16":
      print ("\033[1;31;40m•")
      sleep(1)
      p = open("Goo","r")
      print (p.read())
   elif x == "17":
      q = input(colored(" \n Website : ","green"))
      print (system("curl http://api.hackertarget.com/hostsearch/?q=" + q))
   elif x == "18":
      r = input(colored(" \n Website : ","green"))
      print (system("nmap -PS " + r))
   elif x == "19":
      s = input(colored(" \n Website : ","green"))
      print (system("nmap -F " + s))
   elif x == "20":
      t = input(colored(" \n Website : ","green"))
      print (system("curl http://api.hackertarget.com/zonetransfer/?q=" + t))
   elif x == "21":
      u = input(colored(" \n Website : ","green"))
      print (system("nmap --script=http-headers " + u))
   elif x == "22":
      v = input(colored(" \n Website : ","green"))
      print (system("nmap -sV -p 443 --script=ssl-heartbleed " + v))
   elif x == "23":
      w = input(colored(" \n Website : ","green"))
      print (colored("it Requires \"Root\" permission","red"))
      print (system("sudo nmap -Pn -sU -p44810 --script enip-info " + w))
   elif x == "24":
      y = input(colored(" \n Website : ","green"))
      print (colored("it Requires \"Root\" permission","red"))
      print (system("sudo nmap -Pn -sU -p47808 --script bacnet-info " + y))
   elif x == "25":
      z = input(colored(" \n Website : ","green"))
      print (colored("it Requires \"Root\" permission","red"))
      print (system("sudo nmap -sV --traceroute " + z))
   elif x == "n":
      print ("\033[1;31;40  Installing nmap..\\")
      sleep(1)
      print (system("pkg install nmap"))
   elif x == "0":
      exit()
   else:
      print (colored("Error","red"))
      exit()
Anon()
def Div():
    nsc = input(colored("[*] Continue [y/n] : ","green"))
    sleep(1)
    system("clear")
    if nsc == "y":
       print (logo)
       sleep(1)
       print (Nmap)
       sleep(3)
       print (main)
       Anon()
       Div()
    else:
       exit()
Div()

