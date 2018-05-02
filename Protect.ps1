# Script to 'protect' a file, change the filename to the location of the file you wish to 'protect'.
Add-Type -AssemblyName System.Security
$filename = "C:\Users\YourUserHere\Desktop\unprotected.exe";
$bytes = [System.IO.File]::ReadAllBytes($filename);
$packed = [System.Security.Cryptography.ProtectedData]::Protect(
$bytes,
$null,
[System.Security.Cryptography.DataProtectionScope]::CurrentUser);
[IO.File]::WriteAllBytes($filename, $packed);