import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Pub App",
    page_icon="👋",
)

html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h1 style="color:white;text-align:center;">Streamlit Nearest Pub App 🍻 </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.title("🏠Home Page")
st.header("Welcome to Open Pub Application  🥂")
st.sidebar.success("Select a page above.")

from PIL import Image
img = Image.open("pub.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=1200)

# load the data
df=pd.read_csv('pubs_data.csv')
st.subheader("There  are  {}  Pubs  in  United Kingdom".format(df.shape[0]))
info = st.selectbox('',('Head','Tail'))

if info=='Head':
    st.dataframe(df.head())

elif info=='Tail':
    st.dataframe(df.tail())

st.subheader('Satistical Analysis')    
if st.button('Search'):
    st.dataframe(df.describe())




