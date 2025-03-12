import streamlit as st
import pandas as pd
import random

# Carregar o dataset
df = pd.read_csv("dataset.csv")

def obter_resposta(pergunta):
    for i, row in df.iterrows():
        if row["pergunta"].lower() in pergunta.lower():
            return row["resposta"]
    return "Não encontrei uma solução para esse problema. Tenta reformular a pergunta."

# Interface no Streamlit
st.title("💬 Chatbot de Suporte Técnico")
st.write("Escreve um problema e eu tentarei ajudar!")

pergunta = st.text_input("Qual é o teu problema?")

if pergunta:
    resposta = obter_resposta(pergunta)
    st.write("🔧 Solução:", resposta)
