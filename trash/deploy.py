from roboflow import Roboflow
rf = Roboflow(api_key="kzQBwM6FFB2h2Pclu9AK")
project = rf.workspace("sxc").project("traffic-congestion-detection")
model = project.version(6).model

# infer on a local image
#print(model.predict("your_image.jpg", confidence=40, overlap=30).json())
