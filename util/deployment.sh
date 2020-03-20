sam build &&
sam package \
    --s3-bucket lambda-src-oneid \
    --output-template-file packaged.yaml &&
sam deploy \
    --template-file packaged.yaml \
    --region us-west-2 \
    --parameter-overrides $(cat deployment-params.ini) \
    --capabilities CAPABILITY_IAM \
    --stack-name sam-app-devint &&
sam publish -t packaged.yaml --region us-west-2