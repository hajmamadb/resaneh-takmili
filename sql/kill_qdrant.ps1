# Kill elevated qdrant via UAC prompt
$shell = New-Object -ComObject WScript.Shell
$r = $shell.Run('taskkill /F /PID 9808', 1, $true)
Write-Host "elevated taskkill exit code: $r"
Start-Sleep 2
$p = Get-Process -Name qdrant -ErrorAction SilentlyContinue
if ($p) {
    Write-Host "STILL RUNNING: $($p.Id)"
} else {
    Write-Host "KILLED"
}
