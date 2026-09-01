$ProjectName = "tookie-osint"
$InstallDir  = "C:\Program Files\$ProjectName"

Write-Host "[*] Uninstalling $ProjectName..."

$Identity  = [Security.Principal.WindowsIdentity]::GetCurrent()
$Principal = New-Object Security.Principal.WindowsPrincipal($Identity)

if (-not $Principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "[!] Run PowerShell as Administrator"
    exit 1
}

if (Test-Path $InstallDir) {
    Remove-Item -Recurse -Force $InstallDir
    Write-Host "[+] Removed $InstallDir"
} else {
    Write-Host "[!] Not installed"
}