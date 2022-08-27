import streamlit as st
import pandas as pd

df=pd.read_csv('pubs_data.csv')

html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h1 style="color:white;text-align:center;"> Pub Locations 🗺️  </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)


st.title('Pub locations based On Local Authority or Postal code')

opt=st.selectbox('',('Local Authority','Postal Code'))
if opt=='Local Authority':
    option=st.selectbox(opt,df.local_authority.unique())

    if st.button("Search"):
        pubs_data = df.loc[df["local_authority"]==option]
        "You searched for:",option
        "Total no of pubs in this location is:",len(pubs_data)
        st.map(pubs_data)
        st.dataframe(pubs_data)
else:
    pc=st.selectbox(opt,df.postcode.unique())

    if st.button("Search"):
        pubs_data = df.loc[df["postcode"]==pc]
        "You searched for:",pc
        "Total no of pubs in this location is:",len(pubs_data)
        st.map(pubs_data)
        st.dataframe(pubs_data)


  