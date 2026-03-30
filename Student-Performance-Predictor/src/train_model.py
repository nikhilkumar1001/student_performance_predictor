import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

data = pd.read_csv("../data/student_data.csv")

X = data[['hours_study', 'attendance']]
y = data['marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)
print(f"Model Accuracy (R2 Score): {score:.2f}")

pickle.dump(model, open("../model.pkl", "wb"))

print("Model trained and saved successfully!")
