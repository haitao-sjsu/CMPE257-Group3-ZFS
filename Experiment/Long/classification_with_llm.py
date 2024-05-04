from llm import *

def train_with_llm(posts, results):
    sys_msg = """
    You will be provided a post about renting seperated by {delimiter} and its category also seperated by {delimiter}. You job is to learn the relation between the context of the post and its category. After you finished the learning, please reply 'Finished'.
    """
    for post, result in zip(posts, results):
        usr_msg = f"{delimiter}posts: {post}{delimiter}{delimiter}category: {result}{delimiter}"
        print(get_completion(messages(sys_msg, usr_msg)))
    print(f"Training process completed. {len(posts)} posts have been fed into the llm.")

def classification(post):
    sys_msg = f"""
    You will be provided a post about renting seperated by {delimiter}. Your job is to do the classification of this post. The rules are as follows:

    If you think the post is from the landlord who provided the supply of a house or from someone who wanna sublease his house, the post should be in the 'Supply' category.
    If you think the post is from someone who wanna sublease his house, the post should be in the 'Supply' category.
    If you think the post is from someone who is looking for some other guy to live together, the post should be in the 'Supply' category.
    If you think the post is from someone who are trying to find some room or house to live, the post should be in the 'Demand' category.
    Otherwise, the post should be in the 'Unknown' category.

    Your response could be only one of the three category: 'Supply', 'Demand' or 'Unknown'.
    """

    usr_msg = f"{delimiter}{post}{delimiter}"
    return get_completion(messages(sys_msg, usr_msg))

def predict_with_llm(posts):
    predictions = []
    for post in posts:
        predictions.append(classification_with_llm(post))
    return predictions
