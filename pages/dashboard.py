import streamlit as st

def show_dashboard():
    st.markdown("<h2 style='color: #333333;'>Pilih Jenis Tanaman</h2>", unsafe_allow_html=True)
    
    # Create buttons for each plant type
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🌾 Paddy", use_container_width=True, key="paddy_button"):
            st.session_state.selected_plant = "paddy"
        if st.button("🌶️ Chili", use_container_width=True, key="chili_button"):
            st.session_state.selected_plant = "chili"
        if st.button("🌽 Corn", use_container_width=True, key="corn_button"):
            st.session_state.selected_plant = "corn"
            
    with col2:
        if st.button("🧄 Garlic", use_container_width=True, key="garlic_button"):
            st.session_state.selected_plant = "garlic"
        if st.button("🧅 Onion", use_container_width=True, key="onion_button"):
            st.session_state.selected_plant = "onion"

