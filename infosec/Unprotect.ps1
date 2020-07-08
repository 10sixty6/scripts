# Script to unprotect a file, change the filename to the location of the protected file.
$filename = "C:\Users\YourUserHere\Desktop\protected.exe";
$bytes = [System.IO.File]::ReadAllBytes($filename);
$unpacked = [System.Security.Cryptography.ProtectedData]::Unprotect(
$bytes,
$null,
[System.Security.Cryptography.DataProtectionScope]::CurrentUser);
[IO.File]::WriteAllBytes($filename, $unpacked);
