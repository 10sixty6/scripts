# powershell 
# tbxtbxtbx
# retrieve nanocore indicators from given PID.

<# Get NanocorePID and do initial checks #>
$NanoPID = Read-Host -Prompt 'Enter the PID of the Nanocore Process'
$NanoCheck = 
$NanoName = Get-Process -Id $NanoPID | Select-Object -ExpandProperty ProcessName
Write-Host 'Nanocore process name is:' $NanoName
$IOCSFile = "$env:USERPROFILE\Desktop\Nanocore_IOCS.txt"
$NanoStrings = "$env:USERPROFILE\Desktop\Nanocore_Strings.txt"

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

<# Dump strings of nanocore process #>
Write-Host "`nDumping strings from memory"
strings2 -pid $NanoPID > $NanoStrings

<# Find Version in dumped memory and write to file #>
Write-Host "`nSearching for C2s in memory"
$findlines = gc $NanoStrings | select-string "PrimaryConnection" -context 0,3
ac $IOCSFile "`nPotential C2s found:"; ac $IOCSFile $findlines

<# Get Guid #>
$MachGuid = Get-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Cryptography | Select-Object -ExpandProperty MachineGuid
$NanoFolder = -join ("$env:APPDATA","\","$MachGuid")
Write-Host "`nChecking for created files/folders"
ac $IOCSFile "`nFolder structure matching MachineGuid found: "
$RunTree = tree /F $NanoFolder
$RunTree | Out-File -Append $IOCSFile -Encoding UTF8

<# Get Persistence #>
ac $IOCSFile -Value "`nPossible persistence found: "
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run | Out-File -Append $IOCSFile 

<# Clean Up files/content #>
(Get-Content $IOCSFile) -replace "`0", "" | Set-Content $IOCSFile
Write-Host "`nOpening IOC file"
ri $NanoStrings
ii $IOCSFile