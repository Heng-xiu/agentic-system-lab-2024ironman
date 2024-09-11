import streamlit as st
import requests

# FastAPI server URL
API_URL = "http://localhost:8000/api/v1/joke/invoke"

st.title("Joke Generator Chat")

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

    # Send request to FastAPI server
    req_json = {
        "input": {
            "topic": prompt
        }
    }
    response = requests.post(API_URL, json=req_json)
    
    if response.status_code == 200:
        assistant_response = response.json()["output"]["content"]
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    else:
        st.error(f"Error: Unable to get response from server. Status code: {response.status_code}")