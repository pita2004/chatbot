import openai
import streamlit as st

# Defina sua chave da API OpenAI
openai.api_key = 'sua-chave-api'

def responder_pergunta(pergunta):
    response = openai.Completion.create(
        model="text-davinci-003",  # Ou outro modelo, como GPT-4
        prompt=pergunta,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Configuração do Streamlit
st.title("Assistente de IA")
st.write("Faça suas perguntas e receba respostas geradas pela IA.")

# Caixa de entrada para a pergunta
pergunta = st.text_input("Qual é a sua pergunta?", "")

# Botão para enviar a pergunta
if st.button("Enviar"):
    if pergunta:
        resposta = responder_pergunta(pergunta)
        st.write(f"Resposta: {resposta}")
    else:
        st.write("Por favor, digite uma pergunta.")
