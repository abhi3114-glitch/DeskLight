# DeskLight 💡

**DeskLight** is an intelligent, privacy-focused ambient light detector that uses your laptop's webcam to help you maintain healthy lighting conditions while working.

It analyzes video frames in real-time to calculate ambient brightness and visualizes the data on a dashboard, warning you if your environment is too dark or too bright.

## ✨ Features

- **Real-time Brightness Detection**: Uses computer vision to calculate ambient light levels instantly.
- **Smart Ergonomic Thresholds**: 
    - 🔴 **Too Dark**: Warns you to turn on a light.
    - 🟢 **Ideal**: Confirms optimal lighting.
    - 🟠 **Too Bright**: Suggests reducing glare.
- **Privacy First**: Frames are processed in memory and **never saved** to disk.
- **Light History Graph**: Tracks lighting consistency over your session.
- **Camera Selection**: Support for multiple cameras (internal/external) with a simple selector.
- **Demo Mode**: Simulate various lighting conditions without accessing the camera.

## 🛠️ Tech Stack

- **Python 3.11**
- **Streamlit** (Frontend Dashboard)
- **OpenCV** (Image Processing)
- **Pandas & Altair** (Data Visualization)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhi3114-glitch/DeskLight.git
   cd DeskLight
   ```

2. **Create a virtual environment** (Recommended):
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Mac/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the application using Streamlit:

```bash
streamlit run app.py
```

### Controls
- **Camera Index**: If you have multiple cameras, select `0` (default) or `1` from the sidebar.
- **Start/Stop Webcam**: Click to start monitoring.
- **Demo Mode**: Check this box to see how the app works without a camera.
- **Thresholds**: Adjust "Minimum" and "Maximum" sliders to customize sensitivity for your room.

## 🔧 Troubleshooting

- **"Failed to read from webcam"**: 
    - Ensure your camera is not being used by Zoom, Teams, or another app.
    - Try changing the **Camera Index** in the sidebar.
    - Check your OS privacy settings to allow terminal/python access to the camera.
- **App crashes / Blank screen**:
    - This app uses `cv2.CAP_DSHOW` on Windows for better compatibility. If you are on Linux/Mac, you might strictly need the basic `cv2.VideoCapture(0)`.
    - Ensure you are using **Python 3.11** as newer versions (3.13+) might have library conflicts.

## 📄 License

This project is open-source and available under the MIT License.
