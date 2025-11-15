import streamlit as st

st.title('CALCULATE YOUR BMI')
wt = st.number_input('Enter your weight in KGs:')
h = st.number_input('Enter your height in Ms:')
if h == 0:
    bmi = 0
else:
    bmi = wt/h**2
st.success(f'Your BMI is {round(bmi)} KG/M^2')