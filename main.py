import streamlit as st
import pandas as pd

st.title('Data Visualization')
st.header('Upload Data File')

data_file = st.file_uploader("Choose a CSV file", type=('.csv'))
if data_file is not None:
    df = pd.read_csv(data_file)

    st.header('Show Data')
    st.dataframe(df)

    st.header('Descriptive Statistics')
    st.table(df.describe())

df.info()
  
    
