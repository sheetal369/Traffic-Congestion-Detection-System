import time
import streamlit as st
import torch
from PIL import Image
import torchvision.transforms as transforms
import trash.count2 as ct

# Load the model
model = torch.hub.load('yolov5', 'custom', path='models/best_with_changsin', source='local')

# Define image transformations
transform = transforms.Compose([
    transforms.Resize((640, 640)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Function to predict on uploaded image
def predict(image):
    # Preprocess the image
    image = Image.open(image).convert('RGB')
    image = transform(image).unsqueeze(0)

    total_counts = dict()
    class_names = None

    # Pass the image to the model
    detection_res = model(image)
    st.write(detection_res)

    if not class_names:
        class_names = detection_res.names

    counts = ct.count_vehicles(detection_res, confidence_threshold=0.5)
    st.empty()
    # print(os.path.basename(filename), counts)
    total_counts = ct.add_dicts(total_counts, counts)

    # print counts for each class name
    print("\nTotal counts:")
    ct.print_class_counts(total_counts, class_names)
    time.sleep(5)
    ct.feedback_message()
    return total_counts
    
    # Return the output
    return output

# Create a file uploader
uploaded_file = st.file_uploader("Choose an image :", type=["jpg", "jpeg", "png"])

# Make a prediction when a file is uploaded
if uploaded_file is not None:
    output = predict(uploaded_file)
    st.write(output)

