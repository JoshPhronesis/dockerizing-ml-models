import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the Kings County House Sales dataset
data = pd.read_csv("kc_house_data.csv")

# Using 'sqft_living' as feature and 'price' as target
X = data["sqft_living"].values.reshape(-1, 1)
y = data["price"].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Save the model using pickle
with open("kings_county_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
