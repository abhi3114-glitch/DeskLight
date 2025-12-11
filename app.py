import streamlit as st
import cv2
import numpy as np
import pandas as pd
import time
from brightness import calculate_brightness, get_brightness_status

st.set_page_config(page_title="DeskLight", page_icon="💡", layout="wide")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

if 'run' not in st.session_state:
    st.session_state.run = False

def main():
    st.title("💡 DeskLight: Ambient Light Detector")
    
    # Sidebar
    st.sidebar.header("Settings")
    low_threshold = st.sidebar.slider("Minimum Brightness", 0, 255, 80)
    high_threshold = st.sidebar.slider("Maximum Brightness", 0, 255, 180)
    
    demo_mode = st.sidebar.checkbox("Demo Mode", value=False)
    
    start_button = st.sidebar.button("Start/Stop Webcam")
    
    if start_button:
        st.session_state.run = not st.session_state.run

    # Camera Selection
    camera_index = st.sidebar.selectbox("Camera Index", [0, 1, 2], index=0)

    # Placeholders initialized in columns below
    
    cap = None
    if st.session_state.run and not demo_mode:
        cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    
    
    # Define layout columns
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Live Feed")
        image_placeholder = st.empty()
        image_placeholder.info("Waiting for camera...")
    
    with col2:
        st.subheader("Dashboard")
        status_text_placeholder = st.empty()
        brightness_value_placeholder = st.empty()
        gauge_placeholder = st.empty()
        graph_placeholder = st.empty()

    while st.session_state.run:
        brightness = 0
        frame_display = None
        
        if demo_mode:
            # Simulate brightness
            import random
            brightness = random.randint(0, 255)
            # Create a solid color image based on brightness
            frame_display = np.full((480, 640, 3), brightness, dtype=np.uint8)
            time.sleep(0.5) # Slow down demo
        else:
            # cap is already initialized check validity
            if cap is None or not cap.isOpened():
                st.error("Camera disconnected / not found")
                st.session_state.run = False
                break

            ret, frame = cap.read()
            if not ret:
                st.error(f"Failed to read from webcam {camera_index}. Try a different index.")
                time.sleep(2)
                st.session_state.run = False
                break
            
            brightness = calculate_brightness(frame)
            # Convert BGR to RGB for Streamlit
            frame_display = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Determine status
        status, color = get_brightness_status(brightness, low_threshold, high_threshold)
        
        # Update History
        st.session_state.history.append(brightness)
        if len(st.session_state.history) > 100:
            st.session_state.history.pop(0)
            
        if frame_display is not None:
             image_placeholder.image(frame_display, channels="RGB", use_column_width=True)

        # Display Status
        status_text_placeholder.markdown(f"<h3 style='text-align: center; color: {color};'>{status}</h3>", unsafe_allow_html=True)
        brightness_value_placeholder.markdown(f"<h1 style='text-align: center;'>{int(brightness)}</h1>", unsafe_allow_html=True)
        
        # Display Gauge (Progress Bar)
        gauge_placeholder.progress(min(int(brightness), 255) / 255.0)

        # Display Graph
        chart_data = pd.DataFrame(st.session_state.history, columns=['Brightness'])
        graph_placeholder.line_chart(chart_data, height=150)
        
        if not demo_mode:
            time.sleep(0.05) # Limit loop rate

    if cap:
        cap.release()


    else:
        st.info("Click 'Start/Stop Webcam' in the sidebar to begin.")
        st.write("Current Session State:", st.session_state)

if __name__ == "__main__":
    main()
