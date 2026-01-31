$ProjectName = "tookie-osint"
$InstallDir  = "C:\Program Files\$ProjectName"

Write-Host "[*] Uninstalling $ProjectName..."

if (-not ([Security.Principal.WindowsPrincipal]
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "[!] Run PowerShell as Administrator"
    exit 1
}

if (Test-Path $InstallDir) {
    Remove-Item -Recurse -Force $InstallDir
    Write-Host "[✓] Removed $InstallDir"
} else {
    Write-Host "[!] Not installed"
}