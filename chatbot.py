import streamlit as st
import requests

# Defina sua chave de API e endpoint do Bing Search
API_KEY = "SUA_CHAVE_DE_API_AQUI"
ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"

# Função para fazer a busca com Bing Search API
def buscar_solucao(query):
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY
    }
    
    params = {
        "q": query,
        "textDecorations": True,
        "textFormat": "HTML"
    }
    
    # Fazendo a solicitação de pesquisa
    response = requests.get(ENDPOINT, headers=headers, params=params)
    
    if response.status_code == 200:
        search_results = response.json()
        
        # Filtra os resultados principais e extrai informações
        results = []
        for web_page in search_results.get("webPages", {}).get("value", [])[:3]:  # Pega os 3 primeiros resultados
            results.append(f"**Título**: {web_page['name']}\n**Descrição**: {web_page['snippet']}\n**Link**: {web_page['url']}")
        
        return "\n\n".join(results) if results else "Não encontrei soluções relevantes."
    
    return "Erro na busca, por favor, tente novamente mais tarde."

# Título da aplicação
st.title("💻 Chatbot de Suporte Técnico")

# Caixa de texto para o usuário descrever seu problema
user_input = st.text_input("Descreva seu problema técnico:")

# Quando o botão for clicado, buscar a solução
if st.button("Buscar Solução"):
    if user_input:
        # Chama a função de busca
        resposta = buscar_solucao(user_input)
        st.write("### Soluções encontradas:")
        st.write(resposta)
    else:
        st.warning("Por favor, insira um problema para buscar uma solução.")



