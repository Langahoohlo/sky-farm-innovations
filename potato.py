from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from inference_sdk import InferenceHTTPClient
from datetime import datetime
import cv2
import threading

# Import the InferencePipeline object
from inference import InferencePipeline
# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes

import os
from dotenv import load_dotenv

roboflow_api_key = os.getenv('ROBOFLOW_API_KEY')

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
    timestamp = db.Column(db.DateTime, default=datetime.now)

# Initialize the database
with app.app_context():
    db.create_all()

# Initialize the inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=roboflow_api_key
)

@app.route('/infer_and_save', methods=['GET'])
def infer_and_save():
    image_url = 'assets/images/p4.jpeg'
    result = CLIENT.infer(image_url, model_id="potato-eruvaka/3")
    
    if result and 'predictions' in result:
        detections = []
        for prediction in result['predictions']:
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
            detections.append(detection)
        
        db.session.commit()
        
        return jsonify({'message': 'Detections added successfully', 'detection_ids': [d.id for d in detections]}), 201
    
    return jsonify({'message': 'No predictions found'}), 400

from uuid import uuid4

@app.route('/infer_video', methods=['GET'])
def infer_video():
    video_path = 'assets/videos/potato_digging.mp4'
    cap = cv2.VideoCapture(video_path)
    all_detections = []

    if not cap.isOpened():
        return jsonify({'message': 'Error opening video file'}), 400

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Generate a unique filename for each frame
        filename = f"{uuid4()}.jpg"
        filepath = os.path.join('/tmp', filename)

        # Save the frame as an image file
        cv2.imwrite(filepath, frame)

        # Perform inference using the saved image file
        result = CLIENT.infer(filepath, model_id="potato-eruvaka/3")

        if result and 'predictions' in result:
            for prediction in result['predictions']:
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
                all_detections.append(detection)

        # Clean up the local image file after inference
        os.remove(filepath)

    cap.release()
    db.session.add_all(all_detections)
    db.session.commit()

    return jsonify({'message': 'Detections added successfully', 'detection_ids': [d.id for d in all_detections]}), 201

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