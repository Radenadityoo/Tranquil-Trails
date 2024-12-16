import streamlit as st
from PIL import Image
import torch
import io
import os
from ultralytics import YOLO

def load_model(model_path):
    return YOLO(model_path)

def predict(model, image):
    results = model(image)
    return results

def show_upload():
    st.markdown("<h2 style='color: #333333;'>Unggah atau ambil gambar untuk mendeteksi penyakit tanaman</h2>", unsafe_allow_html=True)

    # Get the selected plant type from session state
    selected_plant = st.session_state.get('selected_plant', 'paddy')

    # Load the appropriate model based on the selected plant
    model_paths = {
        'paddy': "best1.pt",
        'chili': "best2.pt",
        'onion': "best3.pt"
    }
    model_path = model_paths.get(selected_plant, "best1.pt")
    model = load_model(model_path)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    camera_input = st.camera_input("Take a picture")

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button("Analyze", key="analyze_upload_button"):
            results = predict(model, image)
            display_results(image, results)

    elif camera_input is not None:
        image = Image.open(camera_input).convert('RGB')
        st.image(image, caption='Captured Image', use_column_width=True)
        if st.button("Analyze", key="analyze_camera_button"):
            results = predict(model, image)
            display_results(image, results)

def display_results(image, results):
    # Display the annotated image
    annotated_image = results[0].plot()
    st.image(annotated_image, caption='Analysis Result', use_column_width=True)

    # Display text results
    st.markdown("<h3 style='color: #333333;'>Detected Issues:</h3>", unsafe_allow_html=True)
    for r in results:
        for c in r.boxes.cls:
            label = r.names[int(c)]
            confidence = r.boxes.conf[0]
            st.markdown(f"<p style='color: #333333;'>• {label} (Confidence: {confidence:.2f})</p>", unsafe_allow_html=True)

    # Store results in session state for the results page
    st.session_state.analysis_result = results
    st.success("Analysis complete! Check the Results tab for more details.")

