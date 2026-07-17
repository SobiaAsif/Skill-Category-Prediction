import streamlit as st
import pandas as pd
import joblib

# Load model
pipeline = joblib.load("models/skill_category_pipeline.pkl")

# Page configuration
st.set_page_config(
    page_title="Skill Category Prediction",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Skill Category Prediction")
st.write(
    """
Predict the category of a technical skill using market demand and scarcity indicators.
"""
)

# Sidebar
st.sidebar.header("Model Information")

st.sidebar.info(
    """
**Algorithm:** K-Nearest Neighbors (KNN)

**Accuracy:** 51.99%

This model predicts one of six categories:

- AI
- Data
- DevOps
- Engineering
- Product
- Security
"""
)

st.sidebar.header("Input Guide")

st.sidebar.write("""
Enter realistic values for each feature before clicking **Predict Category**.
""")

# Layout
col1, col2 = st.columns(2)

with col1:
    demand_count = st.number_input(
        "Demand Count",
        min_value=0,
        value=1000
    )

    demand_pct = st.number_input(
        "Demand Percentage",
        min_value=0.0,
        value=5.0
    )

    median_days_open = st.number_input(
        "Median Days Open",
        min_value=0.0,
        value=30.0
    )

with col2:
    salary_premium_pct = st.number_input(
        "Salary Premium Percentage",
        value=10.0
    )

    repost_rate_pct = st.number_input(
        "Repost Rate Percentage",
        value=5.0
    )

    scarcity_score = st.number_input(
        "Scarcity Score",
        value=50.0
    )

if st.button("Predict Category"):

    input_data = pd.DataFrame({
        "demand_count": [demand_count],
        "demand_pct": [demand_pct],
        "median_days_open": [median_days_open],
        "salary_premium_pct": [salary_premium_pct],
        "repost_rate_pct": [repost_rate_pct],
        "scarcity_score": [scarcity_score]
    })

    prediction = pipeline.predict(input_data)[0]

    st.success(f"🎯 Predicted Skill Category: **{prediction.upper()}**")

st.markdown("---")

with st.expander("About this Project"):

    st.write("""
This project demonstrates a complete machine learning workflow:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Scaling
- KNN Classification
- Model Evaluation
- Pipeline Creation
- Streamlit Deployment

**Dataset Size:** 1,635 records

**Target Variable:** Category
""")

st.markdown("---")

st.caption(
    "Developed using Python, Scikit-learn, Streamlit, Pandas, NumPy, and Joblib."
)