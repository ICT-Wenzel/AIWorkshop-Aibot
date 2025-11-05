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

        data = response.json()

        # Robust: Prüfen ob es ein Array oder Dict ist
        if isinstance(data, list) and len(data) > 0:
            bot_reply = str(data[0].get("output", "Keine Antwort erhalten."))
        elif isinstance(data, dict):
            bot_reply = str(data.get("output", "Keine Antwort erhalten."))
        else:
            bot_reply = "Keine Antwort erhalten."

        # Nur Text ausgeben
        st.text(bot_reply)

    except requests.exceptions.RequestException as e:
        st.error(f"Fehler beim Aufruf des Webhooks: {e}")
