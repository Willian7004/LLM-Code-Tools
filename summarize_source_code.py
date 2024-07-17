import os
import glob
import api

def find_matching_file(path, extensions):
    dir_name = os.path.dirname(path)
    base_name = os.path.basename(path)
    name_without_ext = os.path.splitext(base_name)[0]
    
    for ext in extensions:
        matching_file = os.path.join(dir_name, f"{name_without_ext}{ext}")
        if os.path.exists(matching_file):
            return matching_file
    return path

def read_files_in_directory(directory):
    txt_files = glob.glob(os.path.join(directory, '**', '*.txt'), recursive=True)
    content = ""
    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as file:
            file_content = file.read()
        
        matching_file = find_matching_file(txt_file, ['.py', '.md', '.csv'])
        content += f"{matching_file}\n{file_content}\n"
    
    return content

def main():
    directory = 'code'
    content = read_files_in_directory(directory)
    
    # Assuming api.summarize() is a function that takes a string and returns a string
    import api_en
    result = api_en.summarize(content)
    
    with open('sum.txt', 'w', encoding='utf-8') as file:
        file.write(result)

main()