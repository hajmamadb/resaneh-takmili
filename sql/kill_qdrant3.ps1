# Capture the exact elevated taskkill error
$shell = New-Object -ComObject WScript.Shell
$shell.Run('cmd /c "taskkill /F /PID 9808 > C:\qk.txt 2>&1"', 1, $true) | Out-Null
Start-Sleep 1
if (Test-Path 'C:\qk.txt') {
    Write-Host "--- taskkill output (elevated) ---"
    Get-Content 'C:\qk.txt'
    Remove-Item 'C:\qk.txt' -Force
} else {
    Write-Host "no output file - UAC prompt likely declined"
}
$p = Get-Process -Name qdrant -ErrorAction SilentlyContinue
if ($p) { Write-Host "STILL RUNNING: $($p.Id)" } else { Write-Host "KILLED" }
