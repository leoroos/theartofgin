import json
import datetime
from urllib import parse

base_h = {
    'Content-Type': 'application/json',
    "Access-Control-Allow-Origin": "*",
}

base_website = 'http://127.0.0.1:1337'


def handler(event, context):
    httpMethod = event['httpMethod']
    data = {
        'output': 'Http method was {}'.format(httpMethod),
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'greeting': 'From planet mars and beyond!',
    }
    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': base_h,
    }


def reviews_get(event, context):
    data = {
        'success': True,
        'message': 'Should get a whole list of shit!',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'data': [{
            'what': 'gin mare',
            'why': 'The Great Neutralizer'
        }, {
            'what': 'Monkey 47',
            'why': 'Going Apeshit!!1111'
        }]
    }
    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': base_h
    }


def reviews_post(event, context):
    params = parse.parse_qs(event['body'])
    ginName = params['ginName'][0]
    ginReview = params['ginReview'][0]
    print('Gin Name is:', ginName)
    print('Gin Review:' , ginReview)
    data = {
        'success': True,
        'message': 'Got the body:' + json.dumps(event['body']),
        'timestamp': datetime.datetime.utcnow().isoformat(),
    }
    h = base_h.copy()
    h.update({ 'Location': base_website + '/reviews.html', })
    return {
        'statusCode': 302,
        'body': json.dumps(data),
        'headers': h
    }


def options(event, context):
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Origin": "*",
        }
    }
