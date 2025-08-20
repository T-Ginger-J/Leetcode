# Target directory where daily folders will be created
$targetDir = "C:\Users\trent\Downloads\Leetcode\Leetcode"

# Today's date in YYMMDD format
$folderName = (Get-Date -Format "dd MM yy")

# Full path
$fullPath = Join-Path $targetDir $folderName

# Ensure target directory exists
if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir | Out-Null
}

# Create today's folder if it doesn't exist
if (!(Test-Path $fullPath)) {
    New-Item -ItemType Directory -Path $fullPath | Out-Null
    Write-Output "Created folder: $fullPath"
} else {
    Write-Output "Folder already exists: $fullPath"
}
