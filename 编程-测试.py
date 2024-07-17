import os
import subprocess
import re

def read_input():
    user_input = input("请输入内容: ")
    if not user_input:
        try:
            with open("question.txt", "r", encoding="utf-8") as file:
                user_input = file.read().strip()
        except FileNotFoundError:
            user_input = ""
    return user_input

def extract_code(response):
    match = re.search(r"```(.*?)```", response, re.DOTALL)
    if match:
        code_lines = match.group(1).strip().split('\n')[1:]
        return '\n'.join(code_lines)
    return None

def run_code(code_path):
    try:
        result = subprocess.check_output(["python", code_path], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        result = str(e)
    return result

def save_code(code):
    with open("code.py", "w", encoding="utf-8") as file:
        file.write(code)

def main():
    text = read_input()
    if not text:
        print("输入内容为空")
        return

    import api
    response = api.code(text)
    code = extract_code(response)
    if not code:
        print("未匹配到代码内容")
        return

    save_code(code)
    result = run_code("code.py")

    for i in range(5):
        if "Error" in result:
            response = api.code_error(code, result)
        else:
            response = api.code_check(text, code, result)

        new_code = extract_code(response)
        if not new_code:
            print(response)
            return

        save_code(new_code)
        result = run_code("code.py")

    if "Error" in result:
        print("程序不能正常运行")
    else:
        print("不确定程序是否符合预期")

main()