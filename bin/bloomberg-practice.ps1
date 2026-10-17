#
# bloomberg-practice.ps1 - Windows/PowerShell port of bin/bloomberg-practice.
#
#   bloomberg-practice create <project-name> <lang> [dir] [--force|-f]
#   bloomberg-practice list [--round <1|2>]
#
# Keep this file and bin/bloomberg-practice in sync. Run it through
# bin/bloomberg-practice.cmd so typing "bloomberg-practice" works from cmd.exe
# and PowerShell.
#
# ASCII only on purpose: Windows PowerShell 5.1 reads BOM-less scripts using
# the system ANSI code page.
#
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:UsageText = @'
Usage:
  bloomberg-practice create <project-name> <lang> [dir] [--force|-f]
  bloomberg-practice list [--round <1|2>]

Commands:
  create   Copy a practice pack into a working directory.
             <project-name>  Pack codename, e.g. marlin or meridian.
             <lang>          One of: python, cpp, java.
             [dir]           Parent directory (default: current directory); the project
                             is created in <dir>/<project-name>-<lang>.
             -f, --force     Copy into a non-empty directory, overwriting clashes.

  list     List available packs, optionally limited to one round.

Examples:
  bloomberg-practice create marlin python
  bloomberg-practice create meridian cpp ~/practice
  bloomberg-practice create harbor java ~/practice --force
  bloomberg-practice list
  bloomberg-practice list --round 2
'@

function Write-Usage {
    param([switch]$ToError)

    if ($ToError) {
        [Console]::Error.WriteLine($script:UsageText)
    } else {
        [Console]::Out.WriteLine($script:UsageText)
    }
}

function Die {
    param([string]$Message)

    [Console]::Error.WriteLine("bloomberg-practice: $Message")
    exit 1
}

function Resolve-RepoRoot {
    if ($env:BLOOMBERG_PRACTICE_ROOT) {
        if (-not (Test-Path -LiteralPath $env:BLOOMBERG_PRACTICE_ROOT -PathType Container)) {
            Die "BLOOMBERG_PRACTICE_ROOT is not a directory: $env:BLOOMBERG_PRACTICE_ROOT"
        }
        return (Resolve-Path -LiteralPath $env:BLOOMBERG_PRACTICE_ROOT).Path
    }

    if (-not $PSScriptRoot) {
        Die "cannot determine the script directory"
    }
    $binDir = (Resolve-Path -LiteralPath $PSScriptRoot).Path
    return (Split-Path -Parent $binDir)
}

