import math
import json
from retrieval import retrieval
from match_with_embedding import match

def match_score(post, usr_demand):
    post_dict = json.loads(retrieval(post))
    usr_dict = json.loads(retrieval(usr_demand))
    match_score_list = []

    for key, post_value in post_dict.items():
        usr_value = usr_dict[key]
        if post_value == 'unknown' or usr_value == 'unknown':
            match_score = 1
        elif key == 'type':
            match_score = 1 if post_value == 'supply' and usr_value == 'demand' else 0
        elif key == 'gender':
            match_score = 0 if post_value == 'male' and usr_value == 'female' or post_value == 'female' and usr_value == 'male' else 1
        elif key == 'price':
            try:
                price = float(post_value)
                budget = float(usr_value)
            except:
                continue
            if price <= budget:
                match_score = 1
            elif price <= budget * 1.2:
                match_score = 0.5
            else:
                match_score = 0
        else:
            post_str = f"{key}: {post_value}"
            user_str = f"{key}: {usr_value}"
            match_score = match(post_str, user_str)

        match_score_list.append(match_score)
        #if post_value != 'unknown' or usr_value != 'unknown':
        #    print(f"post[{key}]:{post_value}")
        #    print(f"demand[{key}]:{usr_value}")
        #    print(f"match_score:{match_score}")
    
    final_score = math.prod(match_score_list)
    return final_score

def recommendation_list(posts, usr_demand, number):
    results = []
    for i in range(len(posts)):
        score = match_score(posts[i], usr_demand)
        results.append((i, score))
    
    results = sorted(results, key=lambda item : item[1], reverse=True)
    print(results)
    return [item[0] for item in results][:number]

