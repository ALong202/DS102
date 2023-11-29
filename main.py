import streamlit as st
import pandas as pd
import io


st.title('Data Visualization')
st.header('Upload Data File')

data_file = st.file_uploader("Choose a CSV file", type=('.csv'))
if data_file is not None:
    df = pd.read_csv(data_file)

    st.header('Show Data')
    st.dataframe(df)

    st.header('Descriptive Statistics')
    st.table(df.describe())
    st.header('Show data infomation')
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())
  
    
