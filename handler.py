import json


def hello(event, context):
    body = {'hello': 'world'}

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
