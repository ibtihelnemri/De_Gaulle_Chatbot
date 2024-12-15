import time
import streamlit as st

def simulate_typing(response, typing_speed=0.05):
    """Simulates typing effect for assistant responses."""
    with st.chat_message("assistant"):
        placeholder = st.empty()
        typing_text = ""

        # Simulate progressive typing effect
        for word in response.split():
            typing_text += word + " "
            placeholder.markdown(f"**Général de Gaulle:** {typing_text}")
            time.sleep(typing_speed)
        placeholder.markdown(f"**Général de Gaulle:** {response}")
    