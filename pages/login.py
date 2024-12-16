import streamlit as st

def show_login():
    st.markdown("<h2 style='color: #333333;'>Masuk</h2>", unsafe_allow_html=True)
    
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Kata sandi", type="password", key="login_password")
    
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Masuk", use_container_width=True, key="login_button"):
            # Add your authentication logic here
            st.session_state.logged_in = True
            st.session_state.current_page = 'dashboard'
            st.rerun()
    
    st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <a href="#" style='color: #5a8f3d;'>Lupa kata sandi?</a>
    </div>
    """, unsafe_allow_html=True)

