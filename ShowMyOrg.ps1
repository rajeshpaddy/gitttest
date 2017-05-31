# This script shows two level hierarychy of a manager. For an M2 manager this script shows the entire org. 
# Usage 
# Input - ShowMyOrg.ps1 <alias> <switches> 
# Output - Manager and Directs in human readable format
# <switches< - -h for human redable format -m for machine readable format

$uri=[string]::Format("http://who/Data/PersonContext/{0}.xml",$args[0])  
[System.Net.WebClient] $wc = New-Object System.Net.WebClient
$switch = $args[1]
$wc.UseDefaultCredentials = $true;
[boolean]$exception_occured= $false

[string] $FTE_COLOR ="blue"
[string] $VENDOR_COLOR = "red"
[string] $DELIMITER_TOKEN =";"
[string] $VENDOR_IDENTIFIER_TOKEN="[v-]"

try
{
    [xml] $doc = $wc.DownloadString($uri)
}
Catch
{
 $exception_occured = $true
 $host.UI.RawUI.ForegroundColor = "red"
 Write-Output ([string]::Format("ERROR::: Check if  valid alias -->{0} is entered  :: {1}",$args[0],$_.Exception.Message))
}

if ($exception_occured -ne $true)
{
    if ($switch -eq "-h" -or $switch -eq $null)
    {
        ForEach ($dc in $doc.GetElementsByTagName("DirectsChain"))
        {
            if ($dc.GetElementsByTagName("Manager").GetElementsByTagName("VendorWorker").InnerText -eq "false")
            { 
                $host.UI.RawUI.ForegroundColor = $FTE_COLOR
                Write-Output($dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText +"("+$dc.GetElementsByTagName("Manager").GetElementsByTagName("Alias").InnerText+")")
            }
            else
            {
                $host.UI.RawUI.ForegroundColor = $VENDOR_COLOR
                Write-Output($dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText +"("+$dc.GetElementsByTagName("Manager").GetElementsByTagName("Alias").InnerText+")" +$VENDOR_IDENTIFIER_TOKEN)
                
            }

            if ($dc.GetElementsByTagName("Manager").GetElementsByTagName("TotalReports").InnerText -ne 0)
            {
                foreach ($dd in $dc.GetElementsByTagName("DirectData"))
                {
                    if ($dd.GetElementsByTagName("VendorWorker").InnerText -eq "false") 
                    {
                        $host.UI.RawUI.ForegroundColor = $FTE_COLOR
                    Write-Output("    -"+$dd.GetElementsByTagName("FullName").InnerText+"("+$dd.GetElementsByTagName("Alias").InnerText+")") 
                    
                    }
                    else
                    {
                    $host.UI.RawUI.ForegroundColor = $VENDOR_COLOR   
                    Write-Output("    -"+$dd.GetElementsByTagName("FullName").InnerText+"(v-)")
                    }
                }
            }
        }
    }

    if ($switch -eq "-m")
    {
        ForEach ($dc in $doc.GetElementsByTagName("DirectsChain"))
        {
            if ($dc.GetElementsByTagName("Manager").GetElementsByTagName("VendorWorker").InnerText -eq "false")
            {
                $host.UI.RawUI.ForegroundColor = $FTE_COLOR
                $lineContent= $dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText +"("+$dc.GetElementsByTagName("Manager").GetElementsByTagName("Alias").InnerText+")"
            }
            else 
            {
                $host.UI.RawUI.ForegroundColor = $VENDOR_COLOR
                $lineContent= $dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText +"("+$dc.GetElementsByTagName("Manager").GetElementsByTagName("Alias").InnerText+")" +$VENDOR_IDENTIFIER_TOKEN
            }
            if ($dc.GetElementsByTagName("Manager").GetElementsByTagName("TotalReports").InnerText -ne 0)
            {
                foreach ($dd in $dc.GetElementsByTagName("DirectData"))
                {
                    if ($dd.GetElementsByTagName("VendorWorker").InnerText -eq "false") 
                    {
                    $host.UI.RawUI.ForegroundColor = $FTE_COLOR
                    $lineContent=$lineContent+$DELIMITER_TOKEN+$dd.GetElementsByTagName("FullName").InnerText+"("+$dd.GetElementsByTagName("Alias").InnerText+")"
                    }
                    else
                    {
                    $host.UI.RawUI.ForegroundColor = $VENDOR_COLOR   
                    $lineContent = $lineContent +$DELIMITER_TOKEN+ $dd.GetElementsByTagName("FullName").InnerText+"("+$dd.GetElementsByTagName("Alias").InnerText+")"+$VENDOR_IDENTIFIER_TOKEN
                    }
                }
            }
            Write-Output ($lineContent+$DELIMITER_TOKEN)
        }
    }
}