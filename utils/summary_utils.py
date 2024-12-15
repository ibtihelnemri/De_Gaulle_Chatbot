from utils.prompts import SUMMARY_PROMPT

def generate_summary(client, french_text, model="gpt-4", temperature=0.5, max_tokens=300):
    """
    Generates an English summary of French text using OpenAI's API.
    """
    try:
        response = client.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": SUMMARY_PROMPT},
                {"role": "user", "content": f"Summarize this French text in English:\n{french_text}"}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating summary: {str(e)}"
