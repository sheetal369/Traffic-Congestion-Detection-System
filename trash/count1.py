import time
import streamlit as st
import torch
from PIL import Image
import torchvision.transforms as transforms

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

    # Pass the image to the model
    output = model(image)

    # Return the output
    return output

# Create a file uploader
uploaded_file = st.file_uploader("Choose an image :", type=["jpg", "jpeg", "png"])

# Make a prediction when a file is uploaded
if uploaded_file is not None:
    output = predict(uploaded_file)
    st.write(output)

def count_vehicles_total(model, path, file_type="*.jpg", confidence_threshold=0.5):
    detection_res = model(filename) #detection_result
    if not class_names:
        class_names = detection_res.names

        counts = count_vehicles(detection_res, confidence_threshold=confidence_threshold)
        st.empty()
        # print(os.path.basename(filename), counts)
        total_counts = add_dicts(total_counts, counts)

    # print counts for each class name
    print("\nTotal counts:")
    print_class_counts(total_counts, class_names)
    time.sleep(5)
    #feedback_message()
    return total_counts

def count_vehicles(detection_res, confidence_threshold=0.5):
  counts = dict()
  # print(res.names.index('car'), res.names.index('bus'), res.names.index('truck'))

  for pred in detection_res.xyxyn[0]:
    confidence = pred[-2]
    if confidence > confidence_threshold:
      # print(pred)

      class_id = int(pred[-1])
      counts = dict_increment(counts, class_id)
  
  
  print_class_counts(counts, detection_res.names)
  return counts


def dict_increment(dict1, key):
  if key in dict1.keys():
    dict1[key] = dict1[key] + 1 
  else:
    dict1[key] = 1
  return dict1


def print_class_counts(dict1, class_names):
  # print counts for each class name
    vehicle_counts = dict()
    for key, val in dict1.items():
        vehicle_counts[class_names[key]] = val

    df = pd.DataFrame.from_dict(vehicle_counts, orient='index', columns=['Counts'])
    df.index.name = 'Vehicles'

    # Display the dataframe
    st.dataframe(df)

    if df['Counts'].sum() < 20 :
          st.warning("There is a no traffic ahead")
    else :
          st.warning("There is a traffic ahead")
          
def add_dicts(dict1, dict2):
  dict3 = dict()

  for key1, val1 in dict1.items():
    dict3[key1] = val1
    if key1 in dict2.keys():
      dict3[key1] = val1 + dict2[key1]

  for key2, val2 in dict2.items():
    if key2 not in dict1.keys():
      dict3[key2] = val2

  return dict3


def add_dicts(dict1, dict2):
  dict3 = dict()

  for key1, val1 in dict1.items():
    dict3[key1] = val1
    if key1 in dict2.keys():
      dict3[key1] = val1 + dict2[key1]

  for key2, val2 in dict2.items():
    if key2 not in dict1.keys():
      dict3[key2] = val2

  return dict3