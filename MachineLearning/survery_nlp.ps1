
# Create an ML Model
$uri_nlptext = 'http://localhost:8080/textbox/check'

$uri_nlptext = 'http://localhost:8080/textbox/check'
Import-csv .\SurveyData.csv|foreach-object {
    $body = @{
        text=$_.problem
    }
    $body=$body|ConvertTo-Json
    
    $response = Invoke-RestMethod -Uri $uri_nlptext -Method Post -Body $body -ContentType 'application/json' 
# $body
Add-Content wordcloud.txt $response.keywords.keyword
}
