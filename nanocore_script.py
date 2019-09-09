# python3 
# tbxtbxtbx
# retrieve nanocore indicators from given PID.

import psutil,sys,os,winreg
# get pid and check if its running
os.system('cls')
nanopid = int(input('Enter the PID of the Nanocore process: '))	
checkpid = psutil.pid_exists(nanopid)
if checkpid == False:
	print('PID ' + str(nanopid) + ' does not appear to be running. Exiting.')
	sys.exit(1)

#set initial stuff up
userprofile = os.environ['USERPROFILE']
stringsfilepath = os.path.join(userprofile, 'Desktop', 'Nanocore_Strings.txt')
filepath = os.path.join(userprofile, 'Desktop', 'Nanocore_IOCs.txt')
outputfile = open(filepath, 'a+')

#get process name of pid/ppid
p = psutil.Process(nanopid)
pp = p.ppid()
nanoname = p.name()
checkppid = psutil.pid_exists(pp)

#check if ppid exists
if checkppid == False:
	print('\nPID ' + str(nanopid) + ' is ' + nanoname + ' - no parent process found or no longer running: ')
else:
	nanopp = (psutil.Process(pp))
	ppname = nanopp.name()
	print('\nPID ' + str(nanopid) + ' is ' + nanoname + ' and the PPID is: ' + str(pp) + ' - ' + str(ppname))

# dump strings of running process
print('\nDumping strings from memory to Desktop\n')
os.system('strings2 -pid ' + str(nanopid) + ' > %userprofile%\\Desktop\\Nanocore_Strings.txt')

#find hosts in dumped memory & write to file:
matchversion = 'Nanocore Client, Version='
with open(stringsfilepath, "r") as input:
	for line in input:
		if matchversion in line:
			outputfile.write('\nNanocore version found:\n' + line)
			outputfile.write(next(input))
			print('\nNanocore version found & written to: ' + filepath)
			input.close()
			break

#find c2 in memory and write to file
matchstringcc = 'PrimaryConnectionHost'
with open(stringsfilepath, "r") as input:
    for line in input:
        if matchstringcc in line:
        	outputfile.write('Found potential C2:\n' + line)
        	outputfile.write(next(input))
        	outputfile.write(next(input))
        	outputfile.write(next(input))
        	print('\nPotential C2 found and written to ' + filepath)
        	break

#get machine guid
guidregfull = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\MachineGuid'
guidreg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
guidkey = winreg.OpenKey(guidreg, r"SOFTWARE\\Microsoft\\Cryptography\\", access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
rawmachguid = winreg.QueryValueEx(guidkey, "MachineGuid")
firstguid = str(rawmachguid[0])
winreg.CloseKey(guidreg)

# check for existence of appdata guid folder & save to file
appdatapath = os.environ['APPDATA']
guidpath = os.path.join(appdatapath, firstguid)
print('\n\nChecking for created files in : ' + guidpath)

# recursive folder contents thanks to https://stackoverflow.com/users/1226857/dhobbs
if os.path.exists(guidpath) == False:
	print('MachineGuid Folder Path doesnt exist.. \n')
else:
	outputfile.write('\n\nFound folder structure: ' + guidpath + '\n\n' + 'Contents below:\n')
	for root, dirs, files in os.walk(guidpath):
		level = root.replace(guidpath, '').count(os.sep)
		indent = ' ' * 2 * (level)
		outputfile.write('{}{}'.format(indent, os.path.basename(root) + ':\n'))
		subindent = ' ' * 2 * (level + 1)
		for f in files:
			outputfile.write('{}{}'.format(subindent, f) + '\n')

# get persistence from run key
hkcurun = "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
regkey = winreg.OpenKey(reg, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
enumkeys = winreg.EnumValue(regkey, 0)
print('\nPossible Persistence found in: ' + hkcurun + '\n')

# save info and tidy up.
outputfile = open(filepath, 'a+')
writekeyinfo = outputfile.write('\n\nPersistence via: \n' + hkcurun + '\n\nValue name: ' + str(enumkeys[0]) + '\nValue data: '  + str(enumkeys[1]))
outputfile.close()
os.remove(stringsfilepath)
os.startfile(filepath)
