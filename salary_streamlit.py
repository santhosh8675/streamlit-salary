import streamlit as st
import joblib
import numpy as np
import pandas as pd
# Load the saved model
model = joblib.load('salary_prediction_model_new.pkl')
base_salary_df = pd.read_csv("ex_sal - Sheet1.csv")
# Set the background color to white using custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# Display an image at the top
st.image("l.png", use_column_width=True)  # Replace 'your_image.png' with your image path

st.title("Incentive Calculator")

# Create input fields for the features
experience_years = st.number_input('Experience Years', min_value=0, max_value=30)
hours_worked_per_week = st.number_input('Hours Worked Per Week', min_value=0)
productivity_score = st.number_input('Productivity Score', min_value=0.0, max_value=100.0)
performance_score = st.number_input('Performance Score', min_value=0.0, max_value=100.0)
skill_level = st.number_input('Skill Level', min_value=1, max_value=5)
defect_rate = st.number_input('Defect Rate', min_value=0.0, max_value=100.0)
# attendance_rate = st.number_input('Attendance Rate', min_value=0.0, max_value=100.0)

# Prediction button
if st.button('Predict Salary and Incentive'):
    # Make prediction using input values
    features = np.array([[experience_years]])
    predicted_salary = model.predict(features)[0]

    # Find the base salary for the given experience
    base_salary = base_salary_df.loc[base_salary_df['Experience'] == experience_years, 'Base_Salary'].values[0]
    
    # Calculate incentive (predicted salary - base salary)
    incentive =  abs(predicted_salary) - base_salary
    
    # Display the results
    st.write(f"Predicted Salary: ₹{predicted_salary:.2f}")
    st.write(f"Base Salary: ₹{base_salary:.2f}")
    st.write(f"Incentive: ₹{incentive:.2f}")
