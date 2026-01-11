import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageLabels')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body, cls=DecimalEncoder)
    }

def lambda_handler(event, context):
    params = event.get("queryStringParameters")

    if not params or "imageName" not in params:
        return response(400, {
            "error": "imageName query parameter required"
        })

    image_name = params["imageName"]

    try:
        db_response = table.get_item(
            Key={"imageName": image_name}
        )
    except Exception as e:
        return response(500, {
            "error": "DynamoDB error",
            "details": str(e)
        })

    if "Item" not in db_response:
        # IMPORTANT: polling expects this
        return response(404, {
            "message": "Labels not ready yet"
        })

    return response(200, db_response["Item"])
