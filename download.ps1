############################################################### 
# Powershell bulk downloader via URL.
############################################################### 
$dest = "C:\Users\REM\Desktop\Newfolder\" 
 
# Download the source list of books 
$downLoadList = "http://ligman.me/2sZVmcG" 
$bookList = Invoke-WebRequest $downLoadList 
 
# Convert the list to an array 
[string[]]$books = "" 
$books = $bookList.Content.Split("`n") 
# Remove the first line - it's not a book 
$books = $books[1..($books.Length -1)] 
$books # Here's the list 
 
# Download the books 
foreach ($book in $books) { 
    $hdr = Invoke-WebRequest $book -Method Head 
    $title = $hdr.BaseResponse.ResponseUri.Segments[-1] 
    $title = [uri]::UnescapeDataString($title) 
    $saveTo = $dest + $title 
    Invoke-WebRequest $book -OutFile $saveTo 
} 