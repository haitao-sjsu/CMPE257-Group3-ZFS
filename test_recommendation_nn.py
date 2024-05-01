import pandas as pd
from test_data import *
from recommendation_nn import *

data = pd.read_csv(r"Dataset_Classification/posts.csv", encoding='utf-8')
data = data.dropna()
posts = data.sample(frac=1).head(15)['text'].values.tolist()

for i in recommendation_list(posts, complicated_demands_for_test[0], 1):
    print(posts[i])