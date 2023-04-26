import torch
import streamlit as st
from PIL import Image
import os
import count

model = torch.hub.load('yolov5', 'custom', path='models/best_TCD.pt', source='local')


# Define Streamlit app
def main():
    st.set_page_config(
        page_title="Traffic Congestion Detection",
        page_icon="🚗",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title('Traffic Congestion Detection')
    button_styles = """
    <style>
    .stButton button {
        background-color: #0072B2;
        border: none;
        color: #FFFFFF;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px #000000;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: #00427C;
        box-shadow: 1px 1px 3px #000000;
    }
    .stButton button:active {
        background-color: #0072B2;
        box-shadow: 0px 0px 1px #000000;
        transform: translateY(2px);
    }
    </style> """

    # Display the button with the custom CSS styles
    st.markdown(button_styles, unsafe_allow_html=True)
    if st.button('Check traffic status', help='Click to check traffic status'):
        count.count_vehicles_total(model, 'images')
    st.write('---')

    st.write('**Upload your own image**')
    # Code to upload and process image
    image = st.file_uploader("Choose an image :", type=["jpg", "jpeg", "png"])
        
    if image is not None:
        imgpath = os.path.join('images', image.name)
        result = model(imgpath)
        st.image(image, width=500, use_column_width=False, clamp=True)
        count.count_vehicles(result)
    else:
        st.write("Please upload an image")

            
    
    count.feedback_message()

if __name__ == '__main__':
    main()