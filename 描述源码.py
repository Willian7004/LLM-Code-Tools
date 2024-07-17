import os
import fnmatch
from api import describe

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def main():
    file_format = '*.py'  # 默认读取.py格式
    source_directory = 'code'  # 读取当前目录下的code文件夹

    for filepath in find_files(source_directory, file_format):
        with open(filepath, 'r', encoding='utf-8') as file:
            file_content = file.read()
        
        description = describe(file_content)
        
        txt_filepath = os.path.splitext(filepath)[0] + '.txt'
        with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
            txt_file.write(description)

main()