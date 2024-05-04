import openai

MODEL = "gpt-3.5-turbo"
MODEL_EMBEDDING = "text-embedding-3-large"
client = openai.OpenAI()

delimiter = "####"

def messages(sys_msg, usr_msg):
    return  [  
{'role':'system', 
 'content': sys_msg},    
{'role':'user', 
 'content': usr_msg},  
] 

def get_completion(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
