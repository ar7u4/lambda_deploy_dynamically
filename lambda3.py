import os

def lambda_handler(event, context):
    file_path = event.get("file_path", "")
    if not file_path:
        return {
            "statusCode": 400,
            "body": "File path not provided"
        }

    try:
        with open(file_path, "r") as file:
            content = file.read()
        return {
            "statusCode": 200,
            "body": f"COntent of {file_path}:\n{content}"
        }
    except FileNotFoundError:
        return {
            "statusCode": 404,
            "body": f"File not found: {file_path}"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error reading file: {str(e)}"
        }

