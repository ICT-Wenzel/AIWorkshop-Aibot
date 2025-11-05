import streamlit as st
import requests
import os

st.title("AI Chatbot via n8n Webhook")

# Benutzerinput
user_input = st.text_input("Schreib etwas:")

# Webhook URL aus den Streamlit Secrets holen
# In Streamlit Cloud: Secrets > "webhook_url"
webhook_url = st.secrets["webhook_url"]

if user_input:
    payload = {"message": user_input}

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Fehler falls Status != 200

        bot_reply = response.json().get("reply", "Keine Antwort erhalten.")
        st.write(bot_reply)

    except requests.exceptions.RequestException as e:
        st.error(f"Fehler beim Aufruf des Webhooks: {e}")
