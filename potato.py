from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from inference_sdk import InferenceHTTPClient
from datetime import datetime
import cv2
import threading

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///detections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Detection model
class Detection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Float, nullable=False)
    image_width = db.Column(db.Integer, nullable=False)
    image_height = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    class_id = db.Column(db.Integer, nullable=False)
    detection_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
with app.app_context():
    db.create_all()

# Initialize the inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="pcwYMWd7eJ8hHyBeVtyU"
)

@app.route('/infer_and_save', methods=['POST'])
def infer_and_save():
    image_url = request.json['image_url']
    result = CLIENT.infer(image_url, model_id="potato-eruvaka/3")
    
    if result and 'predictions' in result:
        prediction = result['predictions'][0]
        detection = Detection(
            time=result.get('time', 0),
            image_width=result['image']['width'],
            image_height=result['image']['height'],
            x=prediction['x'],
            y=prediction['y'],
            width=prediction['width'],
            height=prediction['height'],
            confidence=prediction['confidence'],
            class_name=prediction['class'],
            class_id=prediction['class_id'],
            detection_id=prediction['detection_id']
        )
        db.session.add(detection)
        db.session.commit()
        return jsonify({'message': 'Detection added successfully', 'detection': detection.id}), 201
    
    return jsonify({'message': 'No predictions found'}), 400

@app.route('/detections', methods=['GET'])
def get_detections():
    detections = Detection.query.all()
    return jsonify([{
        'time': det.time,
        'image': {
            'width': det.image_width,
            'height': det.image_height
        },
        'predictions': [{
            'x': det.x,
            'y': det.y,
            'width': det.width,
            'height': det.height,
            'confidence': det.confidence,
            'class': det.class_name,
            'class_id': det.class_id,
            'detection_id': det.detection_id
        }]
    } for det in detections])

if __name__ == '__main__':
    app.run(debug=True)
















# from inference_sdk import InferenceHTTPClient

# CLIENT = InferenceHTTPClient(
#     api_url="https://detect.roboflow.com",
#     api_key="pcwYMWd7eJ8hHyBeVtyU"
# )

# image_url = "assets/images/p3.jpeg"
# result = CLIENT.infer(image_url, model_id="potato-eruvaka/3")

# print(result)