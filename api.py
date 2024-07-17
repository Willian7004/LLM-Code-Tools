#本程序包含用于各项任务的提示词，由项目内其它程序调用，使用前需要在send函数填写自己使用的模型的api地址和api key。
# python3
# Please install OpenAI SDK first：`pip3 install openai`
from openai import OpenAI

def send(system,user):
    client = OpenAI(api_key=" ", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-coder",
        messages=[
            {"role": "system", "content":system},
            {"role": "user", "content":user},
        ],
        stream=False
    )

    return(response.choices[0].message.content)

def note(text):
    output=send("给以下代码添加详细的中文注释",text)
    return(output)

def describe(text):
    output=send("具体描述以下代码的功能",text)
    return(output)

def summarize(text):
    output=send("以下是一个程序源码中各文件的路径和功能描述，根据这些内容描述整个程序的功能和实现方法",text)
    return(output)

def question(text,question):
    output=send("以下是一个程序源码中各文件的路径和功能描述，根据这些内容回答后面的问题"+text,question)
    return(output)

def code(text):
    output=send("根据以下要求，写一个python程序：",text)
    return(output)

def code_check(text,code,result):
    output=send("以下python程序的功能要求为："+text+"程序内容为："+code+"运行结果为："+result,"检查程序运行结果是否符合预期，如果确定运行结果不符合预期，请对程序进行修改。如果不确定运行结果是否符合预期，则回复不确定运行结果是否符合预期")
    return(output)

def code_error(code,result):
    output=send(code,"以上程序报错内容为："+result+"尝试进行修改以修复这个问题")
    return(output)

def modify(question,text):
    output=send("根据以下要求，修改程序："+question,"需要修改的程序如下："+text)
    return(output)

def modify_check(text,code,result):
    output=send("以下python程序的修改要求为："+text+"程序内容为："+code+"运行结果为："+result,"检查程序运行结果是否符合修改要求，如果确定运行结果不符合修改要求，请对程序进行再次修改。如果不确定运行结果是否符合修改要求，则回复不确定运行结果是否符合修改要求")
    return(output)
