import openai

MODEL = "gpt-3.5-turbo"
client = openai.OpenAI()

delimiter = "####"

system_message = f"""
You will be provided two formatted strings, first one is the post string and the second is the user query string. The string format is <key>:<value>. The strings will be delimited with {delimiter} characters.You job is to calculate a match score between these two strings. The match score is a float number between 0 and 1. The higher the score, the more likely the post is recommended to the user query. Please follow the rules to calculate the match score:

The output should be the match score. Nothing else.
"""

system_message_backup = f"""
You will be provided two formatted strings, first one is the post string and the second is the user query string. The string format is <key>:<value>. The strings will be delimited with {delimiter} characters.You job is to calculate a match score between these two strings. The match score is a float number between 0 and 1. The higher the score, the more likely the post is recommended to the user query. Please follow the rules to calculate the match score:

If the key is 'type', the score is either 1 or 0. If the value of the post is 'demand' and the value of the user query is 'supply', the score is 1, otherwise the score is 0.
If the key is 'gender', the score is either 1 or 0. If the two values are 'male' and 'female', the score is 0, otherwise the score is 1.
If either value is empty, the score is 1.

The output should be the match score. Nothing else.
"""

def get_completion(messages, model=MODEL):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def match(post_string, user_string):
    user_message = f"""
    This is the post query: {delimiter}{post_string}{delimiter}. And
    this is the user query: {delimiter}{user_string}{delimiter}.
    """
    messages = [  
        {'role':'system', 
        'content': system_message},    
        {'role':'user', 
        'content': user_message},  
    ]
    response = get_completion(messages)
    return response