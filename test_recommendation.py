from test_data import *
from loaddata import read_posts_from_file, user_query
from recommendation import *

#posts = read_posts_from_file()

def test_case(post, query, complicated=False):
    if (not complicated):
        print(f"post:{post}")
        print(f"query:{query}")
    print(match_score(post, query))

#test_case(complicated_posts_for_test[0], complicated_queries_for_test[0], complicated=True)
#test_case(simple_posts_for_test[4], simple_queries_for_test[4])

for i in recommendation_list(complicated_posts_for_test, complicated_queries_for_test[0], 1):
    print(complicated_posts_for_test[i])