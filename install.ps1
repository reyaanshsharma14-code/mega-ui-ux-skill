# Install the skill into the agents on this machine.
# Usage:  powershell -ExecutionPolicy Bypass -File install.ps1 [-Target antigravity|claude|agents|all]
param([ValidateSet('antigravity','claude','agents','all')][string]$Target = 'antigravity')

$src = Join-Path $PSScriptRoot 'skills\mega-ui-ux'
$dests = @{
  antigravity = Join-Path $env:USERPROFILE '.gemini\config\skills\mega-ui-ux'
  claude      = Join-Path $env:USERPROFILE '.claude\skills\mega-ui-ux'
  agents      = Join-Path $env:USERPROFILE '.agents\skills\mega-ui-ux'
}
$targets = if ($Target -eq 'all') { $dests.Keys } else { @($Target) }
foreach ($t in $targets) {
  $d = $dests[$t]
  if (Test-Path $d) { Remove-Item $d -Recurse -Force }
  New-Item -ItemType Directory -Force (Split-Path $d) | Out-Null
  Copy-Item $src $d -Recurse
  Write-Host "Installed to $d"
}
