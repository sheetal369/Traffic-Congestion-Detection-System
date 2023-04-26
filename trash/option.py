import streamlit as st

# Add the "Check traffic status" button
if st.button(label='Check traffic status', help='Click to check traffic status'):
    # Code to check traffic status
    st.write('auto')

# Add a separator
st.write('---')

# Add the "Upload your own image" button
if st.button('Upload your own image'):
    # Code to upload and process image
    st.write('own')