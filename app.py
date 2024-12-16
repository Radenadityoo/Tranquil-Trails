import streamlit as st
import streamlit_option_menu as som
from PIL import Image
import io
import os
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
        background-color: #76b852 !important;
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
        background-color: #76b852 !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
    }
    .stButton > button:hover {
        background-color: #5a8f3d !important;
        border: none !important;
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
    /* Hide default Streamlit sidebar */
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        display: none;
    }

    /* Improve input field styling */
    .stTextInput input, .stTextArea textarea {
        background-color: white !important;
        color: #333333 !important;
        border: 1px solid #76b852 !important;
    }

    /* Custom sidebar styling */
    .sidebar .sidebar-content {
        background-color: #76b852 !important;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: transparent;
        padding: 0 1rem;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 4px 4px 0px 0px;
        color: white !important;
        border: none !important;
        padding: 0 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: white !important;
        color: #76b852 !important;
    }

    /* Remove any margin/padding from tab panels */
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 1rem;
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
            selected = som.option_menu(
                "Menu",
                ["Jenis", "Unggah", "Chat AI", "Hasil"],
                icons=['plant', 'upload', 'chat-dots', 'clipboard-data'],
                menu_icon="list",
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#76b852"},
                    "icon": {"color": "white", "font-size": "25px"}, 
                    "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin":"0px"},
                    "nav-link-selected": {"background-color": "#5a8f3d"},
                }
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

