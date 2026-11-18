# Elevated kill with visible output
$shell = New-Object -ComObject WScript.Shell
$r = $shell.Run('taskkill /F /PID 9808 2>&1 > C:\qdrant_kill_out.txt', 1, $true)
Write-Host "exit code: $r"
Start-Sleep 1
if (Test-Path 'C:\qdrant_kill_out.txt') {
    Write-Host "--- elevated output ---"
    Get-Content 'C:\qdrant_kill_out.txt'
    Remove-Item 'C:\qdrant_kill_out.txt' -Force
}
# also try wmic kill elevated
$shell.Run('wmic process where ProcessId=9808 call terminate > C:\qdrant_kill_out2.txt 2>&1', 1, $true) | Out-Null
Start-Sleep 1
if (Test-Path 'C:\qdrant_kill_out2.txt') {
    Write-Host "--- wmic output ---"
    Get-Content 'C:\qdrant_kill_out2.txt'
    Remove-Item 'C:\qdrant_kill_out2.txt' -Force
}
$p = Get-Process -Name qdrant -ErrorAction SilentlyContinue
if ($p) { Write-Host "STILL RUNNING: $($p.Id)" } else { Write-Host "KILLED" }
