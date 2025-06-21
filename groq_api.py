import os
import requests
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# API anahtarı ve model tanımı
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama3-8b-8192"

# Sabit URL (Groq API için)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def send_message(chat_history):
    if not GROQ_API_KEY:
        return "❌ API anahtarı eksik. .env dosyasını kontrol edin."

    payload = {
        "model": MODEL_NAME,
        "messages": chat_history,
        "temperature": 0.3,
        "max_tokens": 1024
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.HTTPError as e:
        try:
            error_detail = response.json()
            return f"❌ API hatası (HTTP {response.status_code}): {error_detail}"
        except:
            return f"❌ API hatası (HTTP {response.status_code})"
    except Exception as e:
        return f"❌ Genel hata: {e}"
