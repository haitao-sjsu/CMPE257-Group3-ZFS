from test_data import *
#from loaddata import read_posts_from_file, user_query
from retrieval import retrieval

print(complicated_posts_for_test[0])
print(retrieval(complicated_posts_for_test[0]))

# for post in simple_queries_for_test:
#     print(post)
#     print(retrieval(post))
#     print('\n')