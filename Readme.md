# ZFS project Code Instruction

## Basic ideas
As we discussed before, the basic processdure should be like:

1. Load the dataset to memory. This is done in `load_data.py`.
2. We do some classfications to filter the supply posts. There are two classification algorithms implemented in `classification_with_llm.py` and `classification_without_llm.py`.
3. We do the recommendation. We have three recommendation algorithms, `recommendation_with_llm.py`, `recommendation_nn.py` and `recommendation_customize.py`. each file has a function `recommendation_list()`.
4. We run our program from `ZFS.py`. The command is quite straightforward:
```python
python ZFS.py
```

## Before you run the code
* I would suggest VScode as our developing environment.

* I would suggest the Github destop App if you are not familiar with the git command. Here is the link: https://desktop.github.com/

* Make sure that you have got openai key, and set the configration. Please refer to the documentation: https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key

## What on earth every file and directory do
### Code - Classification
`classification_with_llm.py`: This file do the classification with LLM. Basically we do the prompt engineering to get the classification response. There are two functions in the file - `classification_with_llm()` and `predict_with_llm()`, that first one did the classifcation with one post, and second did the classification with a list of posts. There is another function `train_with_llm()` which tries to train the LLM to get a better result. But the result is not good according to the test file result.

`classification_without_llm.py`: This file try to do the classfication using some conventional technique. You could refer to the link below for detail. What it did is:
a. Data preprocessing. Convert the text of post into a list of words.
b. Word Vectorization. Turning the list of words into numerical feature vectors. TF-IDF method is used.
c. Use the Naive Bayes Classifier Algorithm and SVM Algorithms to Predict the outcome

reference: A guide to Text Classification(NLP) using SVM and Naive Bayes with Python
https://medium.com/@bedigunjit/simple-guide-to-text-classification-nlp-using-svm-and-naive-bayes-with-python-421db3a72d34

### Code - Recommendation
`recommendation_with_llm.py`: Like `classification_with_llm.py`, we did some prompt engineering to let the LLM scores each post based on user's demand. And recommend post based on scores.

`recommendation_nn.py`: We compute the distance between the post and user's demand. The distance represents the similarity between the post and user's demand. And we recommend the nearest neighbours, which have the minimum distance. In the implementation, there are two methods to compute the distance, one is get the embedding of the whole post and user's demand, and compute the distance, this is what the function `distance_coarse_grained()` did. The other method is to retrieve info from post first, and then vectorize and compute the distance, this is what the function `distance_coarse_grained()` did. As for the distance, there are two kinds of distances, `euclidean_distance()` and `manhattan_distance()`.

reference: Hands-on Content Based Recommender System using Python
https://towardsdatascience.com/hands-on-content-based-recommender-system-using-python-1d643bf314e4

`recommendation_customize.py`: Combining the above two ideas, we could do some customization. We choose the compute the match score of the post based on user's demand. We do it following the steps:
1. retrieve the features from post and user's demand.
2. For some basic features such as gender, price, we hard coded some match score rule.
3. For other features not suitable for hard coding, we use LLM to compute the match score. We could either let it compute it directly(`match_with_llm.py`), or convert it into embedding vectors and then compute the cosine similarity(`match_with_embedding.py`).
4. The final match score would be the multiplication of all match scores.
5. sort the list of final match scores, and recommend the posts with highest final match score.

### Code - Library and Utility
`ZFS.py`: The program begins from here. Just like the main function in C.

`load_data.py`: This file is used for loading data from the file. Now it only has one function: `read_posts_from_file()`.

`llm.py`: This is the library of LLM. Any file using LLM should import this file.

`retrieval.py`: This file is to retrieval features from post or user's demand. It would be used in recommendation algorithm.

`match_with_embedding.py`: This file is to get the embedding vector of a text(`get_embedding()`), and compute the similarity of two embedding vectors(`match()`).

`match_with_llm.py`: This file is to let LLM compute the similarity of two formatted strings(`match()`).

### CODE - Testing
There are several test files in the folder. `test_data.py` is a file that contains some test cases, including simple ones and complicated one. Other files, as their names indicated, are the corresponding testing files. For example, `test_classification_with_llm.py` is used for testing `classification_with_llm.py`.

### Markdown Documentation
`Readme.md`: Yes, what you are reading is readme.md.

`Log.md`: As suggested by the name, it is the log file.

### Dataset
`Dataset_Raw_From_Facebook`: This directory and the dataset inside is by Amen. Well done! There are 3 files, and maybe Amen could explain those files in detail. What I am using now is the raw_overview.csv.

`Dataset_Classification`: This directory should be used training the classfication algorithm. In this directory:

- 1000 posts generated from raw_overview.csv
- a classification.csv in this directory. I manually labelled the posts 1-20. For example, 1,0 means post_1.txt is a post from landlord.

`Dataset_Recommendation`:This directory should be used training the recommendation algorithm. Now it is empty.

### Others
`__pycache__`: It seems every python project will have this directory which is generated by python. But I am not very sure what it is. 

## Proposals about what we could do before midterm
* We may train some classification algorithm and test it.
* We may test the accuracy of the recommendation algorithm.
* We may do some prompt engineering to make the result better.
* We need to finish the presentation.

## Proposals about what we could do before final
- We may use the web API to read the data from web
- We may redesign the recommendation algorithm. For example, we could try some library, such as langchain, Kor.
- We may design some UI to accept user input.
- We may design some module to push the notifications to client's Email.
- We may do some analysis from the commercial view (E.g., is it possible to gain profit? Who will be our potiental client? ).
- We need to finish the presentation.