import streamlit as st

def show_register():
    st.markdown("<h2 style='color: #333333;'>Daftar</h2>", unsafe_allow_html=True)
    
    name = st.text_input("Nama", key="register_name")
    email = st.text_input("Email", key="register_email")
    password = st.text_input("Kata Sandi", type="password", key="register_password")
    
    if st.button("Daftar", use_container_width=True, key="register_button"):
        # Add your registration logic here
        st.success("Pendaftaran berhasil! Silakan masuk.")

    st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <p style='color: #333333;'>Sudah punya akun?</p>
    </div>
    """, unsafe_allow_html=True)

