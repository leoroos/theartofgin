import json
import datetime


def handler(event, context):
    httpMethod = event['httpMethod']
    data = {
        'output': 'Http method was {}'.format(httpMethod),
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'greeting': 'From planet mars and beyond!',
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}


def post_gin_review(event, context):
    print(json.dumps(event, indent=4))
    print(event['body'])
    data = {
        'output': json.dumps(event),
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'greeting': 'Answer to gin review',
    }
    return {'statusCode': 200,
            'headers': {'Content-Type': 'application/json'}}
