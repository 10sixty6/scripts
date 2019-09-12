# python3 
# tbxtbxtbx
# retrieve adwind indicators from a given PID.

# to do - cater for multiple network/port entries in config.

import psutil,sys,os,winreg, hashlib
	
#get pid and check if its running
os.system('cls')
adwindpid = int(input('Enter the PID of the adwind process (java.exe): '))
checkpid = psutil.pid_exists(adwindpid)
if checkpid == False:
	print('PID ' + str(adwindpid) + ' does not appear to be running. Exiting.')
	sys.exit(1)

#set initial stuff up
userprofile = os.environ['USERPROFILE']
stringsfilepath = os.path.join(userprofile, 'Desktop', 'Adwind_Strings.txt')
filepath = os.path.join(userprofile, 'Desktop', 'Adwind_IOCs.txt')
outputfile = open(filepath, 'a+')

#get process name of pid/ppid
p = psutil.Process(adwindpid)
pp = p.ppid()
adwindname = p.name()
adwindcmd = p.cmdline()
fileloc = adwindcmd[2]
outputfile.write('Process name: ' + str(adwindname) + '\nCommand Line: ' + str(p.cmdline()) + '\nPayload location: ' + fileloc)
checkppid = psutil.pid_exists(pp)

#get hash of payload.
hasher = hashlib.md5()
with open(fileloc, 'rb') as hashme:
	readfile = hashme.read()
	hasher.update(readfile)
jarhash = hasher.hexdigest()
outputfile.write('\nMD5: ' + jarhash)

#check if ppid exists
if checkppid == False:
	print('\nPID ' + str(adwindpid) + ' is ' + adwindname + ' - no parent process found or no longer running: ')
else:
	nanopp = (psutil.Process(pp))
	ppname = nanopp.name()
	print('\nPID ' + str(adwindpid) + ' is ' + adwindname + ' and the PPID is: ' + str(pp) + ' - ' + str(ppname))

#dump strings of running process
print('\nDumping strings from memory to Desktop\n')
os.system('strings2 -pid ' + str(adwindpid) + ' > %userprofile%\\Desktop\\Adwind_Strings.txt')

#find config in strings, format and save.
matchconfig = '{\"NETWORK\":'
with open(stringsfilepath, "r") as input:
	for line in input:
		if matchconfig in line:
			formatconfig = line.replace(',',',\n')
			outputfile.write('\n\nFound config:\n' + formatconfig)
			print('Potential config found and written to ' + filepath)
			outputfile.close()
			break

#find persistence registry key value name & c2 info
with open(filepath, "r") as f:
	for line in f:
		if 'JAR_REGISTRY' in line:
			jarreg = line.split(":")
			regvalue = jarreg[1]
			cleanregval = (regvalue.translate({ord(i): None for i in '",\n'}))
			stripval = cleanregval.strip()
		if 'NETWORK' in line:
			rawport = line.split(":")
			portrextract = rawport[2]
			ccport = (portrextract.translate({ord(i): None for i in '",\n'}))
		if 'DNS' in line:
			rawserver = line.split(":")
			serverextract = rawserver[1]
			ccserver = (serverextract.translate({ord(i): None for i in '",\n}]'}))

#write c2 to ioc file
outputfile = open(filepath, 'a+')
writec2info = outputfile.write('\nC2 found: \n' + ccserver + ':' + ccport)

#get persistence from run key
hkcurun = "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
regkey = winreg.OpenKey(reg, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
enumkeydata = winreg.QueryValueEx(regkey, stripval)
print('\nPossible Persistence found in: ' + hkcurun + '\n')
writekeyinfo = outputfile.write('\n\nPersistence via: \n' + hkcurun + '\nValue name: ' + str(regvalue) + '\nValue data: '  + str(enumkeydata))

#clean up and open iocs file
outputfile.close()
os.remove(stringsfilepath)
os.startfile(filepath)