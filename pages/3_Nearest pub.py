from turtle import distance
import streamlit as st
import numpy as np
import pandas as pd

df=pd.read_csv('pubs_data.csv')

html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h1 style="color:white;text-align:center;">Find the Nearest Pub 🔎  </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

st.header('Location of Nearest pubs based on given inputs')

lat=st.number_input('latitude')
lon=st.number_input('longitude')
new_df=df[['latitude','longitude']]
inputs=np.array([lat,lon])
distance=np.sqrt(np.sum((inputs-new_df)**2, axis=1))
k = 5
nearest_neighbor = distance.argsort()[:k]

if st.button('search'):
    st.text("The locations corresponding to Nearest 5 Pubs ")
    st.map(df.iloc[nearest_neighbor])
    st.dataframe(df.iloc[nearest_neighbor])

