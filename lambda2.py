def lambda_handler(event, context):
    number = int(event.get("number", 0))
    result = number ** 5
    return {
        "statusCode": 200,
        "body": f"The square of {number} is {result}"
    }

