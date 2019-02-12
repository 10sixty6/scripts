# Python3
# Query a hash against Virus Total.
# Add your own virustotal API key for this to work.
# https://github.com/tbxtbxtbx/

# imports
import sys, os, requests

# usage check
if len(sys.argv) < 2:
    print('Usage: python3 VirusTotal.py *hash to query*')
    sys.exit()

# main
hash_to_query = sys.argv[1]
apikey = 'your key goes here'
os.system('clear')
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print()
print('Querying hash ' + hash_to_query + ' with VirusTotal')
print()
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print()
url = 'https://www.virustotal.com/vtapi/v2/file/report?apikey=' + apikey + '&resource=' + hash_to_query
response = requests.get(url).json()
response_code = response['response_code']
if response_code == 0:
	print('\x1b[0;30;41m' + 'Hash not found on VT - exiting.' + '\x1b[0m')
	print()
	sys.exit()
detections = response['positives']
sha = response['sha256']
file_report = 'https://www.virustotal.com/#/file/' 
print('\x1b[6;30;42m' + str(detections) + ' engines found this file malicious!' + '\x1b[0m')
print()
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print()
print('View the report here:')
print()
print('\033[1m' + file_report + sha + '/detection' + '\033[0m')
print()
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print()
