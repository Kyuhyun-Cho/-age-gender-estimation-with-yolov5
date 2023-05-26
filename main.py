from flask import Flask, request, jsonify
from prediction import model_init, get_class_json

app = Flask(__name__)

model = model_init()

@app.route('/get_class', methods=['POST'])
def get_calss():
    try:
        param = request.get_json()
        image = param['image'].split(",")[1]

    except Exception as e:
        return jsonify({'Error': 'Invalid parameter'}), 400
    
    try:
        result = get_class_json(model, image)
        return result
    
    except Exception as e:
        return jsonify({'Error': 'Error occur in inference'}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=3001, debug=True)