import streamlit as st
import numpy as np
from PIL import Image
from deepface import DeepFace
from scipy.spatial.distance import cosine

# --- PAGE CONFIG ---
st.set_page_config(page_title="DeepFace Fast Finder", page_icon="🚀", layout="wide")

# --- FAST SETTINGS ---
MODEL_NAME = "ArcFace"           
DETECTOR_BACKEND = "yolov8n"     # FIXED: Added 'n' for Nano model
DISTANCE_METRIC = "cosine"

# --- SIDEBAR ---
st.sidebar.title("⚙️ Settings")

tolerance = st.sidebar.slider(
    "Match tolerance (Lower = Stricter)", 
    0.0, 1.0, 0.50, 0.01,
    help="0.40 is strict, 0.60 is loose."
)
st.sidebar.caption(f"Current Limit: **{tolerance:.2f}**")

st.sidebar.markdown("---")

min_face_size = st.sidebar.slider(
    "Minimum face size (px)", 
    10, 200, 20, 5,
    help="Filters out tiny faces in background."
)
st.sidebar.caption(f"Ignoring faces smaller than: **{min_face_size}px**")

# --- MAIN UI ---
st.title("🚀 Find My Face (Fast & Accurate)")
st.markdown(f"""
Upload your **Selfie** and **Group Photos**. 
Engine: `{MODEL_NAME}` | Detector: `{DETECTOR_BACKEND}`
""")

# --- FUNCTIONS ---
def load_image_as_array(uploaded_file):
    return np.array(Image.open(uploaded_file))

def get_embedding(img_array):
    results = DeepFace.represent(
        img_path=img_array,
        model_name=MODEL_NAME,
        detector_backend=DETECTOR_BACKEND,
        enforce_detection=True
    )
    return results[0]["embedding"]

# --- LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    st.info("Step 1: Upload Selfie 👤")
    selfie_file = st.file_uploader("", type=["jpg", "jpeg", "png"], key="selfie")
    if selfie_file:
        st.image(selfie_file, width=150)

with col2:
    st.info("Step 2: Upload Photos to Search 📂")
    photos_files = st.file_uploader("", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="photos")

# --- PROCESS ---
if st.button("🔎 Find me (Fast)", type="primary", use_container_width=True):
    if not selfie_file or not photos_files:
        st.error("Please upload both selfie and photos.")
    else:
        # 1. Selfie
        with st.status("Processing Selfie...", expanded=True) as status:
            try:
                selfie_arr = load_image_as_array(selfie_file)
                selfie_vec = get_embedding(selfie_arr)
                status.update(label="Selfie Encoded! ✅", state="complete", expanded=False)
            except Exception as e:
                status.update(label="Error ❌", state="error")
                st.error(f"Error with selfie: {e}")
                st.stop()

        # 2. Group Photos
        st.divider()
        st.subheader("Results")
        
        found_count = 0
        progress_bar = st.progress(0)
        
        # Grid for results
        cols = st.columns(3)
        col_idx = 0

        for i, photo_file in enumerate(photos_files):
            try:
                target_arr = load_image_as_array(photo_file)
                
                # Optimized: Get embeddings and areas in ONE step
                face_objs = DeepFace.represent(
                    img_path=target_arr,
                    model_name=MODEL_NAME,
                    detector_backend=DETECTOR_BACKEND,
                    enforce_detection=False
                )
                
                match_found = False
                best_dist = 100
                
                for face in face_objs:
                    # Size Filter
                    area = face['facial_area']
                    if area['w'] < min_face_size or area['h'] < min_face_size:
                        continue

                    # Compare
                    dist = cosine(selfie_vec, face["embedding"])
                    
                    if dist < best_dist: best_dist = dist
                    
                    if dist <= tolerance:
                        match_found = True
                        break # Found!

                if match_found:
                    found_count += 1
                    with cols[col_idx % 3]:
                        st.success(f"Match! (Dist: {best_dist:.2f})")
                        st.image(photo_file, caption=photo_file.name, use_container_width=True)
                    col_idx += 1
                    
            except:
                pass # No face found in this image
            
            progress_bar.progress((i + 1) / len(photos_files))

        if found_count == 0:
            st.warning("No matches found.")
        else:
            st.success(f"🎉 Found {found_count} matches!")