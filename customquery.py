import streamlit as st
import pandas as pd
from ai import ask_ai


# ---------------- AI DATA QUERY FUNCTION ----------------
def query_chatgpt(question, context):
    system_prompt = """
You are the world's best teacher and statistical data analyst.
You perform accurate calculations internally.
Return only the final clear answer.
Do NOT show calculation steps.
Be concise and precise.
"""

    user_prompt = f"""
Dataset:
{context}

Question:
{question}
"""

    return ask_ai(system_prompt, user_prompt)


# ---------------- STREAMLIT COMPONENT ----------------
def custom_query():
    st.subheader("Ask Questions About Your Dataset")

    uploaded_file = st.file_uploader("Upload CSV file with student data", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("### Uploaded Data")
        st.dataframe(df)

        question = st.text_area("Ask a question about the dataset:")

        if st.button("Get Answer"):
            if question.strip() == "":
                st.warning("Please enter a question.")
            else:
                context = df.to_string(index=False)

                with st.spinner("Analyzing data with GPT-5-mini..."):
                    answer = query_chatgpt(question, context)

                st.success(answer)