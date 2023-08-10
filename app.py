import streamlit as st
import joblib
st.title("Unerweight/Normal/Overweight Predictor")
st.title("Unerweight/Normal/Overweight Predictor")
weight=st.slider('What is your weight?',min_value=0, max_value=100, value=25, format=None, key=None, help=None, args=None, kwargs=None, label_visibility="visible")
height=st.slider('What is your height?', min_value=0, max_value=200, value=48)

model=joblib.load('model_new')
result=model.predict([[weight,height]])[0]

if st.button("Predict"):
  st.write(f"You are {result}")
  if result=='Overweight':
    st.write("Go HIT GYM")
  if result=='Underweight':
    st.write('Eat Something BRO')
  if result=='Normal':
    st.write('GREAT JOB!!')
