import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the dataset
housing_data = pd.read_csv('modified_excel_file.csv')

# Filter rows labeled as 'Supply' in the 'Supply(Selling)_or_Demand(Buying)' column
supply_data = housing_data[housing_data['Supply(Selling)_or_Demand(Buying)'] == 'Supply'].copy()

# Remove rows with NaN values in 'rent' and 'bedrooms' columns
supply_data.dropna(subset=['rent'], inplace=True)

# Convert 'rent' column to int type
supply_data['rent'] = pd.to_numeric(supply_data['rent'].str.replace('$', ''), errors='coerce')

# Replace punctuation marks in the location column
supply_data['location'] = supply_data['location'].str.replace(',', '')

# Replace missing values and NaN values in 'bedrooms' and 'bathrooms' columns with 1
supply_data['bedrooms'] = supply_data['bedrooms'].fillna(1)
supply_data['bathrooms'] = supply_data['bathrooms'].fillna(1)

# Splitting the data into training and testing sets
X = supply_data[['rent', 'bedrooms']]
y = supply_data[['location', 'amenities', 'text','bedrooms']]  # Features to predict
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def recommend_similar_houses(input_rent, input_bedrooms, k=5):
    # Calculate Euclidean distance between each house's rent and bedrooms to the input values
    distances = np.sqrt((X_train['rent'] - input_rent)**2 + (X_train['bedrooms'] - input_bedrooms)**2)
    supply_data_train = y_train.copy()  # Get supply data corresponding to training set
    supply_data_train['distance'] = distances.values
    
    # Sort houses by distance and select top k recommendations
    recommended_houses = supply_data_train.sort_values(by='distance').head(k)
    
    # Return recommended houses with required columns
    return recommended_houses

# Example of using the function for recommendation
input_rent = 1000
input_bedrooms = 2
k = 5 

recommended_houses = recommend_similar_houses(input_rent, input_bedrooms)
print("Recommended Houses:")
print(recommended_houses)

# Evaluate the recommendation system using the testing set (you can adapt this part based on your evaluation method)
# For simplicity, let's assume the user's preferred house is in the top-K recommended list
user_preferred_bedrooms = 1
user_preferred_rent = input_rent
top_k_recommendations = recommend_similar_houses(user_preferred_rent, user_preferred_bedrooms, k=5)

# Hit Rate
hit_rate = len(top_k_recommendations[top_k_recommendations['bedrooms'] == user_preferred_bedrooms]) / k
print("Hit Rate:", hit_rate)

# Mean Reciprocal Rank (MRR)
mrr = 0
for i, rec in enumerate(top_k_recommendations.values):
    if rec[2] == user_preferred_bedrooms:
        mrr = 1 / (i + 1)
        break
print("Mean Reciprocal Rank (MRR):", mrr)

# Precision at K
relevant_recommendations = len(top_k_recommendations[top_k_recommendations['bedrooms'] == user_preferred_bedrooms])
precision_at_k = relevant_recommendations / k
print("Precision at K:", precision_at_k)

# Plotting
metrics = ['Hit Rate', 'Mean Reciprocal Rank (MRR)', 'Precision at K']
values = [hit_rate, mrr, precision_at_k]

plt.bar(metrics, values, color=['blue', 'green', 'red'])
plt.ylabel('Value')
plt.title('Evaluation Metrics')
plt.show()
