from loaddata import read_posts_from_file, user_query
from retrieval import retrieval
from match_embedding import match

import json

posts = read_posts_from_file()

post_dict = json.loads(retrieval(posts[2]))
user_dict = json.loads(retrieval(user_query))

match_score_list = []
for key, post_value in post_dict.items():
    user_value = user_dict[key]
    if key == 'type':
        match_score = 1 if post_value == 'supply' and user_value == 'demand' else 0
    elif key == 'gender':
        match_score = 0 if post_value == 'male' and user_value == 'female' or post_value == 'female' and user_value == 'male' else 1
    elif post_value == 'unknown' or user_value == 'unknown':
        match_score = 1
    else:
        post_str = f"{key}: {post_value}"
        user_str = f"{key}: {user_value}"
        match_score = match(post_str, user_str)
    match_score_list.append(match_score)
    print(f"post[{key}]: {post_value}")
    print(f"user[{key}]: {user_value}")
    print(f"match score: {match_score}")
