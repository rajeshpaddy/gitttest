# This script shows two level hierarychy of a manager. For an M2 manager this script shows the entire org. 
# Usage 
# Input - ShowMyOrg.ps1 <alias> <switches> 
# Output - Manager and Directs in human readable format
# <switches< - -h for human redable format -m for machine readable format

$uri=[string]::Format("http://who/Data/PersonContext/{0}.xml",$args[0])  
[System.Net.WebClient] $wc = New-Object System.Net.WebClient
$wc.UseDefaultCredentials = $true;
[boolean]$EXCEPTION_OCCURED= $false
try
{
    [xml] $doc = $wc.DownloadString($uri)
}
Catch
{
 $EXCEPTION_OCCURED = $true
 Write-Output ([string]::Format("ERROR::: {0}",$_.Exception.Message))
}

if ($EXCEPTION_OCCURED -ne $true)
{
    ForEach ($dc in $doc.GetElementsByTagName("DirectsChain"))
    {
        $host.UI.RawUI.ForegroundColor = "Blue"
        Write-Output($dc.GetElementsByTagName("Manager").GetElementsByTagName("FullName").InnerText)
        if ($dc.GetElementsByTagName("Manager").GetElementsByTagName("TotalReports").InnerText -ne 0)
        {
            foreach ($dd in $dc.GetElementsByTagName("DirectData"))
            {
                if ($dd.GetElementsByTagName("VendorWorker").InnerText -eq "false") 
                {
                    $host.UI.RawUI.ForegroundColor = "Blue"
                Write-Output("    -"+$dd.GetElementsByTagName("FullName").InnerText+"("+$dd.GetElementsByTagName("Alias").InnerText+")") 
                
                }
                else
                {
                $host.UI.RawUI.ForegroundColor = "Red"   
                Write-Output("    -"+$dd.GetElementsByTagName("FullName").InnerText+"(v-)")
                }
            }
        }
    }
}