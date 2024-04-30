import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from llm import *

def get_embedding(text):
    return client.embeddings.create(input=[text], model=MODEL_EMBEDDING).data[0].embedding

def match(post_string, user_string):
    post_embedding = get_embedding(post_string)
    user_embedding = get_embedding(user_string)
    post_embedding_np = np.array(post_embedding)
    user_embedding_np = np.array(user_embedding)
    return cosine_similarity([post_embedding_np], [user_embedding_np])[0][0]