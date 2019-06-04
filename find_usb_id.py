# python 3
# https://github.com/tbxtbxtbx/
# query usb ids to map to manufacturer - HKLM:\SYSTEM\ControlSet001\Enum\USB

import requests, os 
from bs4 import BeautifulSoup
os.system('clear')
vendorid = input('\nEnter the Vendor ID: \n')
baseurl = 'https://www.the-sz.com/products/usbid/index.php?v=0x' + vendorid + '&p=&n='
response = requests.get(baseurl)
soup = BeautifulSoup(response.text, 'html.parser')
findvendor = soup.find_all('div', attrs={'class' : 'usbid-vendor-name'})[1:2]
for data in findvendor:
    for a in data.find_all('a'):
        print(vendorid + ' is ' + a.text) 