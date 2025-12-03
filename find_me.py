import sys
import os
import cv2
from deepface import DeepFace
from scipy.spatial.distance import cosine
import time

# --- FAST & ACCURATE SETTINGS ---
MODEL_NAME = "ArcFace"           # Best for Accuracy
DETECTOR_BACKEND = "yolov8n"     # 'n' = Nano (Fastest). Requires ultralytics installed.
DISTANCE_METRIC = "cosine"
DEFAULT_TOLERANCE = 0.50 

def find_person_in_photos(selfie_path, db_folder, tolerance=DEFAULT_TOLERANCE, min_face_size=20):
    if not os.path.isfile(selfie_path):
        print(f"[x] Selfie not found: {selfie_path}")
        return

    if not os.path.isdir(db_folder):
        print(f"[x] Database folder not found: {db_folder}")
        return

    print(f"[*] Selfie: {selfie_path}")
    print(f"[*] Folder: {db_folder}")
    print(f"[*] Settings: {MODEL_NAME} | {DETECTOR_BACKEND} | Min Size: {min_face_size}px")
    print("-" * 40)

    # 1. Get Embedding for Selfie
    print("[*] Encoding selfie...")
    try:
        selfie_embeddings = DeepFace.represent(
            img_path=selfie_path,
            model_name=MODEL_NAME,
            detector_backend=DETECTOR_BACKEND,
            enforce_detection=True
        )
        selfie_vec = selfie_embeddings[0]["embedding"]
        print("[+] Selfie encoded successfully.")
    except Exception as e:
        print(f"[!] Error processing selfie: {e}")
        return

    # 2. Search in Database
    image_files = [f for f in os.listdir(db_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"[*] Found {len(image_files)} images. Scanning...")
    
    matches = []
    start_time = time.time()

    for img_file in image_files:
        img_path = os.path.join(db_folder, img_file)
        
        try:
            # OPTIMIZATION: represent() returns embeddings AND facial area in one step.
            # This is much faster than extracting faces first.
            face_objs = DeepFace.represent(
                img_path=img_path,
                model_name=MODEL_NAME,
                detector_backend=DETECTOR_BACKEND,
                enforce_detection=False
            )

            for face_obj in face_objs:
                # Check Size Filter
                area = face_obj['facial_area']
                w = area['w']
                h = area['h']

                if w < min_face_size or h < min_face_size:
                    continue # Skip small faces

                # Calculate Distance
                target_vec = face_obj["embedding"]
                distance = cosine(selfie_vec, target_vec)

                if distance <= tolerance:
                    print(f" ✅ MATCH: {img_file} (Dist: {distance:.3f} | Size: {w}x{h})")
                    matches.append(img_file)
                    break # Stop checking this image if match found

        except Exception:
            continue

    end_time = time.time()
    print("\n================ RESULT ================")
    print(f"Scanned {len(image_files)} images in {end_time - start_time:.2f} seconds.")
    if matches:
        print(f"Found {len(matches)} matching images:")
        for m in matches:
            print(f" - {m}")
    else:
        print("No matches found.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python find_me.py <selfie_path> <images_folder>")
        sys.exit(1)
    
    # You can pass tolerance and size as args if needed, defaulting here for simplicity
    find_person_in_photos(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()