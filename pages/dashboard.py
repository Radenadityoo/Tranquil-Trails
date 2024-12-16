import streamlit as st

def show_dashboard():
    st.markdown("<h2 style='color: #333333;'>Pilih Jenis Tanaman</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🌾 Padi", use_container_width=True, key="paddy_button"):
            st.session_state.selected_plant = "paddy"
            st.session_state.current_page = 'upload'
            st.rerun()
    with col2:
        if st.button("🌶️ Cabai", use_container_width=True, key="chili_button"):
            st.session_state.selected_plant = "chili"
            st.session_state.current_page = 'upload'
            st.rerun()
    with col3:
        if st.button("🧅 Bawang", use_container_width=True, key="onion_button"):
            st.session_state.selected_plant = "onion"
            st.session_state.current_page = 'upload'
            st.rerun()

