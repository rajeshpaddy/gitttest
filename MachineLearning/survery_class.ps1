
# Create an ML Model
    $model_id = 'MSSRE_BreakoutSurvey_Model_01'
    $uri_deletemodel = 'http://localhost:8080/classificationbox/models/'+$model_id
    Invoke-RestMethod -Uri  $uri_deletemodel -Method DELETE     

    $uri_createmodel = 'http://localhost:8080/classificationbox/models'
    $model = @{
        id =  $model_id
        name = 'Survey model for break out sessions'
        options = @{ 
            ngrams =  1
            skipgrams = 1
        }
        classes = @(
            'SRE_role',
            'metics_monitoring',
            'best_practices'
        )
    }
    $body = $model|ConvertTo-Json

    Invoke-RestMethod -Uri $uri_createmodel -Method Post -Body $body

# Train the model for each of the classifier
    $uri_trainmodel = 'http://localhost:8080/classificationbox/models/'+$model_id+'/teach'

    Import-csv .\TrainingData.csv|foreach-object {
        $training_payload = @{
            class =  $_.classifier
            input = @( 
                    @{ 
                    key =  'user_question'
                    type =  'text_en'
                    value = $_.trainingtext 
                    }
                )
            }

    $body = $training_payload|ConvertTo-Json
    $body
    Invoke-RestMethod -Uri $uri_trainmodel -Method Post -Body $body
    }

    ## load the training data 

    # Predict the model for each of the classifier
    $uri_predictmodel = 'http://localhost:8080/classificationbox/models/'+$model_id+'/predict'

    Import-csv .\SurveyData.csv|foreach-object {
        $prediction_payload = @{
            limit =  1
            input = @( 
                    @{ 
                    key =  'user_question'
                    type =  'text_en'
                    value = $_.Problem 
                    }
                )
            }
            
    $body = $prediction_payload|ConvertTo-Json
    # $body
    $response = Invoke-RestMethod -Uri $uri_predictmodel -Method Post -Body $body
    $response.classes.id
    if ($response.classes.id -eq "SRE_ROLE"){$SRE_ROLE++}
    if ($response.classes.id -eq "metics_monitoring"){$metics_monitoring++}
    if ($response.classes.id -eq "best_practices"){$best_practices++}
    # $max = ($response.classes|Measure-Object -Property score -Maximum  ).Maximum
    # $response.classes|Where-Object {$_.score -eq $max }
    $_.Problem 
    $SRE_ROLE
    $metics_monitoring
    $best_practices
    }

# # Load the actual data for prediction
# Import-csv .\SurveyData.csv|foreach-object { Write-Host $_.Topic  $_.
#     problem}

#Write the classified data into a new file



