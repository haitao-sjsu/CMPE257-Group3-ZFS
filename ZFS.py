from loaddata import read_posts_from_file, user_query
from recommendation import recommendation

posts = read_posts_from_file()

for i in range(len(posts)):
    response = recommendation(posts[i], user_query)
    print(f"Post #{i + 1}\n{response}\n\n")