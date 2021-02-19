'Usage Set_zone.ps1 filename'
$Path_to_file = $args[0];
Set-Content -Path $Path_to_file -Stream Zone.Identifier -Value '[ZoneTransfer]','ZoneId=3'
