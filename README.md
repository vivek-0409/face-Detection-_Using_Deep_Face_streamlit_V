# 🚀 Face Detection & Recognition App (DeepFace + Streamlit)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://face-detection-using-deep-face.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![DeepFace](https://img.shields.io/badge/AI-DeepFace-orange)
![Detector](https://img.shields.io/badge/Detector-YOLOv8n-green)

A high-performance **Face Recognition Web App** built using **DeepFace** and **Streamlit**. This tool allows users to upload a selfie and find that person within a folder or collection of group photos.

It utilizes the **ArcFace** model for state-of-the-art accuracy and **YOLOv8n** for ultra-fast face detection.

## 📸 App Interface
![App Interface](image_a73897.png)
*(The interface allows dragging & dropping photos with real-time parameter tuning)*

---

## ✨ Key Features

* **⚡ Blazing Fast:** Uses the **YOLOv8n (Nano)** backend for extremely fast face detection (much faster than RetinaFace).
* **🎯 High Accuracy:** Uses the **ArcFace** model, widely considered one of the most accurate face recognition models available.
* **🎛️ Customizable Controls:**
    * **Tolerance Slider:** Adjust how strict the matching algorithm is.
    * **Min Face Size:** Filter out tiny background faces or noise (e.g., ignore faces smaller than 30px).
* **🔄 Dual Modes:**
    1.  **Web UI (`app.py`):** Interactive visualization in the browser.
    2.  **CLI Tool (`find_me.py`):** Batch processing for local folders via command line.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/vivek-0409/face-Detection-_Using_Deep_Face_streamlit_V.git](https://github.com/vivek-0409/face-Detection-_Using_Deep_Face_streamlit_V.git)
cd face-Detection-_Using_Deep_Face_streamlit_V




Based on the code and features we implemented (DeepFace, YOLOv8n, ArcFace, Streamlit), here is the complete, professional README.md file for your repository.You can create a file named README.md in your project folder and paste this code directly into it.Markdown# 🚀 Face Detection & Recognition App (DeepFace + Streamlit)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://face-detection-using-deep-face.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![DeepFace](https://img.shields.io/badge/AI-DeepFace-orange)
![Detector](https://img.shields.io/badge/Detector-YOLOv8n-green)

A high-performance **Face Recognition Web App** built using **DeepFace** and **Streamlit**. This tool allows users to upload a selfie and find that person within a folder or collection of group photos.

It utilizes the **ArcFace** model for state-of-the-art accuracy and **YOLOv8n** for ultra-fast face detection.

## 📸 App Interface
![App Interface](image_a73897.png)
*(The interface allows dragging & dropping photos with real-time parameter tuning)*

---

## ✨ Key Features

* **⚡ Blazing Fast:** Uses the **YOLOv8n (Nano)** backend for extremely fast face detection (much faster than RetinaFace).
* **🎯 High Accuracy:** Uses the **ArcFace** model, widely considered one of the most accurate face recognition models available.
* **🎛️ Customizable Controls:**
    * **Tolerance Slider:** Adjust how strict the matching algorithm is.
    * **Min Face Size:** Filter out tiny background faces or noise (e.g., ignore faces smaller than 30px).
* **🔄 Dual Modes:**
    1.  **Web UI (`app.py`):** Interactive visualization in the browser.
    2.  **CLI Tool (`find_me.py`):** Batch processing for local folders via command line.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/vivek-0409/face-Detection-_Using_Deep_Face_streamlit_V.git](https://github.com/vivek-0409/face-Detection-_Using_Deep_Face_streamlit_V.git)
cd face-Detection-_Using_Deep_Face_streamlit_V
2. Create a Virtual Environment (Python 3.10 Recommended)Note: Python 3.10 is required for compatibility with DeepFace dependencies.Windows:PowerShellpy -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
Mac/Linux:Bashpython3.10 -m venv .venv
source .venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
🚀 How to RunOption A: Streamlit Web App (Visual)This launches the web interface in your browser.Bashstreamlit run app.py
Upload your Selfie.Upload Group Photos.Click "Find me (Fast)".Option B: Command Line Tool (Batch)Use this to search through a local folder of images without the browser.Bashpython find_me.py "path/to/selfie.jpg" "path/to/images_folder"
Example:Bashpython find_me.py "Sample selfie" "Image_data"

⚙️ Tech Stack & ConfigurationComponentChoiceReasonFrameworkStreamlitFast, interactive UI creationRecognition ModelArcFaceHigh precision (~99.5% accuracy)Face DetectorYOLOv8n'Nano' model provides real-time detection speedDistance MetricCosineStandard metric for ArcFace embeddingsPython Version3.10Stability for TensorFlow/Keras dependencies📂 Project StructurePlaintext├── .venv/                 # Virtual Environment (not uploaded to git)

├── .venv/                 # Virtual Environment
├── Image_data/            # Folder containing group photos (for CLI test)
├── .python-version        # Deployment config (Forces Python 3.10)
├── app.py                 # Main Streamlit Application
├── find_me.py             # Command Line Script
├── packages.txt           # System dependencies (libgl1)
├── requirements.txt       # Python dependencies
├── Sample selfie
└── README.md              # Project Documentation

☁️ Deployment Notes (Streamlit Cloud)If deploying to Streamlit Community Cloud, ensure the following files are present to avoid build errors:
1. packages.txt: Must contain libgl1 (required for OpenCV on Linux)
2. requirements.txt: Must use opencv-python-headless instead of standard opencv.
3. python-version: Must contain 3.10 to prevent Python 3.13 conflicts.
