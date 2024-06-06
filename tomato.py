# Before you run this app please do this first in the terminal export ROBOFLOW_API_KEY=<your api key> replace your api key with your actual api key

import os
from inference import get_model
import supervision as sv
import cv2
from dotenv import load_dotenv

load_dotenv()

roboflow_api_key = os.getenv('ROBOFLOW_API_KEY')

# Define the video file path
video_file = "assets/videos/potato_digging.mp4"

# Load a pre-trained YOLOv8n model
model = get_model(model_id="potato-eruvaka/3")

# Open the video file
cap = cv2.VideoCapture(video_file)

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Create supervision annotators
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

# Loop through each frame of the video
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Break out of the loop if no frame is returned
    
    # Run inference on the frame
    results = model.infer(frame)[0]
    detections = sv.Detections.from_inference(results)
    # detections = sv.Detections.from_roboflow(results[0].dict(by_alias=True, exclude_none=True))
    
    # Print detected objects
    for detection in detections:
        print(detections)
    
    # Annotate the frame with inference results
    annotated_frame = bounding_box_annotator.annotate(
        scene=frame, detections=detections)
    annotated_frame = label_annotator.annotate(
        scene=annotated_frame, detections=detections)
    
    # Display or save the annotated frame
    cv2.imshow('Annotated Frame', annotated_frame)
    
    # Check for the 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
