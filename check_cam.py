import cv2
import time

print("--- Camera Diagnostic ---")
print(f"OpenCV Version: {cv2.__version__}")

def test_backend(index, backend_name, backend_id):
    print(f"\nTesting Camera {index} with {backend_name}...")
    try:
        if backend_id is not None:
            cap = cv2.VideoCapture(index, backend_id)
        else:
            cap = cv2.VideoCapture(index)
        
        if not cap.isOpened():
            print(f"FAILED: Could not open camera {index} with {backend_name}")
            return False
            
        ret, frame = cap.read()
        if ret:
            print(f"SUCCESS: Read frame {frame.shape} from camera {index} with {backend_name}")
            cap.release()
            return True
        else:
            print(f"FAILED: Opened but could not read frame from camera {index} with {backend_name}")
            cap.release()
            return False
    except Exception as e:
        print(f"ERROR: Exception testing {backend_name}: {e}")
        return False

# Test Default
test_backend(0, "Default", None)

# Test DSHOW
test_backend(0, "CAP_DSHOW", cv2.CAP_DSHOW)

# Test MSMF
test_backend(0, "CAP_MSMF", cv2.CAP_MSMF)

print("\n--- End Diagnostic ---")
