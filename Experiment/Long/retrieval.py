from llm import *

def retrieval(post):
    sys_msg = f"""
    You will be provided a post relating to renting seperated by {delimiter}. I need you to retrieve the information from the post. The information include:

    type: there are three types of the post. 'supply' means the post from the landlords, 'demand' means the post from the tenants, and 'unknown' means the post does not belong to the above two categories.
    gender: there are two types of the gender. 'male' or 'female'. For example, some landlords only accept girls as tenants, then it should be 'female'.
    price: the total monthly price, including rent fee, utility fee, etc. If several prices exist and the type of the post is 'supply', then output the lowest one. If several prices exist and the type of the post is 'demand', then output the highest one. The output should be a float number.
    bedroom: If the roome is private/single, output 'single'; if the room is shared, output 'shared'.
    bathroom: for example, is the bathroom or restroom private/single or shared.
    distance to SJSU: for example, 10 min driving distance to SJSU.
    parking: is there any space for parking.
    furniture: fully furnished, partially furnished, or no furnished. what furnitures in the room, for example, bed dresser , work table ,chair, lamp.
    room facilities: such as washer, dryer, kitchen, tv.
    community amenities: such as gym, pool, reading room, bbq space.
    move in date: the earliest available date for moving in.
    other info: informations that not included in the above categories.

    Please extract the above information from the post. If you can not find the information, please output 'unknown'.

    The response format would be a python dictionary, the values of which should be string.
    """

    usr_msg = f"{delimiter}{post}{delimiter}"
    return get_completion(messages(sys_msg, usr_msg))

