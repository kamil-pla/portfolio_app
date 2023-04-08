import streamlit as st
import pandas

st.set_page_config(layout="wide")

my_name = "Kamil Pierzchała"

content1 = """
I am beginner Python programmer. 
Professionally, I was born as a manufacturing engineer in automotive industry and 
since then took several positions transiting towards IT related areas. So far, I have been working in several ERP 
systems in the areas of data analysis, project management, UAT/testing, key user roles and team leading of 
engineers. 

In terms of environment I have been discovering manufacturing field, IT software house practices, acting as 
freelance consultant, learning smooth cooperation with clients, suppliers, software engineers and developers, 
working through wide engineering, ecommerce and finally ERP and IT topics.
"""

content2 = """
Below you may find my initial portfolio of apps which I created while learning coding. 
As a first step I started from Python and learning basics of Git, HTML, CSS and SQL.
"""

col1, col2, col3 = st.columns([1, 3, 6])  # set width ratios for columns


with col1:
    st.write("")

with col2:
    st.image("images/photo.png", width=400)

with col3:
    st.title(my_name)
    st.write(content1)
    st.write(content2)

col4, col5 = st.columns(2)

with col4:
    df = pandas.read_csv("data.csv", sep=";")
    for i, row in df[:10].iterrows():
        st.header(row["title"])

with col5:
    df = pandas.read_csv("data.csv", sep=";")
    for i, row in df[10:].iterrows():
        st.header(row["title"])