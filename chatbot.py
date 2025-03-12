import streamlit as st
import pandas as pd

# Carregar o dataset
df = pd.read_csv("dataset.csv", encoding="utf-8")

# Função para obter resposta com base em palavras-chave
def obter_resposta(pergunta):
    pergunta = pergunta.lower()
    melhor_resposta = "Não encontrei uma solução para esse problema. Tente reformular a pergunta."
    maior_relevancia = 0
    
    for _, row in df.iterrows():
        palavras_chave = row["pergunta"].lower().split()
        relevancia = sum(1 for palavra in palavras_chave if palavra in pergunta)
        
        if relevancia > maior_relevancia:
            maior_relevancia = relevancia
            melhor_resposta = row["resposta"]
    
    return melhor_resposta

# Função para adicionar nova pergunta e resposta ao dataset (apenas na sessão atual)
def adicionar_pergunta_resposta(nova_pergunta, nova_resposta):
    global df
    novo_dado = pd.DataFrame({"pergunta": [nova_pergunta], "resposta": [nova_resposta]})
    df = pd.concat([df, novo_dado], ignore_index=True)
    st.success("Nova pergunta e resposta adicionadas com sucesso! (Nota: Isso não salva permanentemente no dataset)")

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
    st.write("🔧 Solução:", resposta)


