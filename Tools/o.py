# -*- coding: utf-8 -*-
#!usr/bin/python
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

Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


def zone(dom):
  page = 0
  while True:
    page += 1
    f = req.get('http://pluginu.com/domain-zone/'+dom+'/'+str(page))
    g = re.findall('<button class="btn btn-default pull-left" type="button">\n  (.*?)</button></a>', f.text)
    if g == '':
      print('EndPage')
      sys.exit()
    else:
      for domain in g:
        print('Grabbing Domain')
        save = open(dom+'.txt', 'a')
        save.write('http://'+domain+'\n')
        save.close()

def zone(dom):
  page = 0
  while True:
    page += 1
    f = req.get('http://pluginu.com/domain-zone/'+dom+'/'+str(page))
    g = re.findall('<button class="btn btn-default pull-left" type="button">\n  (.*?)</button></a>', f.text)
    if g == '':
      print('EndPage')
      sys.exit()
    else:
      for domain in g:
        print('Grabbing Domain')
        save = open('../result/domain.txt', 'a')
        save.write('http://'+domain+'\n')
        save.close()
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
print('\nDomain.txt will save in folder result'  )
tld = raw_input('{}Enter Domain Name (com,org,net) :  '.format(fw, fw, fr))
zone(tld)

