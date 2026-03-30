import pickle

model = pickle.load(open("../model.pkl", "rb"))

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))

prediction = model.predict([[hours, attendance]])

print(f"Predicted Marks: {prediction[0]:.2f}")
