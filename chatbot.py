import streamlit as st

# Dicionário com perguntas e respostas predefinidas
faq = {
    "Como reiniciar o meu computador?": "Para reiniciar o seu computador, pressione o botão de 'Iniciar' e depois clique em 'Reiniciar'.",
    "O meu computador está muito lento, o que fazer?": "Tente fechar programas que estão a consumir muitos recursos ou reiniciar o computador.",
    "Como configurar uma impressora?": "Para configurar uma impressora, ligue-a ao computador, instale os drivers e defina-a como impressora padrão nas configurações de impressora.",
    "Como resolver erro de impressão?": "Verifique se a impressora está ligada, se há papel e tinta/toner suficientes, e se a impressora está corretamente ligada ao computador.",
    "Como fazer a formatação do meu computador?": "Para formatar o seu computador, faça backup dos seus ficheiros e, em seguida, inicie o sistema a partir de uma unidade de instalação (USB/DVD) e siga as instruções.",
    "A minha impressora não está a imprimir, o que faço?": "Verifique a ligação da impressora, se está ligada e se o estado de impressão está correto. Além disso, veja se não há erros na fila de impressão.",
    "O que é a tela azul e como corrigir?": "A tela azul pode ocorrer devido a erros graves no sistema. Aqui estão três soluções possíveis:\n\n1. **Reinicie o computador em modo de segurança:** Reinicie o computador e pressione F8 antes do carregamento do sistema. Selecione 'Modo de segurança' e veja se o sistema arranca corretamente.\n\n2. **Verifique se há atualizações de drivers:** Drivers desatualizados ou corrompidos podem causar falhas. Vá até o 'Gestor de Dispositivos', clique com o botão direito em cada dispositivo e selecione 'Atualizar driver'.\n\n3. **Verifique o hardware:** A tela azul também pode ser causada por falhas de hardware, como a memória RAM com defeito. Pode realizar um diagnóstico de hardware ou verificar se há cabos soltos ou mal ligados.",
    "Como corrigir problemas de ligação Wi-Fi?": "Verifique se o Wi-Fi está ativado, se o router está a funcionar corretamente e se está ligado à rede certa. Se necessário, reinicie o router ou desligue e ligue novamente a rede.",
    "O meu computador está a bloquear, o que fazer?": "Tente fechar programas que estão a utilizar muitos recursos ou reiniciar o computador. Se o problema persistir, pode verificar se há atualizações do sistema ou realizar uma verificação de vírus.",
    "Como melhorar o desempenho do computador?": "Pode melhorar o desempenho do seu computador: 1) Feche programas desnecessários, 2) Faça uma limpeza de disco para libertar espaço, 3) Verifique se o seu computador necessita de mais memória RAM ou até mesmo de um SSD.",
    "Como posso saber se o meu computador tem vírus?": "Pode instalar e executar um antivírus atualizado para verificar se há malware. Além disso, se o computador estiver mais lento do que o normal ou a apresentar comportamentos estranhos, pode ser um sinal de infecção.",
}

# Função principal do chatbot
def chatbot():
    # Título da aplicação no Streamlit
    st.title("Chatbot de Suporte Técnico")
    st.write("Bem-vindo! Pergunte sobre problemas técnicos de computadores e impressoras.")

    # Caixa de texto onde o utilizador digita a pergunta
    pergunta = st.text_input("Qual é a sua dúvida?")

    # Responder com base na pergunta do utilizador
    if pergunta:
        resposta = faq.get(pergunta, "Desculpe, não tenho uma resposta para essa dúvida. Tente outra pergunta!")
        st.write(f"**Resposta:** {resposta}")

if __name__ == "__main__":
    chatbot()

