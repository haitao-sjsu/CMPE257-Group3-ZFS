import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

def predict_similar_rents(df, input_rent):
  """
  Predicts rows from a housing dataframe with similar rent using Random Forest.

  Args:
      df (pandas.DataFrame): The housing dataframe.
      input_rent (float): The rent value for which to find similar rents.

  Returns:
      list: A list of dataframes containing rows with similar rents.
  """

  # Select numerical features relevant to rent prediction
  numerical_features = ['bedrooms', 'bathrooms']
  X = df[numerical_features]

  # Handle categorical features (e.g., amenities) using one-hot encoding
  categorical_features = ['amenities']
  encoder = OneHotEncoder(handle_unknown='ignore')
  encoded_data = pd.DataFrame(encoder.fit_transform(df[categorical_features]))
  X = pd.concat([X, encoded_data], axis=1)

  # Target variable (rent)
  y = df['rent']

  # Train-test split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Random Forest model
  model = RandomForestRegressor(n_estimators=100, random_state=42)
  model.fit(X_train, y_train)

  # Predict similar rents
  predicted_rents = model.predict(X_test)

  # Tolerance for similar rents (adjust as needed)
  tolerance = 50

  # Find rows with similar rents (within tolerance)
  similar_rent_rows = []
  for index, row in df.iterrows():
    if abs(row['rent'] - input_rent) <= tolerance:
      similar_rent_rows.append(row.to_frame().T)

  # Optionally, filter test set based on predicted rent with tolerance
  # predicted_similar_rents = []
  # for i in range(len(predicted_rents)):
  #   if abs(predicted_rents[i] - input_rent) <= tolerance:
  #     predicted_similar_rents.append(X_test.iloc[i].to_frame().T)

  return similar_rent_rows

# Example usage (replace with your actual dataframe)
df = pd.DataFrame({
  'text': ['description 1', 'description 2'],
  'rent': [1000, 1200],
  'location': ['city A', 'city B'],
  'fromdate': ['2024-01-01', '2024-02-01'],
  'todate': ['2024-01-31', '2024-02-29'],
  'bedrooms': [1, 2],
  'bathrooms': [1, 1.5],
  'amenities': ['balcony, gym', 'parking, dishwasher']
})

input_rent = 1100
similar_rents = predict_similar_rents(df.copy(), input_rent)

# Print similar rent rows (or predicted similar rents if using commented section)
for rent in similar_rents:
  print(rent)
