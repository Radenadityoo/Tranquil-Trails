import streamlit as st
from pages import login, register, dashboard, upload, chat, results
import time

# Set page config
st.set_page_config(
    page_title="Tranquil Trails",
    page_icon="🌾",
    layout="wide",
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
    }
    .main-header {
        background-color: #76b852;
        padding: 1rem;
        color: white;
        margin: -1rem -1rem 1rem -1rem;
    }
    .big-font {
        font-size: 24px !important;
    }
    /* Improve text visibility */
    .stTextInput > div > div > input {
        color: #333333 !important;
        background-color: #f0f0f0 !important;
    }
    .stTextArea > div > div > textarea {
        color: #333333 !important;
        background-color: #f0f0f0 !important;
    }
    .stSelectbox > div > div > div {
        color: #333333 !important;
    }
    .stButton > button {
        color: #ffffff !important;
        background-color: #5a8f3d !important;
        width: 100%;
    }
    .stTab > button {
        color: #333333 !important;
    }
    .stTab > button[data-baseweb="tab"][aria-selected="true"] {
        color: #5a8f3d !important;
    }
    p, .stMarkdown {
        color: #333333 !important;
    }
    /* Hide default sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    /* Custom navigation */
    .custom-nav {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    .nav-button {
        background-color: #5a8f3d;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
    }
    .nav-button:hover {
        background-color: #4a7f2d;
    }
    /* Transition effect */
    .transition-fade {
        animation: fadeIn 0.5s ease-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'login'

def change_page(page):
    st.session_state.current_page = page
    st.rerun()

def main():
    # Header
    st.markdown('<div class="main-header"><h1>Tranquil Trails</h1></div>', unsafe_allow_html=True)
    
    if not st.session_state.logged_in:
        tab1, tab2 = st.tabs(["Masuk", "Daftar"])
        
        with tab1:
            login.show_login()
        with tab2:
            register.show_register()
    else:
        # Custom navigation using Streamlit buttons
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Jenis Tanaman", key="nav_dashboard", use_container_width=True):
                change_page('dashboard')
        with col2:
            if st.button("Unggah", key="nav_upload", use_container_width=True):
                change_page('upload')
        with col3:
            if st.button("Chat AI", key="nav_chat", use_container_width=True):
                change_page('chat')
        with col4:
            if st.button("Hasil", key="nav_results", use_container_width=True):
                change_page('results')

        # Display current page with transition effect
        with st.container():
            st.markdown('<div class="transition-fade">', unsafe_allow_html=True)
            if st.session_state.current_page == 'dashboard':
                dashboard.show_dashboard()
            elif st.session_state.current_page == 'upload':
                upload.show_upload()
            elif st.session_state.current_page == 'chat':
                chat.show_chat()
            elif st.session_state.current_page == 'results':
                results.show_results()
            st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()

