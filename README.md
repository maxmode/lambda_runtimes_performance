
#Reproduce the test

###Preconditions

1. You have AWS account and AWS CLI is configured
1. Serverless is installed

###Steps

1. Checkout this repository
2. Run ```sls deploy```
3. Go to AWS console -> Code Build (region Ireland)
4. Create a new CodeBuild job.
    - As a source - specify this repository
    - Buildspec - specify buildspex.yml from repository
    - Environment variables: 
        - BASE_URL = {common url of your deployed APIs, should be in output on "sls deploy" command}
5. Run the job    

Test results will be in the job's output.
