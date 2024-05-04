import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn import model_selection
from test_data import *
from classification_with_llm import train_with_llm, predict_with_llm

def test_classification_with_llm(scale, training):
    data = pd.read_csv(r"Dataset_Classification/posts.csv", encoding='utf-8')
    data = data.dropna()
    if scale == 'SMALL':
        data = data.sample(frac=1).head(10)
    elif scale == 'MEDIUM':
        data = data.sample(frac=1).head(50)
    elif scale == 'ALL':
        data = data.sample(frac=1)

    if training == False:    
        posts = data['text']
        test_Y = data['label']
        predictions = predict_with_llm(posts)
        accuracy = accuracy_score(predictions, test_Y)*100
        print(f"prediction accuracy with llm and without training -> {accuracy}")
    elif training == True:
        Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(data['text'],data['label'],test_size=0.8)
        train_with_llm(Train_X, Train_Y)
        predictions = predict_with_llm(Test_X)
        accuracy = accuracy_score(predictions, Test_Y)*100
        print(f"prediction accuracy with llm and with training -> {accuracy}")

test_classification_with_llm(scale='MEDIUM', training=False)

#print(predict_with_llm(simple_posts_for_test))
#print(predict_with_llm(simple_demands_for_test))
#print(predict_with_llm(complicated_demands_for_test))
#print(predict_with_llm(complicated_posts_for_test))
