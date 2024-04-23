import numpy as np
import openai
from sklearn.metrics.pairwise import cosine_similarity

MODEL = "text-embedding-3-large"
client = openai.OpenAI()

def get_embedding(text, model):
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def match(post_string, user_string):
    post_embedding = get_embedding(post_string, model=MODEL)
    user_embedding = get_embedding(user_string, model=MODEL)
    post_embedding_np = np.array(post_embedding)
    user_embedding_np = np.array(user_embedding)
    return cosine_similarity([post_embedding_np], [user_embedding_np])[0][0]