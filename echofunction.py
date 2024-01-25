def lambda_handler(event, context):
    message = "Lambda1 says: HEllo, " + event.get("name", "Guest")
    return {
        "statusCode": 200,
        "body": message
    }
