import streamlit as st
from PIL import Image
import io

def show_upload():
    st.markdown("<h2 style='color: #333333;'>Unggah atau ambil gambar untuk mendeteksi penyakit tanaman</h2>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    camera_input = st.camera_input("Take a picture")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button("Analyze", key="analyze_upload_button"):
            # Add your computer vision model prediction here
            st.session_state.analysis_result = "Sample analysis result"
            st.success("Analysis complete! Check the Results tab.")
            
    elif camera_input is not None:
        image = Image.open(camera_input)
        st.image(image, caption='Captured Image', use_column_width=True)
        if st.button("Analyze", key="analyze_camera_button"):
            # Add your computer vision model prediction here
            st.session_state.analysis_result = "Sample analysis result"
            st.success("Analysis complete! Check the Results tab.")

