from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_request():
    if request.method == 'GET':
        image_path = os.path.abspath('./yolov5/test_data/grandma.jpg')

        if os.path.exists(image_path):
            try:
                return send_file(image_path, mimetype='image/jpeg')
            except FileNotFoundError:
                return {"error": "Image file not found"}, 404
        else:
            return {"error": "Image file not found"}, 404
        
    elif request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            json_data = request.get_json()
            print("Age & Gender", json_data)
            response_data = {"message": "Received the JSON data successfully"}
            return jsonify(response_data)
        else:
            return {"error": "Unsupported Media Type"}, 415
    else:
        return {"error": "Method not allowed"}, 405

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
