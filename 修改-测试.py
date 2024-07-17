import os
import subprocess
import re

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def extract_code_from_markdown(text):
    match = re.search(r'```(.*?)\n(.*?)```', text, re.DOTALL)
    if match:
        return match.group(2).strip()
    return ""

def run_code(filename):
    try:
        result = subprocess.run(['python', filename], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

def main():
    text = input("请输入内容: ").strip()
    if not text:
        text = read_file('question.txt')
        if not text:
            print("输入内容为空")
            return

    code = read_file('code.py')
    from api import modify, modify_check, code_error

    response = modify(text, code)
    new_code = extract_code_from_markdown(response)
    if new_code:
        write_file('code.py', new_code)
    else:
        print(response)
        return

    for i in range(5):
        result = run_code('code.py')
        if "Error" in result or "Traceback" in result:
            response = code_error(code, result)
        else:
            response = modify_check(text, code, result)

        new_code = extract_code_from_markdown(response)
        if new_code:
            write_file('code.py', new_code)
        else:
            print(response)
            return

    if "Error" in result or "Traceback" in result:
        print("程序不能正常运行")
    else:
        print("不确定程序是否符合预期")

if __name__ == "__main__":
    main()
    import api
    modified_text = api.modify(text)
    code = extract_code(modified_text)
    if not code:
        print("未匹配到代码块")
        return

    save_code(code)
    execution_count = 0

    while execution_count < 5:
        execution_count += 1
        result, error = run_code()

        if error:
            api.code_error(code, error)
            modified_text = api.code_error(code, error)
        else:
            api.modify_check(text, code, result)
            modified_text = api.modify_check(text, code, result)

        new_code = extract_code(modified_text)
        if new_code:
            save_code(new_code)
        else:
            print(modified_text)
            return

        if execution_count == 5:
            if error:
                print("程序不能正常运行")
            else:
                print("不确定程序是否符合预期")
            return

main()