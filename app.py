
import streamlit as st
import pandas as pd 

st.title("Coin Market Capital Updated Dataset")

filepath = "Dataset/API.csv"
df = pd.read_csv(filepath)

df.drop(
    'Unnamed: 0' , axis = 1
)
st.dataframe(df)

st.download_button(
    label = 'Download Latest dataset' , data = 'API.csv' , file_name='API.csv')

