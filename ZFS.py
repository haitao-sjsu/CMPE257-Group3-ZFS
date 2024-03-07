from dataload import read_posts_from_file
from recommendation import get_completion, messages

posts = read_posts_from_file()

user_query= f"""
I want to find some housing. My budget is under $1500.
"""

for i in range(len(posts)):
    response = get_completion(messages(posts[i], user_query))
    print(f"Post #{i + 1}\n{response}\n\n")