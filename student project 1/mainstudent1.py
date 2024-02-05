import streamlit as st
import pandas
st.set_page_config(layout="wide")

st.title("The Best Company")
content = """The Best Company is a global leader in next-generation digital services and consulting. 
             We enable clients in more than 56 countries to navigate their digital transformation. """
st.info(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data1.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images1/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images1/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images1/" + row["image"])
