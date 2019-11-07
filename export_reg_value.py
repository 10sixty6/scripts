# python3 
# tbxtbxtbx
# export a registy value
# python3 export_reg_value.py -r HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run -v skype

import argparse,winreg

hivename = {'HKCU':'HKEY_CURRENT_USER', 'HKLM':'HKEY_LOCAL_MACHINE', 'HKU':'HKEY_USERS', 'HKCC':'HKEY_CURRENT_CONFIG','HKCR':'HKEY_CLASSES_ROOT'}

# argument parser stuff
parser = argparse.ArgumentParser(description='Export the value of a registry subkey by supplying the key and subkey/value')
parser.add_argument("-r", "--registry", dest="regkey", required=True, help="Registry key to search")
parser.add_argument("-v", "--value", dest="regval", required=True, help="Registry value to retrieve contents of")
args = parser.parse_args()

# set required info
regkey = args.regkey
regval = args.regval
hivesplit = regkey.split('\\',1)
shorthive = hivesplit[0].upper()
fullkey = hivesplit[1]

def hiveformat(shorthive):
	"Corrects format of hive if required"
	if "HKEY" in regkey.upper():
		return shorthive
	else:
		return hivename[shorthive]

def saveme(data):
	"Writes value of reg key to text file"
	with open('exported.txt', 'w') as f:
		f.write(str(content))
		f.close()

hive = hiveformat(shorthive)

def setcorrecthive(hive):
	"Determines correct hive and queries value of sub key"
	if hive.upper() == 'HKEY_CURRENT_USER':
		reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
		openpls = winreg.OpenKey(reg, fullkey)
		enumkeys = winreg.QueryValueEx(openpls, regval)
		return enumkeys
	elif hive.upper() == 'HKEY_LOCAL_MACHINE':
		reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
		openpls = winreg.OpenKey(reg, fullkey)
		enumkeys = winreg.QueryValueEx(openpls, regval)
		return enumkeys
	elif hive.upper() == 'HKEY_USERS':
		reg = winreg.ConnectRegistry(None, winreg.HKEY_USERS)
		openpls = winreg.OpenKey(reg, fullkey)
		enumkeys = winreg.QueryValueEx(openpls, regval)
		return enumkeys
	elif hive.upper() == 'HKEY_CURRENT_CONFIG':
		reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_CONFIG)
		openpls = winreg.OpenKey(reg, fullkey)
		enumkeys = winreg.QueryValueEx(openpls, regval)
		return enumkeys
	elif hive.upper() == 'HKEY_CLASSES_ROOT':
		reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
		openpls = winreg.OpenKey(reg, fullkey)
		enumkeys = winreg.QueryValueEx(openpls, regval)
		return enumkeys
	else:
		print("You've probably entered an invalid hive")

content = setcorrecthive(hive)[0]
print('\nData written to exported.txt')
saveme(content)