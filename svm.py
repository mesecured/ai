import pandas as pd
import numpy as np
data=pd.read_csv('Social_Network_Ads.csv')
print(data.dtypes)
print(data['User ID'].head())
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X = data[['User ID', 'Age', 'EstimatedSalary']]

# Extract the target variable y
y = data['Purchased']

# Perform any necessary preprocessing on X and y if required

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an SVM classifier
classifier = svm.SVC(kernel='linear')

# Train the classifier on the training data
classifier.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
