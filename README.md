#  Student Performance Predictor using Machine Learning

## 📌 Overview
The Student Performance Predictor is a machine learning project that estimates student marks based on key academic factors such as study hours and attendance.

This project demonstrates how AI/ML can be applied to solve real-world educational problems by helping students understand and improve their academic performance.

---

## Features
- Predicts student marks using ML model  
- Uses Linear Regression algorithm  
- Simple and fast prediction system  
- Command-line based interaction  
- Provides model accuracy using R² score  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Pickle  

---

## 📂 Project Structure
Student-Performance-Predictor/
│
├── data/
│   └── student_data.csv
│
├── src/
│   ├── train_model.py
│   ├── predict.py
│
├── model.pkl
├── requirements.txt
├── README.md
└── report.pdf

---

 ## Usage

Step 1: Train the Model
python src/train_model.py

Step 2: Run Prediction
python src/predict.py

Example Input:
Enter study hours: 6  
Enter attendance (%): 80  

Example Output:
Predicted Marks: 72.50  

---

##  Machine Learning Workflow
1. Data Collection  
2. Data Preprocessing  
3. Model Training  
4. Model Evaluation (R² Score)  
5. Prediction  

---

## 🎯 Problem Statement
Students often lack insights into how their study habits and attendance impact their academic performance. This project aims to provide a predictive model to assist students in improving their results.

---

## 📈 Results
The model successfully predicts student marks with a reasonable level of accuracy using a simple linear regression approach.

---

## ⚠️ Limitations
- Uses a small dataset  
- Limited features  

---

##  Future Improvements
- Add more features  
- Build GUI  
- Use advanced ML models  
- Deploy as web app  
