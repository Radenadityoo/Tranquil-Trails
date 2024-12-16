import streamlit as st

def show_results():
    st.markdown("<h2 style='color: #333333;'>Hasil Penyakit Tanaman Anda!</h2>", unsafe_allow_html=True)
    
    if "analysis_result" in st.session_state:
        st.markdown(f"<p style='color: #333333;'>{st.session_state.analysis_result}</p>", unsafe_allow_html=True)
    else:
        st.info("No analysis results yet. Please upload an image in the Upload tab first.")

