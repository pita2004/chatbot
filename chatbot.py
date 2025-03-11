import streamlit as st

# Dicionário com perguntas e respostas predefinidas
faq = {
    "Como reiniciar meu computador?": "Para reiniciar seu computador, pressione o botão de 'Iniciar' e depois clique em 'Reiniciar'.",
    "Meu computador está muito lento, o que fazer?": "Tente fechar programas que estão consumindo muitos recursos ou reiniciar o computador.",
    "Como configurar uma impressora?": "Para configurar uma impressora, conecte-a ao computador, instale os drivers e defina-a como impressora padrão nas configurações de impressora.",
    "Como resolver erro de impressão?": "Verifique se a impressora está ligada, se há papel e tinta/toner suficientes, e se a impressora está corretamente conectada ao computador.",
    "Como faço para formatar meu computador?": "Para formatar seu computador, faça backup dos seus arquivos e, em seguida, inicialize o sistema com uma mídia de instalação (USB/DVD) e siga as instruções.",
    "Minha impressora não está imprimindo, o que faço?": "Verifique a conexão da impressora, se ela está ligada e se o status de impressão está correto. Além disso, veja se não há erros na fila de impressão.",
    "O que é a tela azul e como corrigir?": "A tela azul pode ocorrer devido a erros graves do sistema. Aqui estão três soluções possíveis:\n\n1. **Reinicie o computador em modo de segurança:** Reinicie o computador e pressione F8 antes do carregamento do sistema. Selecione 'Modo de segurança' e veja se o sistema inicia corretamente.\n\n2. **Verifique se há atualizações de drivers:** Driver desatualizado ou corrompido pode causar falhas. Vá até o 'Gerenciador de dispositivos', clique com o botão direito em cada dispositivo e selecione 'Atualizar driver'.\n\n3. **Verifique o hardware:** A tela azul também pode ser causada por falhas de hardware, como memória RAM com defeito. Você pode executar um diagnóstico de hardware ou verificar se há cabos soltos ou mal conectados.",
    "Como corrigir problemas de conexão Wi-Fi?": "Verifique se o Wi-Fi está ativado, se o roteador está funcionando corretamente, e se você está conectado à rede certa. Se necessário, reinicie o roteador ou desconecte e reconecte-se à rede.",
    "Meu computador está travando, o que fazer?": "Tente fechar programas que estão utilizando muitos recursos, ou reinicie o computador. Se o problema persistir, você pode verificar se há atualizações de sistema ou realizar uma verificação de vírus.",
    "Como melhorar o desempenho do computador?": "Você pode melhorar o desempenho do seu computador: 1) Feche programas desnecessários, 2) Realize uma limpeza de disco para liberar espaço, 3) Verifique se o seu computador precisa de mais memória RAM ou até mesmo um SSD.",
    "Como posso saber se o meu computador tem vírus?": "Você pode instalar e executar um antivírus atualizado para verificar se há malwares. Além disso, se o computador estiver mais lento do que o normal ou exibindo comportamentos estranhos, pode ser um sinal de infecção.",
}

# Função principal do chatbot
def chatbot():
    # Título da aplicação no Streamlit
    st.title("Chatbot de Suporte Técnico")
    st.write("Bem-vindo! Pergunte sobre problemas técnicos de computadores e impressoras.")

    # Campo de texto onde o usuário digita a pergunta
    pergunta = st.text_input("Qual é a sua dúvida?")

    # Responder com base na pergunta do usuário
    if pergunta:
        resposta = faq.get(pergunta, "Desculpe, não tenho uma resposta para essa dúvida. Tente outra pergunta!")
        st.write(f"**Resposta:** {resposta}")

if __name__ == "__main__":
    chatbot()

