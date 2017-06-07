# This script shows two level hierarychy of a manager. For an M2 manager this script shows the entire org. 
# Usage 
# Input - ShowMyOrg.ps1 <alias> <switches> 
# Output - Manager and Directs in human readable format
# <switches< - -h for human redable format -m for machine readable format
# list of foreground colors are available in https://technet.microsoft.com/en-us/library/ff406264.aspx
$uri=[string]::Format("http://who/Data/PersonContext/{0}.xml",$args[0] )
[System.Net.WebClient] $wc = New-Object System.Net.WebClient
$switch = $args[1]
$wc.UseDefaultCredentials = $true;
[boolean]$exception_occured= $false
[string] $FTE_COLOR ="cyan"
[string] $VENDOR_COLOR = "Yellow"
[string] $SUMMARY_COLOR = "Green"
[string] $DELIMITER_TOKEN =";"
[string] $VENDOR_IDENTIFIER_TOKEN="[v-]"
[string] $DEFAULT_FOREGROUND_COLOR = $host.UI.RawUI.ForegroundColor
[int] $vendor_count=0
[int] $FTE_count=0
[int] $OPEN_count=0
try
{
    [xml] $doc = $wc.DownloadString($uri)
}
Catch
{
    $exception_occured = $true
    $host.UI.RawUI.ForegroundColor = "red"
    Write-Output ([string]::Format("ERROR::: Check if  valid alias -->{0} is entered :: {1}",$args[0],$_.Exception.Message))
}

if ([string]::IsNullOrEmpty($switch))
{
    Write-Output ("NAME")
    Write-Output ("`t ShowMyOrg")
    Write-Output ("SYNTAX")
    Write-Output ("`t ShowMyOrg [Alias] <string> [Switches: -h human readable, -m machine readable -s single person information] ")
    Write-Output ("`t Examples: ")
    Write-Output ("`t `t 1) ShowMyOrg Toddba -h --> Shows human readable org of Toddba and his directs")
    Write-Output ("`t `t 2) ShowMyOrg Toddba -m --> Shows machine readable org of Toddba and his directs")
    Write-Output ("`t `t 3) ShowMyOrg Toddba -s --> Shows information for Toddba")
    Write-Output ("`t `t 4) ShowMyOrg Toddba    --> Shows machine readable org of Toddba and his directs")
    Write-Output ("`t `t 5) ShowMyOrg Toddba    --> Shows usage of this command") 
    exit
}
if ($switch -eq "-s")
{
    $person = $doc.GetElementsByTagName("Person")[0]
    Write-Output([string]::Format("Name - {0}",$person.Name))
    Write-Output([string]::Format("Alias  - {0}",$person.Alias))
    Write-Output([string]::Format("Office - {0}",$person.Office))
    Write-Output([string]::Format("Department - {0}",$person.Department))
    Write-Output([string]::Format("ManagerFullName - {0}",$person.ManagerFullName))
    Write-Output([string]::Format("FullTimeReports - {0}",$person.FullTimeReports))
    Write-Output([string]::Format("ImageLink - {0}",$person.ImageLink))
    exit
}
if ($exception_occured -eq $false)
{   
    ForEach ($dc in $doc.GetElementsByTagName("DirectsChain"))
    {
        #for manager
        if ($dc.GetElementsByTagName("Manager").GetElementsByTagName("VendorWorker").InnerText -eq "false")
        {
            $host.UI.RawUI.ForegroundColor = $FTE_COLOR
            $lineContent= $dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText +"("+$dc.GetElementsByTagName("Manager").GetElementsByTagName("Alias").InnerText+")"
            if ($switch -eq "-h")
            {
                Write-Output ($lineContent)
            }
            if (($dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText -like "*OPEN*"))
            {
                $OPEN_count++
            }
            else
            {
                $FTE_count++
            }
        }
        else 
        {
            $host.UI.RawUI.ForegroundColor = $VENDOR_COLOR
            $lineContent= $dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText +"("+$dc.GetElementsByTagName("Manager").GetElementsByTagName("Alias").InnerText+")" +$VENDOR_IDENTIFIER_TOKEN
            $vendor_count++
            if ($switch -eq "-h")
            {
                Write-Output ($lineContent)
            }
        }
        #for directs
        if ($dc.GetElementsByTagName("Manager").GetElementsByTagName("TotalReports").InnerText -ne 0)
        {
            foreach ($dd in $dc.GetElementsByTagName("DirectData"))
            {
                if ($dd.GetElementsByTagName("VendorWorker").InnerText -eq "false") 
                {
                    $host.UI.RawUI.ForegroundColor = $FTE_COLOR
                    $currentLineContent=$dd.GetElementsByTagName("FullName").InnerText+"("+$dd.GetElementsByTagName("Alias").InnerText+")"
                    $lineContent=$lineContent+$DELIMITER_TOKEN+$currentLineContent     
                    if ($switch -eq "-h")
                    {
                        Write-Output ("    -"+$currentLineContent)
                    }
                    if (($dd.GetElementsByTagName("FullName").InnerText -like "*OPEN*"))
                    {
                        $OPEN_count++
                    }
                    else
                    {
                        $FTE_count++
                    }
                }
                else
                {
                    $host.UI.RawUI.ForegroundColor = $VENDOR_COLOR   
                    $currentLineContent = $dd.GetElementsByTagName("FullName").InnerText+"("+$dd.GetElementsByTagName("Alias").InnerText+")"+$VENDOR_IDENTIFIER_TOKEN
                    $lineContent = $lineContent +$DELIMITER_TOKEN+ $currentLineContent
                    $vendor_count++
                    if ($switch -eq "-h")
                    {
                        Write-Output ("    -"+$currentLineContent)
                    }
                }
            }
        }
        if ($switch -eq "-m" -or $switch -eq $null)
        {
            Write-Output ($lineContent+$DELIMITER_TOKEN)
        }
    }
}
$host.UI.RawUI.ForegroundColor = $SUMMARY_COLOR
Write-Output ("--------------------------------------------------------------------")
$host.UI.RawUI.ForegroundColor = $FTE_COLOR
Write-Output ([string]::Format("Total FTE - {0}",$FTE_count))
Write-Output ([string]::Format("Total OPEN - {0}",$OPEN_count))
$host.UI.RawUI.ForegroundColor = $VENDOR_COLOR   
Write-Output ([string]::Format("Total Vendor - {0}",$vendor_count))
$host.UI.RawUI.ForegroundColor = $DEFAULT_FOREGROUND_COLOR