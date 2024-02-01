import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Indraneel Jain")
    content = """ Hi , I am a python developer, 
     i graduated in 2020,
     i worked at Infosys with 2 years of experience
     WELCOME to my Portfolio   """
    st.info(content)