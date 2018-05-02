$EncodedText = “SGVsbG8gd29ybGQgdGhpcyBpcyBtZXJlbHkgYSB0ZXN0IHBhcmFncmFwaCB0byBlbnN1cmUgdGhhdCBteSBiYXNlNjQgZGVjb2Rpbmcgcm91dGluZSBpbiBwb3dlcnNoZWxsIHdvcmtzIHByb3Blcmx5LiBJdCBiZXR0ZXIgaGFkIGRvLg==”
$DecodedText = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($EncodedText))
echo $DecodedText