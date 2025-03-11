import streamlit as st
import requests
from bs4 import BeautifulSoup

def search_solution(query):
    # Fazer uma pesquisa no Google
    search_url = f"https://www.google.com/search?q={query}+solução"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        # Realizar a requisição para o Google
        response = requests.get(search_url, headers=headers, timeout=5)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Procurar por snippets (resultados relevantes)
            snippets = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
            
            results = []
            for snippet in snippets[:3]:  # Mostrar os 3 primeiros resultados
                text = snippet.get_text()
                if len(text) > 50:  # Garantir que o texto tenha tamanho suficiente
                    results.append(text)
            
            if results:
                return "\n\n".join(results)
            else:
                return "Não encontrei soluções relevantes nos resultados de pesquisa."
        else:
            return f"Erro ao acessar o Google. Status code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Ocorreu um erro: {e}"

# Configuração do Streamlit
st.title("💻 Chatbot de Suporte Técnico")
user_input = st.text_input("Descreva seu problema técnico:")

if st.button("Buscar Solução"):
    if user_input:
        # Buscar solução no Google
        response = search_solution(user_input)
        st.write("### Soluções encontradas:")
        st.write(response)
    else:
        st.warning("Por favor, insira um problema para buscar uma solução.")

