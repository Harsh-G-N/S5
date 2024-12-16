import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv('PlayTennis.csv')
print(data.head())

X = data.drop('Play Tennis', axis=1)  
y = data['Play Tennis'] 

X = pd.get_dummies(X)
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
precision = precision_score(y_test, y_pred, average='weighted')
print(f'Precision: {precision:.2f}')
recall = recall_score(y_test, y_pred, average='weighted')
print(f'Recall: {recall:.2f}')

outlook = input("Enter Outlook (Sunny, Overcast, Rain): ")
temperature = input("Enter Temperature (Hot, Mild, Cool): ")
humidity = input("Enter Humidity (High, Normal): ")
wind = input("Enter Wind (Weak, Strong): ")

user_input = {
    'Outlook': outlook,
    'Temperature': temperature,
    'Humidity': humidity,
    'Wind': wind
}

user_input_df = pd.DataFrame([user_input])

user_input_encoded = pd.get_dummies(user_input_df)

for col in X_train.columns:
    if col not in user_input_encoded.columns:
        user_input_encoded[col] = 0

user_input_encoded = user_input_encoded[X_train.columns]

user_prediction = model.predict(user_input_encoded)

print(f'The prediction for the given input is: {user_prediction[0]}')