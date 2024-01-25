def lambda_handler(event, context):
    message = "Lambda1 says: Hello, " + event.get("name", "Guest")
    return {
        "statusCode": 200,
        "body": message
    }
