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
        	input.close()
        	print('\nPotential C2 found and written to ' + filepath)
        	break

# get persistence from run key
hkcurun = "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
regkey = winreg.OpenKey(reg, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
enumkeys = winreg.EnumValue(regkey, 0)
formatpers = str(enumkeys).replace(',','\n\n') 
print('\nPossible Persistence found in: ' + hkcurun + '\n')

# save info and tidy up.
writekeyinfo = outputfile.write('\nPersistence via: \n' + hkcurun + '\n\n ' + str(formatpers))
outputfile.close()
os.remove(stringsfilepath)
os.startfile(filepath)
