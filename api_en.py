#This program contains prompts for each task, which are called by other programs in the project, and you need to fill in the API address and API key of the model you are using in the send function before use.
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
    output=send("Add detailed comments to the following code",text)
    return(output)

def describe(text):
    output=send("Describe the functionality of the following code specifically",text)
    return(output)

def summarize(text):
    output=send("The following is a description of the path and function of each file in the source code of a program, and describes the function and implementation method of the whole program according to these contents",text)
    return(output)

def question(text,question):
    output=send("The following is a description of the path and function of each file in the source code of a program, and answer the following questions based on these contents"+text,question)
    return(output)

def code(text):
    output=send("Write a python program according to the following requirements：",text)
    return(output)

def code_check(text,code,result):
    output=send("The functional requirements of the following python program are: "+text+" program content is: "+code+" running result is: "+result," check whether the program running result meets expectations, if it is determined that the running result does not meet expectations, please modify the program. If you're not sure if the run results are as expected, reply that you're not sure if the run results are as expected")
    return(output)

def code_error(code,result):
    output=send(code,"The error message of the above program is: "+result+" tries to modify it to fix this problem")
    return(output)

def modify(question,text):
    output=send("According to the following requirements, modify the program: "+question," and the program that needs to be modified is as follows："+text)
    return(output)

def modify_check(text,code,result):
    output=send("The following python program modification requirements are: "+text+" program content is: "+code+" running result is: "+result," check whether the program running result meets the modification requirements, if it is determined that the running result does not meet the modification requirements, please modify the program again. If you are not sure whether the run result meets the modification requirements, reply that you are not sure whether the run results meet the modification requirements")
    return(output)
