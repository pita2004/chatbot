import streamlit as st
import requests
from bs4 import BeautifulSoup

# Função para buscar soluções na web (usando scraping simples)
def buscar_solucao(query):
    # URL de pesquisa do Google (ou outra página pública)
    search_url = f"https://www.google.com/search?q={query}+solução+problema+site:stackoverflow.com"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)

    # Se a resposta for bem-sucedida, fazer o parsing do HTML
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontrar os snippets da resposta no Google (parte do HTML da página de resultados)
        snippets = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")
        
        results = []
        for snippet in snippets[:3]:  # Pega os 3 primeiros resultados
            text = snippet.get_text()
            if len(text) > 50:
                results.append(text)
        
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
