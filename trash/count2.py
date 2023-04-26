import glob
import os
import streamlit as st
import pandas as pd
import time
from PIL import Image
import torchvision.transforms as transforms

CLASSES = ['Bus', 'Car', 'Motorcycle', 'Truck']

def count_vehicles_total(model, image, confidence_threshold=0.5):
  total_counts = dict()
  class_names = None

  # Set the background color and font style of the table
  detection_res = predict(model, image) #detection_result
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
  feedback_message()
  return total_counts


# Define image transformations
transform = transforms.Compose([
    transforms.Resize((640, 640)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Function to predict on uploaded image
def predict(model, image):
    # Preprocess the image
    image = Image.open(image).convert('RGB')
    image = transform(image).unsqueeze(0)

    # Pass the image to the model
    output = model(image)

    # Return the output
    return output

def feedback_message():
    with st.sidebar:
      st.subheader("Evaluate Output Accuracy")
      answer = st.radio("Is the output accurate according to the image provided?", ("Yes", "No"))
      st.write("Thank You for your feed")





def glob_files(path, file_type="*"):
    search_string = os.path.join(path, file_type)
    files = glob.glob(search_string)
    # print('searching ', path)
    paths = []
    for f in files:
      if os.path.isdir(f):
        sub_paths = glob_files(f + '/')
        paths += sub_paths
      else:
        paths.append(f)

    # We sort the images in alphabetical order to match them
    #  to the annotation files
    paths.sort()
    return paths

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