function Expand-Destination {
    param([string]$Path)

    if ($Path -eq '~') {
        return $HOME
    }
    if ($Path.StartsWith('~/') -or $Path.StartsWith('~\')) {
        return (Join-Path $HOME $Path.Substring(2))
    }
    return $Path
}

function Find-Pack {
    param([string]$Name)

    if ([string]::IsNullOrEmpty($Name) -or $Name -eq '.' -or $Name -eq '..') {
        Die "invalid project name: $Name"
    }
    if ($Name -notmatch '^[A-Za-z0-9._-]+$') {
        Die "invalid project name: $Name"
    }

    $found = ''
    foreach ($round in @('round-1', 'round-2')) {
        $candidate = Join-Path (Join-Path $script:RepoRoot $round) $Name
        if (Test-Path -LiteralPath $candidate -PathType Container) {
            if ($found) {
                Die "project '$Name' exists in both rounds; codenames must be unique"
            }
            $found = $round
        }
    }

    if (-not $found) {
        Die "unknown project: $Name (run 'bloomberg-practice list' to see the packs)"
    }
    return $found
}

function Get-Domain {
    param([string]$Round, [string]$Name)

    $readme = Join-Path $script:RepoRoot 'README.md'
    if (-not (Test-Path -LiteralPath $readme -PathType Leaf)) {
        return ''
    }

    $needle = "[$Name]($Round/$Name)"
    $line = Get-Content -LiteralPath $readme -Encoding UTF8 |
        Where-Object { $_.Contains($needle) } |
        Select-Object -First 1
    if (-not $line) {
        return ''
    }

    $parts = $line -split '\|'
    if ($parts.Count -lt 3) {
        return ''
    }
    return $parts[2].Trim()
}

function Invoke-Create {
    param([string[]]$Arguments)

    if ($null -eq $Arguments) {
        $Arguments = @()
    }

    $force = $false
    $endOfOptions = $false
    $pos = New-Object 'System.Collections.Generic.List[string]'

    for ($i = 0; $i -lt $Arguments.Count; $i++) {
        $arg = $Arguments[$i]
        if ($endOfOptions) {
            $pos.Add($arg)
            continue
        }
        switch -CaseSensitive ($arg) {
            '-f' { $force = $true }
            '--force' { $force = $true }
            '-h' { Write-Usage; exit 0 }
            '--help' { Write-Usage; exit 0 }
            '--' { $endOfOptions = $true }
            default {
                if ($arg -clike '-*') {
                    Die "unknown option for create: $arg"
                }
                $pos.Add($arg)
            }
        }
    }

    if ($pos.Count -lt 2) {
        Write-Usage -ToError
        Die "create needs <project-name> and <lang>"
    }
    if ($pos.Count -gt 3) {
        Die "too many arguments: $(@($pos) -join ' ')"
    }

    $name = $pos[0]
    $lang = $pos[1]
    if ($pos.Count -ge 3) {
        $dest = Expand-Destination -Path $pos[2]
    } else {
        $dest = '.'
    }

    if (@('python', 'cpp', 'java') -cnotcontains $lang) {
        Die "unsupported language: $lang (choose python, cpp, or java)"
    }

    $round = Find-Pack $name
    $pack = Join-Path (Join-Path $script:RepoRoot $round) $name

    if (Test-Path -LiteralPath $dest) {
        if (-not (Test-Path -LiteralPath $dest -PathType Container)) {
            Die "destination exists and is not a directory: $dest"
        }
    }

    $target = Join-Path $dest "$name-$lang"
    if (Test-Path -LiteralPath $target) {
        if (-not (Test-Path -LiteralPath $target -PathType Container)) {
            Die "project path exists and is not a directory: $target"
        }
    }

    $targetIsDir = Test-Path -LiteralPath $target -PathType Container
    if ($targetIsDir) {
        $entries = @(Get-ChildItem -LiteralPath $target -Force)
        if ($entries.Count -gt 0 -and -not $force) {
            Die "project directory is not empty: $target (use --force to copy anyway)"
        }
    }

    [System.IO.Directory]::CreateDirectory($target) | Out-Null

    $docs = @(Get-ChildItem -LiteralPath $pack -File -Force |
        Where-Object { $_.Extension -ceq '.md' -and $_.Name -ne 'SETUP.md' } |
        Sort-Object Name)
    foreach ($doc in $docs) {
        Copy-Item -LiteralPath $doc.FullName -Destination (Join-Path $target $doc.Name) -Force
    }

    $tickets = Join-Path $pack 'tickets'
    $hasTickets = Test-Path -LiteralPath $tickets -PathType Container
    if ($hasTickets) {
        $ticketsDest = Join-Path $target 'tickets'
        [System.IO.Directory]::CreateDirectory($ticketsDest) | Out-Null
        Get-ChildItem -LiteralPath $tickets -Force | ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination $ticketsDest -Recurse -Force
        }
    }

    $langSrc = Join-Path $pack $lang
    Get-ChildItem -LiteralPath $langSrc -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force
    }

    $absDest = (Resolve-Path -LiteralPath $target).Path
    $roundNum = $round.Substring($round.Length - 1)
    [Console]::Out.WriteLine("Created $name (round $roundNum, $lang) in $absDest")

    $docNames = @($docs | ForEach-Object { $_.Name })
    if ($hasTickets) {
        $docNames += 'tickets/'
    }
    [Console]::Out.WriteLine("  documents: $($docNames -join ', ')")
    [Console]::Out.WriteLine("  code:      $lang files in project root")
    [Console]::Out.WriteLine('Next: read the documents, then write a test that reproduces a reported problem.')
}

