import streamlit as st
import pandas as pd

# Carregar o dataset
df = pd.read_csv("dataset.csv", encoding="utf-8")

# Função para obter resposta baseada em palavras-chave
def obter_resposta(pergunta):
    pergunta = pergunta.lower()
    for i, row in df.iterrows():
        if any(palavra in pergunta for palavra in row["pergunta"].lower().split()):
            return row["resposta"]
    return "Não encontrei uma solução para esse problema. Tente reformular a pergunta ou adicionar mais detalhes."

# Função para adicionar nova pergunta e resposta ao dataset (temporário)
def adicionar_pergunta_resposta(nova_pergunta, nova_resposta):
    global df
    novo_dado = pd.DataFrame({"pergunta": [nova_pergunta], "resposta": [nova_resposta]})
    df = pd.concat([df, novo_dado], ignore_index=True)
    st.success("Nova pergunta e resposta adicionadas com sucesso! (Essa informação não será salva permanentemente)")

# Interface no Streamlit
st.title("💬 Chatbot de Suporte Técnico")
st.write("Escreva um problema e eu tentarei ajudar!")

# Caixa de texto para inserir o problema
pergunta = st.text_input("Qual é o teu problema?")

# Caixa de texto para adicionar uma nova pergunta e resposta
nova_pergunta = st.text_input("Nova Pergunta")
nova_resposta = st.text_area("Nova Resposta")

if nova_pergunta and nova_resposta:
    adicionar_pergunta_resposta(nova_pergunta, nova_resposta)

if pergunta:
    resposta = obter_resposta(pergunta)
    st.write("🔧 Solução:", resposta)

if pergunta:
    resposta = obter_resposta(pergunta)
    if resposta:
        st.write("🔧 Solução:", resposta)

