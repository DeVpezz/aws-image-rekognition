import json
import boto3
import uuid

s3 = boto3.client("s3", region_name="ap-south-1")

BUCKET_NAME = "rekognition-image-labels-siddharth"

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    if "fileName" not in params:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "fileName is required"})
        }

    file_name = params["fileName"]
    object_key = f"{uuid.uuid4()}-{file_name}"

    presigned_url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": object_key
        },
        ExpiresIn=300
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "uploadUrl": presigned_url,
            "imageName": object_key
        })
    }
