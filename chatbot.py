import streamlit as st

def gerar_solucao(query):
    # Aqui você pode usar um modelo de linguagem como GPT ou outras fontes de dados para gerar a solução
    problemas_comuns = {
        "não consigo acessar a internet": "Tente reiniciar o roteador e verificar as conexões de cabo. Caso o problema persista, verifique se o seu provedor está com algum problema técnico.",
        "computador muito lento": "Tente fechar programas desnecessários, limpar o disco e desfragmentar. Caso o problema continue, considere aumentar a memória RAM ou atualizar o sistema operacional.",
        "tela azul no Windows": "A tela azul pode ser causada por problemas de hardware ou software. Tente reiniciar o computador e, se o problema continuar, verifique drivers e faça uma restauração do sistema.",
        "celular não liga": "Verifique se a bateria está carregada. Se o celular não ligar, tente pressionar o botão de liga/desliga por 10 segundos ou faça uma reinicialização forçada.",
    }

    # Verificar se o problema é um dos casos comuns
    for problema, solucao in problemas_comuns.items():
        if problema in query.lower():
            return solucao

    # Caso não seja um problema comum, retornar uma resposta genérica
    return "Não consegui encontrar uma solução exata. Você pode tentar reiniciar o dispositivo ou consultar o manual do usuário."

st.title("💻 Chatbot de Suporte Técnico")
user_input = st.text_input("Descreva seu problema técnico:")

if st.button("Buscar Solução"):
    if user_input:
        resposta = gerar_solucao(user_input)
        st.write("### Solução encontrada:")
        st.write(resposta)
    else:
        st.warning("Por favor, insira um problema para buscar uma solução.")
