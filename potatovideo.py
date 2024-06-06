from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from inference_sdk import InferenceHTTPClient
from datetime import datetime
import cv2
import os
import tempfile
from dotenv import load_dotenv

load_dotenv()

roboflow_api_key = os.getenv('ROBOFLOW_API_KEY')

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///detections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Detection model
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
    api_key=roboflow_api_key
)

def process_frame(frame):
    # Save frame as a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_file_path = temp_file.name
    cv2.imwrite(temp_file_path, frame)
    temp_file.close()

    # Perform inference using the temporary file path
    result = CLIENT.infer(temp_file_path, model_id="potato-eruvaka/3")

    # Remove the temporary file
    os.remove(temp_file_path)

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

        # Draw bounding box on the frame
        x = int(prediction['x'])
        y = int(prediction['y'])
        width = int(prediction['width'])
        height = int(prediction['height'])
        start_point = (x - width // 2, y - height // 2)
        end_point = (x + width // 2, y + height // 2)
        color = (0, 255, 0)  # Green color for bounding box
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
        frame = cv2.putText(frame, prediction['class'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

    return frame

def gen_frames(video_path):
    # cap = cv2.VideoCapture(0)  # Capture video from webcam
    cap = cv2.VideoCapture(video_path)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = process_frame(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    video_path = request.args.get('video_path')  # Retrieve 'video_path' parameter from the URL query string
    if not video_path or not os.path.exists(video_path):
        return "Error: Video file path is invalid or file does not exist.", 400
    return Response(gen_frames(video_path), mimetype='multipart/x-mixed-replace; boundary=frame')


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
