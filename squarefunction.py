def lambda_handler(event, context):
    number = int(event.get("number", 1))
    result = number ** 17
    return {
        "statusCode": 200,
        "body": f"The square of {number} is {result}"
    }

