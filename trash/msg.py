import torch
import streamlit as st
from PIL import Image
import os
import pywhatkit
import datetime

import count

model = torch.hub.load('yolov5', 'custom', path='models/bestc', source='local')


# Define Streamlit app
def main():
    st.title('Traffic Congestion Detection')
    
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
    # No image uploaded
        st.write("Please upload an image")
    
    
# Add a button to copy the traffic status to the clipboard
    # Add a button to share the traffic status via WhatsApp
    if st.button('Share traffic status via WhatsApp'):
        now = datetime.datetime.now()
        pywhatkit.sendwhatmsg('+9779867567762', 'Traffic is congested!', now.hour, now.minute)
        st.write('Traffic status shared via WhatsApp.')

if __name__ == '__main__':
    main()