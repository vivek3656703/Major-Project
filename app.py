import streamlit as st
import joblib
model = joblib.load('Sentiment_Analysis02')
st.title('Sentiment_Analysis Check')
ip = st.text_input('Enter your sentiment')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op)
   
       
         
