# powershell 
# tbxtbxtbx
# retrieve nanocore indicators from given PID.

<# Get NanocorePID and do initial checks #>
$NanoPID = Read-Host -Prompt 'Enter the PID of the Nanocore Process'
$NanoName = gps -Id $NanoPID | select -ExpandProperty ProcessName
Write-Host 'Nanocore process name is:' $NanoName
$IOCSFile = "$env:USERPROFILE\Desktop\Nanocore_IOCS.txt"
$NanoStrings = "$env:USERPROFILE\Desktop\Nanocore_Strings.txt"
$NanoPath = (gps -id $NanoPID).Path

<# Create IOCs file if it doesnt already exist #>
if (!(Test-Path $IOCSFile))
{
   ni $IOCSFile -type "file" | Out-Null
   Write-Host "`nCreated new file $env:USERPROFILE\Desktop\Nanocore_IOCS.txt"
}
else
{
  Write-Host "$env:USERPROFILE\Desktop\Nanocore_IOCS.txt already exists"
}
ac $IOCSFile 'Nanocore process name is:'; ac $IOCSFile $NanoName;


<# Get hash of file #>
$NanoPath = (gps -id $NanoPID).Path
$NanoHash = (Get-FileHash -Algorithm MD5 $NanoPath).Hash
$HashFormat = -join("MD5:","$NanoHash")
ac $IOCSFile $NanoPath; ac $IOCSFile $HashFormat

<# Dump strings of nanocore process #>
Write-Host "`nDumping strings from memory"
strings2 -pid $NanoPID > $NanoStrings

<# Find Version in dumped memory and write to file #>
Write-Host "`nSearching for C2s in memory"
$findlines = gc $NanoStrings | select-string "PrimaryConnection" -context 0,3
ac $IOCSFile "`nPotential C2s found:"; ac $IOCSFile $findlines

<# Get Guid #>
$MachGuid = gp -Path HKLM:\SOFTWARE\Microsoft\Cryptography | Select-Object -ExpandProperty MachineGuid
$NanoFolder = -join ("$env:APPDATA","\","$MachGuid")
Write-Host "`nChecking for created files/folders"
if (!(Test-Path $NanoFolder))
{
	Write-Host "`nFolder structure not found"
}
else
{
	ac $IOCSFile "`nFolder structure matching MachineGuid found: "
	Write-Host "`nFolder structure matching MachineGuid found: "
	$RunTree = tree /F $NanoFolder
	$RunTree | Out-File -Append $IOCSFile -Encoding UTF8
}

<# Get Persistence #>
ac $IOCSFile -Value "`nPossible persistence found: "
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run | Out-File -Append $IOCSFile 

<# Clean Up files/content #>
(gc $IOCSFile) -replace "`0", "" | sc $IOCSFile
Write-Host "`nOpening IOC file"
ri $NanoStrings
ii $IOCSFile
