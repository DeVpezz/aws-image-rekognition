import json
import boto3
from urllib.parse import unquote_plus
from datetime import datetime
from decimal import Decimal

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageLabels')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    image = unquote_plus(event['Records'][0]['s3']['object']['key'])

    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': image
            }
        },
        MaxLabels=10,
        MinConfidence=70
    )

    labels = [
        {
            'Name': label['Name'],
            'Confidence': Decimal(str(round(label['Confidence'], 2)))
        }
        for label in response['Labels']
    ]

    table.put_item(
        Item={
            'imageName': image,
            'bucket': bucket,
            'labels': labels,
            'timestamp': datetime.utcnow().isoformat()
        }
    )

    print("Saved to DynamoDB:", image)

    return {
        'statusCode': 200,
        'message': 'Labels stored successfully',
        'labels': labels
    }
