# Get all subfolders in the current directory
Get-ChildItem -Directory | ForEach-Object {
    $oldName = $_.Name

    # Extract the first number (sequence of digits at the start)
    if ($oldName -match '^\d+') {
        $num = [int]$Matches[0]  # Convert to int to strip leading zeros
        $newName = $num.ToString()

        if ($oldName -ne $newName) {
            Rename-Item -Path $_.FullName -NewName $newName
            Write-Output "Renamed '$oldName' -> '$newName'"
        }
    }
}
