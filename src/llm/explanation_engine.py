import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

def generate_explanation(prompt: str) -> str:
    try:
        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload, timeout=120)

        if response.status_code != 200:
            return "LLM error: Unable to generate explanation."

        return response.json().get("response", "").strip()

    except Exception as e:
        return f"LLM exception: {str(e)}"