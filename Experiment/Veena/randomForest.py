import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel('OFFICIAL_Labeling_dataset_facebook-groups-scraper_raw_SVM_PREDICTIONS.xlsx')
data = data[data['Supply(Selling)_or_Demand(Buying)'] == 'Supply']

# Preprocessing
# Selecting relevant columns for the model
features = ['Column1','text', 'location', 'fromDate', 'toDate', 'amenities', 'bedrooms', 'bathrooms']
target = 'rent'

X = data[features]
y = data[target]

X_encoded = pd.get_dummies(X, columns=['Column1','text', 'location', 'fromDate', 'toDate', 'amenities', 'bedrooms', 'bathrooms'])

# Impute missing values with the mean for features
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X_encoded)

y_imputed = y.fillna(y.mean())

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y_imputed, test_size=0.2, random_state=42)

# Training the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predicting on the test set
y_pred = rf_model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# Selecting rows with rent close to 1000 dollars
threshold = 10
close_to_1000_indices = np.where((y_pred >= 1000 - threshold) & (y_pred <= 1000 + threshold))[0]

# Get the actual rows corresponding to the selected indices

encoded_columns = X_encoded.columns

for row in close_to_1000_indices:
    encoded_row = X_test[row]
    decoded_row = {}
    for i, val in enumerate(encoded_row):
        if val == 1:
            column_name = encoded_columns[i]
            feature_name, feature_value = column_name.split('_', 1) 
            decoded_row[feature_name] = feature_value
    print(decoded_row)
    print("======================================================================")
