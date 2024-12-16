import streamlit as st

def show_chat():
    st.markdown("<h2 style='color: #333333;'>Chat dengan AI Assistant</h2>", unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Halo! Saya siap membantu anda dengan masalah tanaman. Apa yang ingin anda tanyakan?"}
        ]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f"<p style='color: #333333;'>{message['content']}</p>", unsafe_allow_html=True)

    # Chat input
    if prompt := st.chat_input("Ketik pesan anda"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(f"<p style='color: #333333;'>{prompt}</p>", unsafe_allow_html=True)
            
        # Add your chatbot logic here
        response = "This is a sample response. Replace with your actual chatbot implementation."
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(f"<p style='color: #333333;'>{response}</p>", unsafe_allow_html=True)

