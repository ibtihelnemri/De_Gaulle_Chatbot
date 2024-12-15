import streamlit as st
from PIL import Image
from utils.openai_client import initialize_openai_client
from utils.prompts import GENERAL_DE_GAULLE_PROMPT
from utils.streamlit_helpers import simulate_typing
from utils.chat_utils import initialize_chat, get_chat_response
from utils.translation_utils import translate_text
from utils.summary_utils import generate_summary


# Initialize OpenAI client
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
client = initialize_openai_client(OPENAI_API_KEY)

# Initialize session state
initialize_chat(GENERAL_DE_GAULLE_PROMPT)

# Layout configuration
st.title("Chatbot Général de Gaulle")

# Add the image
image = Image.open("assets/De_Gaulle.jpg")
resized_image = image.resize((int(image.width * 1.8), int(image.height * 1.5)))  # Scale to 80% of the original size
st.image(resized_image)

st.sidebar.header("Chatbot Settings")

# Sidebar settings
temperature = st.sidebar.slider("Response Creativity (Temperature)", 0.0, 1.0, 0.3, 0.1)
generate_summary_option = st.sidebar.checkbox("Generate English Summary", value=True)

# User input
user_query = st.chat_input("Posez votre question dans n'importe quelle langue :")
if user_query:
    #st.chat_message("user").markdown(user_query)

    # Input question
    st.write(f"The questions is : {user_query}")

    # Translate Query to French
    translated_query = translate_text(user_query, target_lang="fr")
    st.markdown(f"**Translated to French:** {translated_query}")


    # Get assistant response
    assistant_response = get_chat_response(client, translated_query, temperature)
    simulate_typing(assistant_response)

    # Generate English summary if option enabled
    if generate_summary_option:
        with st.chat_message("summary"):
            english_summary = generate_summary(client, assistant_response)
            if "Error" not in english_summary:
                st.markdown(f"**English Summary:**\n{english_summary}")
            else:
                st.error(english_summary)

    
