import openai

MODEL = "gpt-3.5-turbo"
client = openai.OpenAI()

delimiter = "####"

system_message = f"""
You will be provided a post relating to renting. I need you to retrieve the information from the post. The information include:

type: there are three types of the post. 'supply' means the post from the landlords, 'demand' means the post from the tenants, and 'unknown' means the post does not belong to the above two categories.
gender: there are two types of the gender. 'male' or 'female'. For example, some landlords only accept girls as tenants, then it should be 'female'.
price: the total monthly price, including rent fee, utility fee, etc.
location: the address or the name of the room/apartment.
distance to SJSU: for example, 10 min driving distance to SJSU.
bedroom: is it private or shared.
bathroom: is it private or shared.
furniture: fully furnished, partially furnished, or no furnished. what furnitures in the room, for example, bed dresser , work table ,chair, lamp.
room facilities: such as washer, dryer, kitchen, tv.
community amenities: such as gym, pool, reading room, bbq space.
parking: is there any space for parking.
move in date: the earliest available date for moving in.
other info: informations that not included in the above categories.

Please extract the above information from the post. If you can not find the information, please output 'unknown'.

The response format would be a python dictionary.
"""

def messages(post):
    return  [  
{'role':'system', 
 'content': system_message},    
{'role':'user', 
 'content': f"{delimiter}{post}{delimiter}"},  
]

def retrieval(post, model=MODEL):
    response = client.chat.completions.create(
        model=model,
        messages=messages(post),
        temperature=0
    )
    return response.choices[0].message.content

