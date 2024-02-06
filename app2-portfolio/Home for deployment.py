import streamlit as st
import pandas
import os

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("app2-portfolio/images/photo.png")
    image_path = "app2-portfolio/images/photo.png"
    if os.access(image_path, os.R_OK):
        print("file is readable")
    else:
        print("file is not readable ")

with col2:
    st.title("Indraneel Jain")
    content = """ Hi , I am a python developer, 
     i graduated in 2020,
     i worked at Infosys with 2 years of experience
     on Python,sql,oracle\n\nWELCOME to my Portfolio   """
    st.info(content)

content2 = """ Below you can find 
               some of the projects that
                i worked upon....."""

st.write(content2)

col3, emptycol, col4 = st.columns([1.5, 0.5, 1.5])  # dividing the my projects in two coloumns

df = pandas.read_csv("app2-portfolio/data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("app2-portfolio/images/" + row[
            "image"])  # because images are not in the Home.py directory but rather in image folder
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("app2-portfolio/images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

# final
