import os
import re
import subprocess

def extract_function_name(commit_message):
    match = re.search(r'update function: (.+)', commit_message)
    return match.group(1) if match else None

def update_lambda_function(file_path, function_name):
    zip_file_path = f'/tmp/{function_name}.zip'
    subprocess.run(['zip', '-j', zip_file_path, file_path])
    subprocess.run(['aws', 'lambda', 'update-function-code', '--function-name', function_name, '--zip-file', f'fileb://{zip_file_path}'])

def main():
    with open('changed_files.txt', 'r') as file:
        # Skip the commit message and get the list of changed files
        changed_files = [line.strip() for line in file.readlines()[1:]]

    for file_path in changed_files:
        if file_path.endswith('.py') and file_path.startswith('lambda'):
            commit_message = subprocess.run(['git', 'log', '-1', '--pretty=%B'], capture_output=True, text=True).stdout.strip()
            function_name = extract_function_name(commit_message)

            if function_name:
                update_lambda_function(file_path, function_name)
                print(f'Lambda function {function_name} updated successfully.')

if __name__ == "__main__":
    main()
