import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()
df=pd.DataFrame(data=cancer.data)
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=42)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=cancer.feature_names, class_names=cancer.target_names)
plt.show()

new_sample = np.array([14.0, 20.0, 100.0, 70.0, 0.1, 0.2, 0.3, 0.2, 1.0, 2.0, 
                       15.0, 80.0, 0.05, 0.05, 0.03, 0.02, 0.1, 0.2, 0.3, 0.2, 
                       0.3, 0.4, 0.3, 0.2, 0.4, 0.5, 0.4, 0.3,0.4,0.9]).reshape(1, -1)  

prediction = clf.predict(new_sample)
predicted_class = cancer.target_names[prediction][0]

print(f"The predicted value: {predicted_class}")
print(df)
