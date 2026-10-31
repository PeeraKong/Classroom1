# ติดตั้ง ScreenTimeGuard ให้เปิดเองทุกครั้งที่มีผู้ใช้ล็อกอิน (ต้องรันด้วยสิทธิ์ Administrator)
$ErrorActionPreference = "Stop"
$AppName = "ScreenTimeGuard"
$InstallDir = Join-Path $env:ProgramFiles $AppName
$DataDir = Join-Path $env:ProgramData $AppName

$admin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $admin) { throw "กรุณาคลิกขวาที่ install.bat แล้วเลือก 'Run as administrator'" }

$pythonw = (Get-Command pythonw.exe -ErrorAction SilentlyContinue).Source
if (-not $pythonw) { throw "ไม่พบ Python กรุณาติดตั้ง Python จาก python.org (ติ๊ก 'Add python.exe to PATH' และ 'Install for all users')" }

# 1) คัดลอกโปรแกรมไปไว้ใน Program Files (ผู้ใช้ทั่วไปแก้ไข/ลบไม่ได้)
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
Copy-Item -Force (Join-Path $PSScriptRoot "screen_time_guard.py") $InstallDir
$script = Join-Path $InstallDir "screen_time_guard.py"

# 2) โฟลเดอร์ข้อมูล: ผู้ใช้ทั่วไปอ่าน/เขียนได้ แต่ลบไฟล์ไม่ได้
New-Item -ItemType Directory -Force -Path $DataDir | Out-Null
foreach ($f in "config.json", "usage.json") {
    $p = Join-Path $DataDir $f
    if (-not (Test-Path $p)) { Set-Content -Path $p -Value "{}" -Encoding UTF8 }
}
icacls $DataDir /inheritance:r /grant:r "*S-1-5-32-544:(OI)(CI)F" "*S-1-5-18:(OI)(CI)F" "*S-1-5-32-545:(OI)(CI)(RX,W)" /T | Out-Null

# 3) ตั้งรหัสผ่านผู้ปกครองและเวลาที่อนุญาต
Write-Host "กำลังเปิดหน้าตั้งค่า กรุณาตั้งรหัสผ่านผู้ปกครอง..."
Start-Process -FilePath $pythonw -ArgumentList "`"$script`" --setup" -Wait

# 4) ให้ Task Scheduler เปิดโปรแกรมตอนล็อกอิน และเปิดซ้ำทุก 1 นาทีถ้าโดนปิด
$action = New-ScheduledTaskAction -Execute $pythonw -Argument "`"$script`""
$atLogon = New-ScheduledTaskTrigger -AtLogOn
$repeat = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1) -RepetitionDuration (New-TimeSpan -Days 3650)
$principal = New-ScheduledTaskPrincipal -GroupId "S-1-5-32-545" -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Seconds 0) -MultipleInstances IgnoreNew -StartWhenAvailable
Register-ScheduledTask -TaskName $AppName -Action $action -Trigger $atLogon, $repeat `
    -Principal $principal -Settings $settings -Force | Out-Null

Start-ScheduledTask -TaskName $AppName
Write-Host "ติดตั้งเรียบร้อย! นาฬิกานับเวลาจะขึ้นที่มุมขวาล่างของจอ" -ForegroundColor Green
