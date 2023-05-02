import torch
import streamlit as st
from PIL import Image
import os

import count

#Custom Trained
model = torch.hub.load('yolov5', 'custom', path='models/best_TCD.pt', source='local')

# Define Streamlit app
def main():
    st.set_page_config(
        page_title="Traffic Congestion Detection",
        page_icon="👮‍♂️",)
    st.title('Traffic Congestion Detection')
    image = st.file_uploader("**Choose an image :**", type=["jpg", "jpeg", "png"])
    
    if image is not None:
        imgpath = os.path.join('images', image.name)
        result = model(imgpath)
        st.image(image, width=500, use_column_width=False, clamp=True)
        count.count_vehicles(result)
        count.feedback_message()
    else:
        st.write("Please upload an image")

if __name__ == '__main__':
    main()