import openai

MODEL = "gpt-3.5-turbo"
client = openai.OpenAI()

delimiter = "####"

def system_message_1(post):
    return f"""
You will be provided a leasing post and a customer query. The post and the customer query will be delimited with {delimiter} characters. You job is to judge whether the post matches the customer query or not, and explain why. Please follow these steps to answer the customer queries.

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

Step 4: Judge whether the info and req are matched or not. The result would be a float number between 0 and 1. The higher the score, the more likely the post is recommended to the customer query. If req are not matched with info, then score would be 0, if they perfectly match, the score would be 1.

Your output format would be:
Match score: <the result of step 4>
Reason: in less than 50 words

{delimiter}{post}{delimiter}
"""

def system_message_2(post):
    return f"""
You will be provided a leasing post and a customer query. The post and the customer query will be delimited with {delimiter} characters. You job is to compute the recommendation score of the post to the customer query. The score is a float number between 0 and 1. The higher the score, the more likely the post is recommended to the customer query.

The output should be the recommendation score. Nothing else.

This is the leasing post: {delimiter}{post}{delimiter}
"""

def messages(post, user_query):
    return  [  
{'role':'system', 
 'content': system_message_1(post)},    
{'role':'user', 
 'content': f"This is the customer query: {delimiter}{user_query}{delimiter}"},  
] 

def get_completion(messages, model=MODEL):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def recommendation(post, user_query):
    return get_completion(messages(post, user_query))