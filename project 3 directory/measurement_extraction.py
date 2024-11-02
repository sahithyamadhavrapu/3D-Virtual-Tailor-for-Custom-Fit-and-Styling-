import cv2

def capture_body_image():
    cap = cv2.VideoCapture(0)
    print("Press 'c' to capture an image for measurement.")
    
    while True:
        ret, frame = cap.read()
        cv2.imshow('Press c to capture', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Save image when 'c' is pressed
            cv2.imwrite('body_image.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Image captured and saved as 'body_image.jpg'.")

def estimate_measurements(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Here we would process the image to estimate measurements.
    # For simplicity, let's assume we return approximate values.
    measurements = {
        "chest": 90,   # in cm
        "waist": 70,   # in cm
        "hips": 95     # in cm
    }
    
    print(f"Estimated Measurements: {measurements}")
    return measurements

# Run the body capture and measurement estimation
if __name__ == "__main__":
    capture_body_image()
    measurements = estimate_measurements('body_image.jpg')
