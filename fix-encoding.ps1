$file = "c:\Users\pjm35\source\repos\fiction\dark-fantasy\mythara\mythara-world-bible.md"
$content = Get-Content $file -Raw -Encoding UTF8
$emdash = [char]8212

# Replace malformed em-dashes
$content = $content -replace "'€"", $emdash

# Fix spacing issues
$content = $content -replace 'peakSilk', "peak${emdash}Silk"
$content = $content -replace 'scrollsavailable', "scrolls${emdash}available"
$content = $content -replace 'holding\*require', "holding*${emdash}require"
$content = $content -replace 'healing\*available', "healing*${emdash}available"

# Save the file
$content | Set-Content -Path $file -NoNewline -Encoding UTF8

Write-Host "Successfully fixed all encoding issues!"
Write-Host "Replaced malformed characters with proper em-dashes (—)"
