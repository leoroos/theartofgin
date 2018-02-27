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
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*",
            }}


def reviews(event, context):
    httpMethod = event['httpMethod']
    print(httpMethod)
    if httpMethod == 'GET':
        data = {
            'success': True,
            'message': 'Should get a whole list of shit!',
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'data': [{
                'what': 'gin mare',
                'why': 'The Great Neutralizer'
            },{
                'what': 'Monkey 47',
                'why': 'Going Apeshit!!1111'
            }
            ]
        }
    elif httpMethod == 'POST':
        data = {
            'success': True,
            'message': 'all good',
            'timestamp': datetime.datetime.utcnow().isoformat(),
        }
    else:
        data = { 'success': False, 'message': 'no data for you' }

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*",
            }}


def options(event, context):
    response = {
        'statusCode': 200,
        'headers' : {
            "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Origin": "*",
        }
    }
    return response
