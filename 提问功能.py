import os
import glob

def find_files_with_same_name_but_different_extension(directory, filename):
    base_name, _ = os.path.splitext(filename)
    pattern = os.path.join(directory, f"{base_name}.*")
    files = glob.glob(pattern)
    return [os.path.basename(f) for f in files if f != filename]

def read_all_txt_files(directory):
    content = ""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                
                # Find files with the same name but different extension
                other_files = find_files_with_same_name_but_different_extension(root, file)
                if other_files:
                    file_name_to_use = other_files[0]
                else:
                    file_name_to_use = file
                
                content += f"{os.path.join(root, file_name_to_use)}\n{file_content}\n"
    return content

def main():
    directory = "code"
    content = read_all_txt_files(directory)
    
    question = input("Please enter your question: ")
    
    import api
    api.question(content, question)

main()