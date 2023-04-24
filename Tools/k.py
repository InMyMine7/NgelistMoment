import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,colorama,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
from platform import system
colorama.init()
import os
print os.getcwd()
os.chdir('../result')

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"
RESET = "\033[0m"
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"


def getIP(site):
    
		site = i.strip()

		try:
			if 'http://' not in site:
				IP1 = socket.gethostbyname(site)
				print "IP: "+IP1
				open('../result/ips.txt', 'a').write(IP1+'\n')
			elif 'http://' in site:
				url = site.replace('http://', '').replace('https://', '').replace('/', '')
				IP2 = socket.gethostbyname(url)
				print "IP: "+IP2
				open('../result/ips.txt', 'a').write(IP2+'\n')
	
		except:
			pass
			import requests

if system() == 'Windows':

 os.system('cls')
elif system() == 'Linux':
 os.system('clear')
else:
    pass
print """
\033[91m                   
 )                                  *                                    
 ( /(              (             )   (  `                                )  
 )\()) (  (     (  )\ (       ( /(   )\))(           )      (         ( /(  
((_)\  )\))(   ))\((_))\  (   )\()) ((_)()\   (     (      ))\  (     )\()) 
 _((_)((_))\  /((_)_ ((_) )\ (_))/  (_()((_)  )\    )\  ' /((_) )\ ) (_))/  
| \| | (()(_)(_)) | | (_)((_)| |_   |  \/  | ((_) _((_)) (_))  _(_/( | |_   
\033[97m| .` |/ _` | / -_)| | | |(_-<|  _|  | |\/| |/ _ \| '  \()/ -_)| ' \))|  _|  
|_|\_|\__, | \___||_| |_|/__/ \__|  |_|  |_|\___/|_|_|_| \___||_||_|  \__|  
      |___/\033[97m
           Code By Mine7   [github.com/InMyMine7]
           Version 1.0
"""
print('\nips.txt will be save in result')
nam=raw_input('Enter List Domain :')
with open(nam) as f:
    for i in f:
        getIP(i)

		
