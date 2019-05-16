# Python3
# Unshorten URLs to reveal destination
# https://github.com/tbxtbxtbx/

import requests
shorturl = input('\nEnter the URL to unshorten (include http:// or https:// prefix)\n')
r = requests.head(shorturl, allow_redirects=True)
print('\nThis redirects to:\n' + r.url)
secondurl = r.url
s = requests.head(secondurl, allow_redirects=True)
if s.url == r.url:
	print('\nNo further redirects observed\n')
else: 
	print(s.url)