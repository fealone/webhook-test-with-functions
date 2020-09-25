# webhook-test-with-functions

## Deploy for GCP

```shell
poetry export -f requirements.txt > requirements.txt
gcloud functions deploy webhook-test-with-functions \
    --runtime python37 \
    --trigger-http \
    --entry-point entry_point \
    --region {region} \
    --set-env-vars PLATFORM=GCP
```

## Deploy for AWS

* Packaging

```shell
poetry export -f requirements.txt > requirements.txt
mkdir dist \
    && cp main.py dist/ \
    && pip install -r requirements.txt -t dist/ \
    && cd dist \
    && zip ../dist.zip * \
    && cd ../ \
    && rm -rf dist
```

* Deploy

```shell
aws lambda create-function \
    --function-name webhook-test-with-functions \
    --runtime python3.7 \
    --role {LambdaExecuteRole} \
    --handler entry_point \
    --zip-file fileb://dist.zip \
    --environment "Variables={PLATFORM=AWS}"
```

* Configure API Gateway
    - Supported REST API only
