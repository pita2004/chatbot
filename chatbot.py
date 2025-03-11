import openai
import streamlit as st

# Defina sua chave da API OpenAI
openai.api_key = 'sua-chave-api'

def responder_pergunta(pergunta):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ou o modelo GPT-4 se você tiver acesso
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": pergunta}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()

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

