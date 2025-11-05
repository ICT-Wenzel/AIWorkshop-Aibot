import streamlit as st
import requests

st.title("AI Chatbot via n8n Webhook")

user_input = st.text_input("Schreib etwas:")

webhook_url = st.secrets["webhook_url"]

if user_input:
    payload = {"message": user_input}

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Fehler falls Status != 200

        data = response.json()  # JSON-Antwort parsen

        # Da n8n ein Array zurückgibt, holen wir das erste Element und dann das "output"-Feld
        bot_reply = data[0].get("output", "Keine Antwort erhalten.") if isinstance(data, list) else "Keine Antwort erhalten."
        st.write(bot_reply)

    except requests.exceptions.RequestException as e:
        st.error(f"Fehler beim Aufruf des Webhooks: {e}")
