# Start a fresh Qdrant on port 6344 with clean storage (short ASCII paths only)
$base = 'D:\resq'
$exe = 'D:\resq\qdrant.exe'
$wd  = 'D:\resq'
$log = 'D:\resq\qdrant6344.log'

if (-not (Test-Path $exe)) {
    Copy-Item 'D:\' * -Destination $exe -ErrorAction SilentlyContinue
}
# copy exe from the real location (resolved via Get-ChildItem to avoid encoding issues)
$real = Get-ChildItem 'D:\' -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'qdrant\qdrant.exe') } | Select-Object -First 1
$srcExe = Join-Path $real.FullName 'qdrant\qdrant.exe'
Write-Host "source exe: $srcExe  exists: $(Test-Path $srcExe)"

if (-not (Test-Path 'D:\resq')) { New-Item -ItemType Directory 'D:\resq' | Out-Null }
if (-not (Test-Path 'D:\resq\storage6344')) { New-Item -ItemType Directory 'D:\resq\storage6344' | Out-Null }

$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $srcExe
$psi.WorkingDirectory = $wd
$psi.UseShellExecute = $false
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$psi.StandardOutputEncoding = [System.Text.Encoding]::UTF8
$psi.StandardErrorEncoding = [System.Text.Encoding]::UTF8
$psi.EnvironmentVariables['QDRANT__SERVICE__HTTP_PORT'] = '6344'
$psi.EnvironmentVariables['QDRANT__STORAGE__STORAGE_PATH'] = 'D:\resq\storage6344'
$psi.EnvironmentVariables['QDRANT__STORAGE__WMAP'] = 'true'

$p = [System.Diagnostics.Process]::Start($psi)
$pid6344 = $p.Id
$pid6344 | Out-File -FilePath 'D:\resq\qdrant6344.pid' -Encoding ascii
Start-Sleep 8
$alive = -not $p.HasExited
Write-Host "PID: $pid6344  alive: $alive"
if (-not $alive) {
    Write-Host "EXITED code: $($p.ExitCode)"
    try { $p.StandardOutput.ReadToEnd() } catch {}
}
exit 0
