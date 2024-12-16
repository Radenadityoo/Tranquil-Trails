import streamlit as st

def show_results():
    st.markdown("<h2 style='color: #333333;'>Hasil Penyakit Tanaman Anda!</h2>", unsafe_allow_html=True)
    
    if "analysis_result" in st.session_state and st.session_state.analysis_result:
        results = st.session_state.analysis_result
        st.markdown("<h3 style='color: #333333;'>Detected Issues:</h3>", unsafe_allow_html=True)
        for r in results:
            for c in r.boxes.cls:
                label = r.names[int(c)]
                confidence = r.boxes.conf[0]
                st.markdown(f"<p style='color: #333333;'>• {label} (Confidence: {confidence:.2f})</p>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #333333;'>Recommendations:</h3>", unsafe_allow_html=True)
        st.markdown("""
        <p style='color: #333333;'>Based on the detected issues, consider the following actions:</p>
        <ul style='color: #333333;'>
            <li>Consult with a local agricultural expert for personalized advice.</li>
            <li>Review your current plant care practices and make necessary adjustments.</li>
            <li>Consider appropriate treatments or interventions based on the specific issues detected.</li>
        </ul>
        """, unsafe_allow_html=True)
    else:
        st.info("No analysis results yet. Please upload an image in the Upload tab first.")

