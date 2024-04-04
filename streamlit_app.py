import streamlit as st
import pandas as pd
import numpy as np
import pickle 
#to load a saved model
import base64  
#to open .gif files in streamlit app

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
  feature_dict = {"No":1,"Yes":2}
  for key,value in feature_dict.items():
    if val == key:
      return value
      
def get_value(val, my_dict):
  for key,value in my_dict.items():
    if val == key:
      return value
      
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode == 'Home':
  st.title('LOAN PREDICTION :')
  st.image('loan_image.jpg')
  st.markdown('Dataset :')
  data=pd.read_csv('loan_dataset.csv')
  st.write(data.head())
  st.markdown('Applicant Income VS Loan Amount ')
  st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))
