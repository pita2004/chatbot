import streamlit as st

# Base interna com perguntas e respostas
respostas = {
    "como corrigir erro de conexão wi-fi": "Para corrigir problemas de conexão Wi-Fi, tente reiniciar o roteador, verificar as configurações de rede e garantir que o driver da sua placa de rede esteja atualizado.",
    "como resolver erro de compilação no python": "Verifique se você instalou as dependências corretamente, se a versão do Python é compatível com o código e se não há erros de sintaxe no código.",
    "como corrigir erro de tela azul no windows": "Tente reiniciar o computador, verifique se há atualizações de drivers e, se o problema persistir, você pode tentar restaurar o sistema para um ponto anterior.",
    "como configurar uma rede vpn": "Para configurar uma VPN, você precisa de um serviço de VPN, configurar as credenciais e usar um software de cliente VPN para se conectar à rede segura.",
    "como melhorar o desempenho do computador": "Você pode melhorar o desempenho do seu computador desinstalando programas desnecessários, limpando arquivos temporários e considerando upgrades de hardware, como mais memória RAM ou um SSD."
}

# Título da aplicação
st.title("💻 Chatbot de Suporte Técnico Simplificado")

# Caixa de texto para o usuário descrever seu problema
user_input = st.text_input("Descreva seu problema técnico:")

# Quando o botão for clicado, busca pela solução na base interna
if st.button("Buscar Solução"):
    if user_input:
        # Converter para minúsculas e procurar uma resposta
        user_input = user_input.lower()
        resposta = respostas.get(user_input, "Desculpe, não encontrei uma solução para o seu problema. Tente novamente com outra descrição.")
        
        # Exibe a resposta
        st.write("### Solução encontrada:")
        st.write(resposta)
    else:
        st.warning("Por favor, insira um problema para buscar uma solução.")


