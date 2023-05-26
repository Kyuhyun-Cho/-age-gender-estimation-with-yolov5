import torch
from PIL import Image
import numpy as np
import json
import requests
import sys
import io

# if len(sys.argv) > 1:
server_url = 'http://localhost:3000/'

# Initialize the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5/runs/train/age_gender_detect/weights/best.pt')
model.conf = 0.4  # confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.classes = None  # filter by class
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
# device = torch.device('cpu')
model.to(device).eval()

# Load image
response = requests.get(server_url)
img = Image.open(io.BytesIO(response.content))
img.show()

img = np.array(img)
print(img.shape)

# Perform inference
with torch.no_grad():
    results = model([img], size=640)  # includes NMS

# Find the largest bounding box
if len(results.pred[0]) > 0:  # if there is at least one detection
    max_area = 0
    max_class = None
    for *box, conf, cls in results.pred[0]:
        x1, y1, x2, y2 = box
        area = (x2 - x1) * (y2 - y1)
        if area > max_area:
            max_area = area
            max_class = cls.int().item()

    if max_class is not None:
        # Get the class name
        class_name = model.names[max_class]

        # Create a JSON response
        json_data = json.dumps({"class": class_name})
else:
    json_data = json.dumps({"class": "00-39 MALE"})

print("Age & Gender JSON data:", json_data)

# Server URL
# url = "http://localhost:3000"

# Create a Post request with JSON data and send to servers
response = requests.post(server_url, json=json_data, headers = {'Content-Type': 'application/json'} )

# Print response of server
print(response.json())

# else:
#     print("Please enter Image Path")