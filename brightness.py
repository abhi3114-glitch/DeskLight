import cv2
import numpy as np

def calculate_brightness(frame):
    """
    Calculates the average brightness of a frame.
    Converts frame to grayscale and returns the mean pixel intensity.
    """
    if frame is None:
        return 0
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate mean brightness
    brightness = np.mean(gray)
    return brightness

def get_brightness_status(brightness, low_threshold=80, high_threshold=180):
    """
    Determines status based on brightness level.
    Returns: status string, color code
    """
    if brightness < low_threshold:
        return "Too Dark", "#FF4B4B"  # Red
    elif brightness > high_threshold:
        return "Too Bright", "#FFA500" # Orange
    else:
        return "Ideal", "#00C851" # Green
