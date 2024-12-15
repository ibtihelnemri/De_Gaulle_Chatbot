import openai

def initialize_openai_client(api_key):
    """Initialize OpenAI client."""
    openai.api_key = api_key
    return openai