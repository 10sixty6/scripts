$EncodedText = “SGVsbG8gV29ybGQh”
$DecodedText = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($EncodedText))
echo $DecodedText
