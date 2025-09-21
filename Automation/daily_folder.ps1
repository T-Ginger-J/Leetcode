# Base directory where everything lives
$baseDir = "C:\DailyFolders"

# Get current month name (e.g., "September") and day number (e.g., "9")
$monthName = (Get-Date -Format "MMMM")
$dayNum = [int](Get-Date -Format "dd")  # convert to int to strip leading zero

# Full path to month folder
$monthPath = Join-Path $baseDir $monthName

# Ensure month folder exists
if (!(Test-Path $monthPath)) {
    New-Item -ItemType Directory -Path $monthPath | Out-Null
    Write-Output "Created month folder: $monthPath"
}

# Full path to today's folder
$dayPath = Join-Path $monthPath $dayNum

# Ensure day folder exists
if (!(Test-Path $dayPath)) {
    New-Item -ItemType Directory -Path $dayPath | Out-Null
    Write-Output "Created day folder: $dayPath"
} else {
    Write-Output "Day folder already exists: $dayPath"
}
