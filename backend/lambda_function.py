import json
import random
import uuid
import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")
table = dynamodb.Table("voiddatabase")

MESSAGES = [
    "Hello from the void.",
    "The void is listening.",
    "You have successfully invoked Lambda.",
    "Nothing here... except serverless computing."
]


def lambda_handler(event, context):
    try:
        body = event.get("body", event)

        if isinstance(body, str):
            body = json.loads(body)

        if not isinstance(body, dict):
            body = {}

        alias = str(body.get("name", "Anonymous"))[:100]
        user_message = str(body.get("message", "Hello from Void"))[:2000]

        response_message = random.choice(MESSAGES)
        item_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()

        table.put_item(
            Item={
                "ID": item_id,
                "Alias": alias,
                "UserMessage": user_message,
                "Response": response_message,
                "Timestamp": timestamp
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "status": "success",
                "id": item_id,
                "message": response_message,
                "saved": True
            })
        }

    except Exception:
        print("Error processing Void request")
        raise
