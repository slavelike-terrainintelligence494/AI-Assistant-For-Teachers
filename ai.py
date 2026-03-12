from openai import OpenAI
import os
import streamlit as st


# ---------------- INITIALIZE CLIENT ----------------
@st.cache_resource
def get_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    return OpenAI(api_key=api_key)


client = get_client()


# ---------------- CENTRAL AI FUNCTION ----------------
def ask_ai(system_prompt: str, user_prompt: str) -> str:
    """
    Central AI handler for entire application.
    GPT-5-mini compatible version.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
            # ✅ IMPORTANT: NO temperature parameter
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"