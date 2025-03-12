import streamlit as st
import pandas as pd
import os

# Nome do arquivo CSV
DATASET_PATH = "dataset.csv"

# Verifica se o arquivo existe, se não, cria um novo com colunas vazias
if not os.path.exists(DATASET_PATH):
    df = pd.DataFrame(columns=["pergunta", "resposta"])
    df.to_csv(DATASET_PATH, index=False, encoding="utf-8")
else:
    df = pd.read_csv(DATASET_PATH, encoding="utf-8")

# Função para obter resposta baseada em palavras-chave
def obter_resposta(pergunta):
    for i, row in df.iterrows():
        if any(palavra.lower() in pergunta.lower() for palavra in row["pergunta"].split()):
            return row["resposta"]
    return "Não encontrei uma solução para esse problema. Tente reformular a pergunta."

# Função para adicionar nova pergunta e resposta ao dataset e salvar no CSV
def adicionar_pergunta_resposta(nova_pergunta, nova_resposta):
    global df
    novo_dado = pd.DataFrame({"pergunta": [nova_pergunta], "resposta": [nova_resposta]})
    df = pd.concat([df, novo_dado], ignore_index=True)
    df.to_csv(DATASET_PATH, index=False, encoding="utf-8")  # Salvar mudanças no arquivo CSV
    st.success("Nova pergunta e resposta adicionadas com sucesso e salvas no dataset!")

# Interface no Streamlit
st.title("💬 Chatbot de Suporte Técnico")
st.write("Escreve um problema e eu tentarei ajudar!")

# Caixa de texto para inserir o problema
pergunta = st.text_input("Qual é o teu problema?")

# Caixa de texto para adicionar uma nova pergunta e resposta
nova_pergunta = st.text_input("Nova Pergunta")
nova_resposta = st.text_area("Nova Resposta")

if nova_pergunta and nova_resposta:
    adicionar_pergunta_resposta(nova_pergunta, nova_resposta)

if pergunta:
    resposta = obter_resposta(pergunta)
    if resposta:
        st.write("🔧 Solução:", resposta)

