# ==============================
# Tookie-OSINT Windows Installer
# ==============================

$ProjectName = "tookie-osint"
$SourceDir   = Get-Location
$InstallDir  = "C:\Program Files\$ProjectName"
$BinDir      = "C:\Program Files\$ProjectName\bin"
$Launcher    = "$BinDir\tookie-osint.ps1"
$Python      = "python"

Write-Host "[*] Installing $ProjectName..."

# Ensure admin
if (-not ([Security.Principal.WindowsPrincipal]
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "[!] Please run PowerShell as Administrator"
    exit 1
}

# Remove existing install
if (Test-Path $InstallDir) {
    Write-Host "[*] Removing existing install"
    Remove-Item -Recurse -Force $InstallDir
}

# Copy files
Write-Host "[*] Copying files to $InstallDir"
Copy-Item $SourceDir $InstallDir -Recurse -Force

# Create bin directory
New-Item -ItemType Directory -Path $BinDir | Out-Null

# Create launcher
Write-Host "[*] Creating launcher"
@"
`$ScriptDir = '$InstallDir'
`$VenvDir   = "`$ScriptDir\.venv"

if (!(Test-Path `$VenvDir)) {
    Write-Host "[*] Creating virtual environment..."
    $Python -m venv `$VenvDir
    & "`$VenvDir\Scripts\pip.exe" install --upgrade pip
    & "`$VenvDir\Scripts\pip.exe" install -r "`$ScriptDir\requirements.txt"
}

& "`$VenvDir\Scripts\python.exe" "`$ScriptDir\brib.py" `$args
"@ | Set-Content $Launcher -Encoding UTF8

# Add to PATH
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
if ($CurrentPath -notlike "*$BinDir*") {
    Write-Host "[*] Adding to system PATH"
    [Environment]::SetEnvironmentVariable(
        "Path",
        "$CurrentPath;$BinDir",
        "Machine"
    )
}

Write-Host "[✓] Installation complete!"
Write-Host "Restart your terminal, then run: tookie-osint"