# ถอนการติดตั้ง ScreenTimeGuard (ต้องรันด้วยสิทธิ์ Administrator)
$AppName = "ScreenTimeGuard"
Unregister-ScheduledTask -TaskName $AppName -Confirm:$false -ErrorAction SilentlyContinue
Get-CimInstance Win32_Process -Filter "Name = 'pythonw.exe'" |
    Where-Object { $_.CommandLine -like "*screen_time_guard.py*" } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
Remove-Item -Recurse -Force (Join-Path $env:ProgramFiles $AppName) -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force (Join-Path $env:ProgramData $AppName) -ErrorAction SilentlyContinue
Write-Host "ถอนการติดตั้งเรียบร้อย" -ForegroundColor Green
