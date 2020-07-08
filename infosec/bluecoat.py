# Python3
# Query website category via Symantec [Bluecoat]
# https://github.com/tbxtbxtbx/

import requests, sys, os 
from bs4 import BeautifulSoup
if len(sys.argv) < 2:
	print('Usage is bluecoat.py [URL to check]')
	quit()
urltocheck = sys.argv[1]
bluecoaturl = 'http://sitereview.bluecoat.com/resource/lookup'
headers = {"Content-Type": 'application/json; charset=utf-8'}
data = {"url":urltocheck,"captcha":""}
r = requests.post(bluecoaturl, json=data, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
print(urltocheck + ' [' + soup.find('name').text + ']')