function Invoke-List {
    param([string[]]$Arguments)

    if ($null -eq $Arguments) {
        $Arguments = @()
    }

    $roundFilter = ''
    for ($i = 0; $i -lt $Arguments.Count; $i++) {
        $arg = $Arguments[$i]
        switch -CaseSensitive ($arg) {
            '--round' {
                if ($i + 1 -ge $Arguments.Count) {
                    Die "$arg needs a value (1 or 2)"
                }
                $i++
                $roundFilter = $Arguments[$i]
            }
            '-r' {
                if ($i + 1 -ge $Arguments.Count) {
                    Die "$arg needs a value (1 or 2)"
                }
                $i++
                $roundFilter = $Arguments[$i]
            }
            '-h' { Write-Usage; exit 0 }
            '--help' { Write-Usage; exit 0 }
            default {
                if ($arg.StartsWith('--round=')) {
                    $roundFilter = $arg.Substring(8)
                } elseif ($arg -clike '-*') {
                    Die "unknown option for list: $arg"
                } else {
                    Die "unexpected argument for list: $arg"
                }
            }
        }
    }

    switch -CaseSensitive ($roundFilter) {
        '' { }
        '1' { $roundFilter = '1' }
        'round-1' { $roundFilter = '1' }
        '2' { $roundFilter = '2' }
        'round-2' { $roundFilter = '2' }
        default { Die "invalid round: $roundFilter (choose 1 or 2)" }
    }

    $total = 0
    foreach ($round in @('round-1', 'round-2')) {
        $num = $round.Substring($round.Length - 1)
        if ($roundFilter -and $roundFilter -ne $num) {
            continue
        }

        $roundDir = Join-Path $script:RepoRoot $round
        $packs = @(Get-ChildItem -LiteralPath $roundDir -Directory -Force | Sort-Object Name)
        if ($packs.Count -eq 0) {
            continue
        }

        [Console]::Out.WriteLine("Round $num ($($packs.Count) projects)")
        foreach ($packDir in $packs) {
            $packName = $packDir.Name
            $domain = Get-Domain -Round $round -Name $packName
            if ($domain) {
                [Console]::Out.WriteLine(("  {0,-12} {1}" -f $packName, $domain))
            } else {
                [Console]::Out.WriteLine("  $packName")
            }
            $total++
        }
        if (-not $roundFilter) {
            [Console]::Out.WriteLine('')
        }
    }

    if ($total -eq 0) {
        Die "no projects found"
    }
}

$script:RepoRoot = Resolve-RepoRoot
$round1 = Join-Path $script:RepoRoot 'round-1'
$round2 = Join-Path $script:RepoRoot 'round-2'
if (-not (Test-Path -LiteralPath $round1 -PathType Container) -or
    -not (Test-Path -LiteralPath $round2 -PathType Container)) {
    Die "cannot find the practice packs under $script:RepoRoot (set BLOOMBERG_PRACTICE_ROOT)"
}

$scriptArgs = @($args)
if ($scriptArgs.Count -eq 0) {
    Write-Usage -ToError
    exit 1
}

$command = $scriptArgs[0]
$rest = @()
if ($scriptArgs.Count -gt 1) {
    $rest = @($scriptArgs | Select-Object -Skip 1)
}

switch -CaseSensitive ($command) {
    'create' { Invoke-Create -Arguments $rest }
    'list' { Invoke-List -Arguments $rest }
    '-h' { Write-Usage }
    '--help' { Write-Usage }
    'help' { Write-Usage }
    default { Die "unknown command: $command (try 'bloomberg-practice --help')" }
}
