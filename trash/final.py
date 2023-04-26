import torch
import streamlit as st
from PIL import Image
import os

import count

#Custom Trained
model = torch.hub.load('yolov5', 'custom', path='models/bestc', source='local')

# Define Streamlit app
def main():

    st.title('Traffic Congestion Detection')
    image = st.file_uploader("Choose an image :", type=["jpg", "jpeg", "png"])
    if image is not None:
        imgpath = os.path.join('images', image.name)
        rst = model(imgpath)
        st.write(rst)
        st.image(image, width=500, use_column_width=False, clamp=True)
        count.count_vehicles(rst)

if __name__ == '__main__':
    main()