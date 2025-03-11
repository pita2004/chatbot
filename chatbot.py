import streamlit as st
import requests
from bs4 import BeautifulSoup

def search_solution(query):
    search_url = f"https://www.google.com/search?q={query}+solução"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        snippets = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
        
        results = []
        for snippet in snippets[:3]:  # Pegar os 3 primeiros resultados
            text = snippet.get_text()
            if len(text) > 50:
                results.append(text)
        
        if results:
            return "\n\n".join(results)
    
    return "Não consegui encontrar uma solução exata. Tente acessar este link: " + search_url

st.title("💻 Chatbot de Suporte Técnico")
user_input = st.text_input("Descreva seu problema técnico:")

if st.button("Buscar Solução"):
    if user_input:
        response = search_solution(user_input)
        st.write("### Soluções encontradas:")
        st.write(response)
    else:
        st.warning("Por favor, insira um problema para buscar uma solução.")

