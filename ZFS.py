from load_data import read_posts_from_file
from test_data import *
from classification_with_llm import classification
from recommendation_customize import recommendation_list

recommendation_number = 1
posts = read_posts_from_file()
supply_posts = [post for post in posts[10:20] if classification(post) == 'Supply']
usr_demand = complicated_demands_for_test[0]

print(f"Your demand is:\n{usr_demand}")
print(f"The following {recommendation_number} posts are recommended for you:")
for i in recommendation_list(supply_posts, usr_demand, recommendation_number):
    print(f"Post #{i + 1}\n{supply_posts[i]}\n\n")