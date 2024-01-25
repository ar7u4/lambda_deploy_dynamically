import os
import subprocess

def update_lambda_function(function_name, zip_file_path):
    subprocess.run(["aws", "lambda", "update-function-code",
                    "--function-name", function_name,
                    "--zip-file", "fileb://" + zip_file_path])

with open(os.environ["CHANGED_FILES_FILE"], "r") as f:
    changed_files = f.readlines()

extracted_function_names = subprocess.check_output(["git", "log", "-1", "--pretty=%s"]).decode("utf-8").split(" ")

for function_name in extracted_function_names:
    if function_name.startswith("update function:"):
        function_name = function_name[16:]  # Extract from commit message
        if any(changed_file.strip().split(".")[0] == function_name for changed_file in changed_files):
            zip_file_path = f"{function_name}.zip"
            changed_file = next(changed_file for changed_file in changed_files if function_name in changed_file)  # Find matching file
            subprocess.run(["zip", "-r", zip_file_path, changed_file])  # Create zip
            update_lambda_function(function_name, zip_file_path)  # Update function
