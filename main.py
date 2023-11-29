from streamlit as st
import pandas as pd

st.title('Data visualization')
st.header('Upload data file')

data_file = st.file_uploader("Choose a csv file", type =(['.csv']))
if data_file is not None:
    df = pd.read_csv(data_file)

    st.header('Show data')
    st.dataframe(df)

st.header('Descripite statictics')
st.table(df.describle())

  
    
