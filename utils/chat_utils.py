import streamlit as st

def initialize_chat(system_prompt):
    """Initializes the chat session."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [{"role": "system", "content": system_prompt}]


def get_chat_response(client, user_input, temperature):
    """Sends a user message and gets a response from the OpenAI ChatCompletion endpoint."""
    # Add user input to the chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Call OpenAI ChatCompletion API
    response = client.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.chat_history,
        temperature=temperature
    )
    # Extract assistant response
    assistant_response = response['choices'][0]['message']['content']

    # Append assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    return assistant_response

