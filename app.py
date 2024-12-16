import streamlit as st
from pages import login, register, dashboard, upload, chat, results

# Set page config
st.set_page_config(
    page_title="Tranquil Trails",
    page_icon="🌾",
    layout="wide"
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
    }
    .sidebar .sidebar-content {
        background-color: #76b852;
    }
    .big-font {
        font-size: 24px !important;
    }
    /* Improve text visibility */
    .stTextInput > div > div > input {
        color: #333333 !important;
    }
    .stTextArea > div > div > textarea {
        color: #333333 !important;
    }
    .stSelectbox > div > div > div {
        color: #333333 !important;
    }
    .stButton > button {
        color: #ffffff !important;
        background-color: #5a8f3d !important;
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
    /* Custom styles for the sidebar */
    .sidebar .sidebar-content {
        background-color: #76b852;
    }
    .sidebar .stRadio > div {
        flex-direction: column;
    }
    .sidebar .stRadio label {
        color: white !important;
        background-color: #5a8f3d;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        text-align: center;
        cursor: pointer;
    }
    .sidebar .stRadio label:hover {
        background-color: #4a7f2d;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

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
        # Sidebar menu
        with st.sidebar:
            st.markdown('<h2 style="color: white;">Menu</h2>', unsafe_allow_html=True)
            selected = st.radio(
                "",
                ["Jenis", "Unggah", "Chat AI", "Hasil"],
                index=0,
                key="sidebar_menu"
            )
        
        if selected == "Jenis":
            dashboard.show_dashboard()
        elif selected == "Unggah":
            upload.show_upload()
        elif selected == "Chat AI":
            chat.show_chat()
        elif selected == "Hasil":
            results.show_results()

if __name__ == "__main__":
    main()

