import torch
import streamlit as st
from PIL import Image

#import count
import trash.count_new as count_new
#Custom Trained
model = torch.hub.load('yolov5', 'custom', path='models/best_with_changsin', source='local')

# Define Streamlit app
def main():
    st.title('Traffic Congestion Detection')
    
    uploaded_file = st.file_uploader("Choose an image :", type=["jpg", "jpeg", "png"])
    count_new.count_vehicles_total(model, uploaded_file)


if __name__ == '__main__':
    main()