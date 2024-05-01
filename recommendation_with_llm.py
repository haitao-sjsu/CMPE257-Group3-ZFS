from llm import *

def match_score(post, user_demand):
    sys_msg = f"""
    You will be provided a leasing post and a customer demand. The post and the customer demand will be delimited with {delimiter} characters. You job is to compute the recommendation score of the post to the customer demand. The score is a float number between 0 and 1. The higher the score, the more likely the post is recommended to the customer demand.

    The output should be the recommendation score. Nothing else.

    This is the leasing post: {delimiter}{post}{delimiter}
    """

    usr_demand = f"This is the customer demand: {delimiter}{user_demand}{delimiter}"
    return get_completion(messages(sys_msg, usr_demand))

def recommendation_list(posts, usr_demand, number):
    results = []
    for i in range(len(posts)):
        score = match_score(posts[i], usr_demand)
        results.append((i, score))
    
    results = sorted(results, key=lambda item : item[1], reverse=True)
    print(results)
    return [item[0] for item in results][:number]
