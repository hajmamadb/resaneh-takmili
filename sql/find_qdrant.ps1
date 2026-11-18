Get-NetTCPConnection -LocalPort 6333 -State Listen |
  ForEach-Object {
    $c = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue
    [PSCustomObject]@{
      LocalAddress = $_.LocalAddress
      PID          = $_.OwningProcess
      Name         = if ($c) { $c.ProcessName } else { 'UNKNOWN' }
      Path         = if ($c) { $c.Path } else { '' }
      Start        = if ($c) { $c.StartTime } else { '' }
    }
  } | Format-List

Write-Host "--- all qdrant processes ---"
Get-Process -Name qdrant -ErrorAction SilentlyContinue |
  Select-Object Id, ProcessName, Path, StartTime | Format-List
