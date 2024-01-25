import os
import subprocess

def update_lambda_function(file_path):
    function_name = os.path.splitext(os.path.basename(file_path))[0]
    zip_file_path = f'/tmp/{function_name}.zip'
    subprocess.run(['zip', '-j', zip_file_path, file_path])
    subprocess.run(['aws', 'lambda', 'update-function-code', '--function-name', function_name, '--zip-file', f'fileb://{zip_file_path}'])

def main():
    with open('changed_files.txt', 'r') as file:
        # Skip the commit message and get the list of changed files
        changed_files = [line.strip() for line in file.readlines()[1:]]

    for file_path in changed_files:
        if file_path.endswith(('.py', '.sh')):
            update_lambda_function(file_path)
            print(f'Lambda function {os.path.splitext(os.path.basename(file_path))[0]} updated successfully.')

if __name__ == "__main__":
    main()
