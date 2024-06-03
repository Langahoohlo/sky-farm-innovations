from ultralytics import YOLO
import cv2

def process_image(image_path):
    model = YOLO('yolov8x.pt')

    objects_rec = []

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    # Run the YOLOv8 model on the image
    results = model(image)
    annotated_image = results[0].plot()

    # Iterate through detections and add them to the list
    for detection in results[0].boxes:
        class_id = detection.cls
        confidence = detection.conf
        label = model.names[class_id]
        objects_rec.append((label, confidence.item()))

    # Display the results
    cv2.imshow('YOLOv8 Detection', annotated_image)

    # Print the detected objects and their confidence scores
    print(objects_rec)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_image('cb2.jpeg')
