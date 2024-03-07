import openai

MODEL = "gpt-3.5-turbo"
client = openai.OpenAI()

delimiter = "####"

def system_message(post):
    return f"""
You will be provided a leasing or renting post and a customer query. The post and the customer query will be delimited with {delimiter} characters. You job is to judge whether the post matches the customer query or not, and explain why. Please follow these steps to answer the customer queries.

Step 1: Jude the post type, whether it is for leasing, renting or unrelevant. If it is not for leasing, then the match fails. 

Step 2: Extract information(info) from the post. The information include:
positon
room size
room type
furniture and facility
price
the beginning date of leasing
the ending date of leasing
leasing period
contact information

Step 3: Extract information(req) from the customer query.

Step 4: Judge whether the info and req are matched or not. The result would be one of the three: not match, partially match, perfectly match.
not match: req are not matched with info.
partially match: req are partially matched with info.
perfectly match: req are perfectly matched with info.

Your output format would be:
Match or not: <the result of step 3>
Reason: in less than 50 words

{delimiter}{post}{delimiter}
"""

def messages(post, user_query):
    return  [  
{'role':'system', 
 'content': system_message(post)},    
{'role':'user', 
 'content': f"{delimiter}{user_query}{delimiter}"},  
] 

def get_completion(messages, model=MODEL):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
