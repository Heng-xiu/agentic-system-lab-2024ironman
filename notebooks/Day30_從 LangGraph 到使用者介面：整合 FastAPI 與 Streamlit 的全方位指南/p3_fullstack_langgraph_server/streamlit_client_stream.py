import streamlit as st
import requests
import json

# LangServe FastAPI server URL
API_URL = "http://localhost:8000/api/v1/joke/stream"

st.title("Joke Generator Chat (LangServe Streaming)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What kind of joke would you like?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare the request payload
    payload = {
        "input": {
            "topic": prompt
        }
    }

    # Send request to LangServe FastAPI server
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "text/event-stream"
        }
        
        with requests.post(API_URL, json=payload, headers=headers, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        try:
                            data = json.loads(line[6:])  # Skip 'data: ' prefix
                            chunk = data.get('content', '')
                            if chunk:
                                full_response += chunk
                                message_placeholder.markdown(full_response + "▌")
                        except json.JSONDecodeError:
                            continue
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})