from deep_translator import GoogleTranslator

def translate_text(text, target_lang="fr"):
    """Translates text into the target language."""
    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception as e:
        return f"Error during translation: {e}"

