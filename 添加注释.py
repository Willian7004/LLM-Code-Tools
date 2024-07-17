import os
import re
from api import note

def read_files(directory, file_extension='.py'):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                file_paths.append(os.path.join(root, file))
    return file_paths

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    processed_content = note(content)
    match = re.search(r'```(.*?)```', processed_content, re.DOTALL)
    if match:
        extracted_content = match.group(1).strip().split('\n', 1)[1]
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(extracted_content)

def main():
    directory = 'code'
    file_extension = '.py'
    file_paths = read_files(directory, file_extension)
    for file_path in file_paths:
        process_file(file_path)

main()