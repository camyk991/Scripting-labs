$reportFile = "report-powershell.log"
$checkInterval = 30

function Generate-Report {
    param (
        [string]$message
    )
    Add-Content -Path $reportFile -Value $message
}

function Analyze-Journalctl {
    $command = "journalctl -u ssh --since '1 minute ago' --no-pager"
    $result = Invoke-Expression -Command $command

    $lines = $result -split "`n"

    foreach ($line in $lines) {
        if ($line -match "Failed password" -or $line -match "invalid") {
            Generate-Report -message "$line`n"
        }
    }
}

while ($true) {
    Analyze-Journalctl
    Start-Sleep -Seconds $checkInterval
}

