import json
import torch
import base64
import numpy as np
from io import BytesIO
from PIL import Image

def model_init():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./model/best.pt')
    model.conf = 0.4  # confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.classes = None  # filter by class
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device).eval()
    print("complete model loading")
    return model

def get_class_json(model, encoded_img):
    # Perform inference
    img = Image.open(BytesIO(base64.b64decode(encoded_img)))
    img = np.array(img)
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
            return json_data
    else:
        json_data = json.dumps({"class": "00-39 MALE"})
        return json_data