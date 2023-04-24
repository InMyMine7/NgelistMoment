import os, re, sys, socket, json

import requests as req

from multiprocessing.dummy import Pool
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from colorama import *
from platform import system
init(autoreset=True)

fg = '\033[0;32m'
fr = '\033[0;31m'
fw = '\033[1;37m'
fb = '\033[0;34m'
fy = '\033[1;33m'
fre = '\033[0m'

init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
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
print("{}[{}1{}] {}Grab Website From Domain Extensions".format(fr, fw, fr, fw))
print("{}[{}2{}] {}Domain To IP".format(fr, fw, fr, fw))

tool = raw_input(fw + "\n["+fw+"-"+fw+"]Choose tool : ")

	
if tool == "1":
	os.chdir("tools/")
	os.system("python2 o.py")
	
elif tool == "2":
	os.chdir("tools/")
	os.system("python2 k.py")	

pass
print('\nHmm...\n')
