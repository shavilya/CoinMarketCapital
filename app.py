
import streamlit as st
import pandas as pd 

st.title("Coin Market Capital Updated Dataset")

filepath = "API.csv"
df = pd.read_csv(filepath)

df.drop(
    'Unnamed: 0' , axis = 1
)
st.dataframe(df)

rows = df.shape[0]
cols = df.shape[1]

st.markdown("Shape of Dataset")
col1,col2 = st.columns(2)

col1.metric(label = 'Rows' , value = rows) 
col2.metric(label = 'Columns' , value = cols)

st.download_button(
    label = 'Download Latest dataset' , data = 'API.csv' , file_name='API.csv'
)