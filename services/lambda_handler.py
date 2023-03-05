import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        #    "body": data_dict
        "body": json.dumps("Hello CDK CI/CD Pipeline"),
        "headers": {"Content-Type": "application/json"},
    }
