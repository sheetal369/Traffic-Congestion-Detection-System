import streamlit as st

st.set_page_config(
    page_title="My App Title",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        /* Add your CSS styles here */
    </style>
    """,
    unsafe_allow_html=True
)

# Rest of your app code goes here
