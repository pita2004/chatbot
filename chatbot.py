import streamlit as st
import requests
from bs4 import BeautifulSoup

# Função para buscar soluções diretamente no Stack Overflow
def buscar_solucao(query):
    # URL de pesquisa no Stack Overflow
    search_url = f"https://stackoverflow.com/search?q={query.replace(' ', '+')}"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)

    # Se a resposta for bem-sucedida, fazer o parsing do HTML
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontrar os snippets das perguntas mais relevantes
        questions = soup.find_all("div", class_="result-link")
        
        results = []
        for question in questions[:3]:  # Pega as 3 primeiras perguntas
            title = question.find("a").get_text(strip=True)
            link = "https://stackoverflow.com" + question.find("a")["href"]
            results.append(f"**Título**: {title}\n**Link**: {link}")
        
        # Exibe as soluções encontradas
        if results:
            return "\n\n".join(results)
    
    return "Não consegui encontrar uma solução exata. Tente reformular o problema."

# Configuração do Streamlit
st.title("💻 Chatbot de Suporte Técnico")

# Caixa de entrada para o problema do usuário
user_input = st.text_input("Descreva seu problema técnico:")

if st.button("Buscar Solução"):
    if user_input:
        # Chama a função para buscar a solução
        resposta = buscar_solucao(user_input)
        st.write("### Soluções encontradas:")
        st.write(resposta)
    else:
        st.warning("Por favor, insira um problema para buscar uma solução.")

