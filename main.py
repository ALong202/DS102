import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt


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
    
    st.header('Visualize each attribute')
    for col in list(df.columns):
        fig, ax = plt.subplots()
        ax.hist(df[col], bins =20)
        plt.xlable(col)
        plt.ylable('Quantity')
        st.pyplot(fig)
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    


  
    
