import streamlit as st
import requests

st.title("Saneamento Analytics")

uploaded_file = st.file_uploader("Envie um arquivo CSV ou Excel", type=["csv", "xlsx"])
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(
        "https://saneamento-backend.onrender.com/analyze",
        files={"file": uploaded_file},
        timeout=60
    )
    if response.status_code == 200:
        result = response.json()
        st.write("Resultado da Análise:", result)
    else:
        st.error("Erro na análise. Verifique o arquivo ou tente novamente.")
