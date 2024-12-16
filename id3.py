import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import graphviz
from sklearn.tree import export_graphviz


# Load training data
col_names = ['Outlook', 'Temperature', 'Humidity', 'Wind', 'Play Tennis']
train_data = pd.read_csv("PlayTennis.csv", header=None, names=col_names)

# Define feature columns and class label
feature_cols = ['Outlook', 'Temperature', 'Humidity', 'Wind']
class_label = "Play Tennis"

# Split data into features and target variable
x_train = train_data[feature_cols].copy()  # Make a copy to avoid SettingWithCopyWarning
y_train = train_data[class_label]

# Encode categorical features
label_encoders = {}
for column in feature_cols:
    le = LabelEncoder()
    x_train.loc[:, column] = le.fit_transform(x_train[column])
    label_encoders[column] = le

# Encode the target variable
le_target = LabelEncoder()
y_train = le_target.fit_transform(y_train)

# Initialize and fit the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy',min_samples_split=2)
clf = clf.fit(x_train, y_train)

# Load test data
test_data = pd.read_csv("testPlayTennis.csv", header=None, names=col_names)

# Split test data into features and target variable
x_test = test_data[feature_cols].copy()  # Make a copy to avoid SettingWithCopyWarning
y_test = test_data[class_label]

# Encode test features using the same encoders as for training
for column in feature_cols:
    x_test.loc[:, column] = label_encoders[column].transform(x_test[column])

# Encode the test target variable
y_test = le_target.transform(y_test)

# Predict and evaluate the model
y_pred = clf.predict(x_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

instance = []
for column in feature_cols:
    value = input(f"Enter {column}: ")
    instance.append(value)

for i, column in enumerate(feature_cols):
    instance[i] = label_encoders[column].transform([instance[i]])[0]

instance = pd.DataFrame([instance], columns=feature_cols)

predicted_label = clf.predict(instance)[0]

predicted_label = le_target.inverse_transform([predicted_label])[0]

print("Predicted class label:", predicted_label)

# Create a Graphviz graph object
dot_data = export_graphviz(clf, out_file=None, 
                           feature_names=feature_cols,  
                           class_names=le_target.classes_,
                           filled=True, rounded=True,  
                           special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree", format="png")
