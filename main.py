import streamlit as st

st.set_page_config(layout="wide")

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
    st.markdown(
        f"""
        <div class="container d-flex justify-content-center">
            <div class="content">
                <h1 class="text-center">Kamil Pierzchała</h1>
                <p>{content1}</p>
                <p>{content2}</p>
            </div>
        </div>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-twekYlQ5+pbDLBJq0CTh7JGGzKGmRUE7dMM0pP8hO9uYp1CFszdG+IOb2hJtXTj" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="./style.css">
        """
        , unsafe_allow_html=True
    )
