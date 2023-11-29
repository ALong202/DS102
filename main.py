import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Data Visualization')
st.header('Upload Data File')

data_file = st.file_uploader("Choose a CSV file", type=('.csv'))
if data_file is not None:
    df = pd.read_csv(data_file)

    st.header('Show Data')
    st.dataframe(df)

    st.header('Descriptive Statistics')
    st.table(df.describe())
    
    st.header('Show Data Information')
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.header('Visualize Each Attribute')
    for col in list(df.columns):
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        plt.xlabel(col)  # Corrected from plt.xlable(col)
        plt.ylabel('Quantity')  # Corrected from plt.ylable('Quantity')
        st.pyplot(fig)

    
    st.header('Show correlation between variables ')
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(method='pearson'), ax = ax, vmax = 1, square = True, annot = True, cmap = 'Reds'
    st.write(fig)
    
    
    
    
    
    
    
    


  
    
