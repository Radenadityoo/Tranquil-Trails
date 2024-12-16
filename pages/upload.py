import streamlit as st
from PIL import Image
import io
import os

try:
    import torch
    from ultralytics import YOLO
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False

def load_model(model_path):
    if TORCH_AVAILABLE:
        return YOLO(model_path)
    else:
        st.error("PyTorch dan YOLO tidak tersedia. Tidak dapat memuat model.")
        return None

def predict(model, image):
    if TORCH_AVAILABLE and model is not None:
        results = model(image)
        return results
    else:
        st.error("PyTorch dan YOLO tidak tersedia. Tidak dapat melakukan prediksi.")
        return None

def show_upload():
    st.markdown("<h2 style='color: #333333;'>Unggah atau ambil gambar untuk mendeteksi penyakit tanaman</h2>", unsafe_allow_html=True)

    if not TORCH_AVAILABLE:
        st.warning("PyTorch dan YOLO tidak tersedia. Beberapa fitur mungkin terbatas.")

    # Get the selected plant type from session state
    selected_plant = st.session_state.get('selected_plant', 'paddy')

    # Load the appropriate model based on the selected plant
    model_paths = {
        'paddy': "best1.pt",
        'chili': "best2.pt",
        'onion': "best3.pt"
    }
    model_path = model_paths.get(selected_plant, "best1.pt")
    model = load_model(model_path) if TORCH_AVAILABLE else None

    uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])
    camera_input = st.camera_input("Ambil gambar")

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Gambar yang Diunggah', use_container_width=True)
        if st.button("Analisis", key="analyze_upload_button"):
            if TORCH_AVAILABLE:
                results = predict(model, image)
                display_results(image, results)
            else:
                st.error("Tidak dapat menganalisis. PyTorch dan YOLO tidak tersedia.")

    elif camera_input is not None:
        image = Image.open(camera_input).convert('RGB')
        st.image(image, caption='Gambar yang Diambil', use_container_width=True)
        if st.button("Analisis", key="analyze_camera_button"):
            if TORCH_AVAILABLE:
                results = predict(model, image)
                display_results(image, results)
            else:
                st.error("Tidak dapat menganalisis. PyTorch dan YOLO tidak tersedia.")

def display_results(image, results):
    if results is not None:
        # Display the annotated image
        annotated_image = results[0].plot()
        
        # Store results and analyzed image in session state
        st.session_state.analysis_result = results
        st.session_state.analyzed_image = annotated_image
        
        st.success("Analisis selesai! Periksa tab Hasil untuk detail lebih lanjut.")
        
        # Automatically switch to results page after analysis
        st.session_state.current_page = 'results'
        st.rerun()
    else:
        st.error("Tidak ada hasil yang tersedia. Analisis tidak dapat dilakukan.")

