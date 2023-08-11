
import streamlit as st
from src.utils import data_import 

st.title("Coin Market Capital Updated Dataset")


df = data_import('Dataset/API.csv')
df.drop(
    'Unnamed: 0' , axis = 1
)
st.dataframe(df)

st.download_button(
    label = 'Download Latest dataset' , data = 'API.csv' , file_name='API.csv')

