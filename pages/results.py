import streamlit as st

def show_results():
    st.markdown("<h2 style='color: #333333;'>Hasil Penyakit Tanaman Anda!</h2>", unsafe_allow_html=True)
    
    if "analyzed_image" in st.session_state:
        st.image(st.session_state.analyzed_image, caption='Hasil Analisis', use_container_width=True)
    
    if "analysis_result" in st.session_state and st.session_state.analysis_result:
        results = st.session_state.analysis_result
        st.markdown("<h3 style='color: #333333;'>Masalah yang Terdeteksi:</h3>", unsafe_allow_html=True)
        for r in results:
            for c in r.boxes.cls:
                label = r.names[int(c)]
                confidence = r.boxes.conf[0]
                st.markdown(f"<p style='color: #333333;'>• {label} (Kepercayaan: {confidence:.2f})</p>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #333333;'>Rekomendasi:</h3>", unsafe_allow_html=True)
        st.markdown("""
        <p style='color: #333333;'>Berdasarkan masalah yang terdeteksi, pertimbangkan tindakan berikut:</p>
        <ul style='color: #333333;'>
            <li>Konsultasikan dengan ahli pertanian setempat untuk saran yang lebih personal.</li>
            <li>Tinjau kembali praktik perawatan tanaman Anda saat ini dan lakukan penyesuaian yang diperlukan.</li>
            <li>Pertimbangkan perawatan atau intervensi yang sesuai berdasarkan masalah spesifik yang terdeteksi.</li>
        </ul>
        """, unsafe_allow_html=True)
    else:
        st.info("Belum ada hasil analisis. Silakan unggah gambar di tab Unggah terlebih dahulu.")

