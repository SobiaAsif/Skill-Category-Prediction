# 💼 Skill Category Prediction

## 🚀 Live Demo

https://ml-skill-category-prediction.streamlit.app/

## 📌 Project Overview

This project predicts the category of a technical skill using market demand and scarcity indicators. It is a multiclass classification problem built with the K-Nearest Neighbors (KNN) algorithm and deployed using Streamlit.

The model classifies a skill into one of the following categories:

- AI
- Data
- DevOps
- Engineering
- Product
- Security

---

## 📂 Dataset

- **File:** `skill-scarcity-index.csv`
- **Rows:** 1,635
- **Target Variable:** `category`

### Features

- Demand Count
- Demand Percentage
- Median Days Open
- Salary Premium Percentage
- Repost Rate Percentage
- Scarcity Score

---

## 🛠️ Machine Learning Workflow

- Data Loading
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Missing Value Handling
- Feature Selection
- Feature Scaling
- Train-Test Split
- K-Nearest Neighbors (KNN) Model Training
- Model Evaluation
- Pipeline Creation
- Model Saving using Joblib
- Streamlit Web Application

---

## 🤖 Model

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Neighbors (K):** 3
- **Feature Scaling:** StandardScaler
- **Pipeline:** Scikit-learn Pipeline

---

### Evaluation Metrics

- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📁 Project Structure

```text
Skill_Category_Prediction/

├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
├── models/
├── notebooks/
└── screenshots/
```

## 🚀 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

## ▶️ How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

### Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📸 Screenshots

## 📸 Screenshots

### Home Page

![Home](<screenshots/home.png>)

### About 

![About](<screenshots/About this project.png>)

---

## 🔮 Future Improvements

- Compare KNN with Random Forest and XGBoost
- Tune hyperparameters using GridSearchCV
- Improve feature engineering
- Deploy using Docker and cloud platforms

---

## 👩‍💻 Author

**Sobia Asif **

Computer Science Graduate

GitHub: *(https://github.com/SobiaAsif/)*
