from test_data import *
from loaddata import read_posts_from_file, user_demand
from recommendation import *

#posts = read_posts_from_file()

def test_case(post, demand, complicated=False):
    if (not complicated):
        print(f"post:{post}")
        print(f"demand:{demand}")
    print(match_score(post, demand))

#test_case(complicated_posts_for_test[0], complicated_demands_for_test[0], complicated=True)
#test_case(simple_posts_for_test[4], simple_demands_for_test[4])

for i in recommendation_list(complicated_posts_for_test, complicated_demands_for_test[0], 1):
    print(complicated_posts_for_test[i])