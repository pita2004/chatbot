import streamlit as st

# Dicionário com perguntas e respostas predefinidas (palavras-chave relacionadas)
faq_keywords = {
    "tela azul": [
        "A tela azul pode ocorrer devido a erros graves no sistema. Aqui estão três soluções possíveis:\n\n1. **Reinicie o computador em modo de segurança:** Reinicie o computador e pressione F8 antes do carregamento do sistema. Selecione 'Modo de segurança' e veja se o sistema arranca corretamente.\n\n2. **Verifique se há atualizações de drivers:** Drivers desatualizados ou corrompidos podem causar falhas. Vá até o 'Gestor de Dispositivos', clique com o botão direito em cada dispositivo e selecione 'Atualizar driver'.\n\n3. **Verifique o hardware:** A tela azul também pode ser causada por falhas de hardware, como a memória RAM com defeito. Pode realizar um diagnóstico de hardware ou verificar se há cabos soltos ou mal ligados."
    ],
    "lentidão": [
        "Se o seu computador está lento, tente as seguintes soluções:\n\n1. **Fechar programas desnecessários:** Verifique os programas que estão a consumir muitos recursos e feche os que não são essenciais.\n\n2. **Verificar vírus e malwares:** Execute uma verificação completa com um antivírus atualizado para garantir que não há infecção.\n\n3. **Limpeza de disco:** Utilize a ferramenta de limpeza de disco para remover ficheiros temporários e outros dados desnecessários que estão a ocupar espaço no seu disco."
    ],
    "impressora": [
        "Se a sua impressora não está a imprimir, tente as seguintes soluções:\n\n1. **Verifique a ligação da impressora:** Certifique-se de que a impressora está ligada e que está corretamente conectada ao computador.\n\n2. **Verifique o status da impressora:** Aceda às configurações de impressoras e verifique se há algum erro ou se a impressora está definida como padrão.\n\n3. **Atualizar drivers da impressora:** Verifique se há atualizações para os drivers da impressora e instale-os."
    ],
    "wi-fi": [
        "Se estiver com problemas de ligação Wi-Fi, siga estas dicas:\n\n1. **Verifique se o Wi-Fi está ativado no seu computador e no router.**\n\n2. **Reinicie o router.** Se o problema persistir, tente desligar o router, esperar alguns segundos e ligá-lo novamente.\n\n3. **Esqueça e reconecte-se à rede Wi-Fi:** Aceda às configurações de Wi-Fi, 'Esqueça' a rede e depois reconecte-se com a senha."
    ],
    "vírus": [
        "Para verificar se o seu computador tem vírus:\n\n1. **Execute uma verificação com um antivírus atualizado.**\n\n2. **Se o computador estiver muito lento ou a apresentar comportamentos estranhos,** isso pode ser um sinal de infeção por vírus.\n\n3. **Verifique os processos em execução:** No 'Gestor de Tarefas', veja se há algum processo desconhecido ou suspeito a utilizar muitos recursos."
    ],
    "drivers": [
        "Os drivers são essenciais para o funcionamento dos dispositivos do computador. Se um dispositivo não estiver a funcionar corretamente, pode ser necessário atualizar os drivers. Aqui estão algumas sugestões:\n\n1. **Verificar atualizações de drivers:** Aceda ao 'Gestor de Dispositivos' e clique com o botão direito nos dispositivos para procurar atualizações.\n\n2. **Reinstalar drivers:** Se os drivers estiverem corrompidos, pode ser necessário desinstalar e instalar novamente.\n\n3. **Utilizar o Windows Update:** O Windows Update também pode ajudar a instalar drivers importantes para o funcionamento correto do sistema."
    ],
    "espaço em disco": [
        "Se o seu computador está com pouco espaço em disco, tente estas soluções:\n\n1. **Limpar ficheiros temporários:** Utilize a ferramenta de 'Limpeza de Disco' para remover ficheiros desnecessários.\n\n2. **Mover ficheiros grandes para outro dispositivo:** Se possível, mova vídeos, fotos e outros ficheiros grandes para um disco rígido externo ou para a nuvem.\n\n3. **Desinstalar programas que não usa:** Aceda ao painel de controlo e remova programas que não são necessários."
    ],
    "software": [
        "Se o seu software não está a funcionar corretamente, tente as seguintes soluções:\n\n1. **Verificar se há atualizações disponíveis:** Certifique-se de que o software está atualizado para a versão mais recente.\n\n2. **Reinstalar o software:** Se o software não está a funcionar corretamente, tente desinstalá-lo e instalá-lo novamente.\n\n3. **Verificar configurações do software:** Aceda às definições do software e veja se algo está mal configurado ou corrompido."
    ],
    "superaquecimento": [
        "Se o seu computador está a sobreaquecer, isto pode causar lentidão ou falhas. Tente estas dicas:\n\n1. **Limpar as ventoinhas e entradas de ar:** Poeira e detritos podem bloquear as ventoinhas e impedir o arrefecimento adequado.\n\n2. **Verificar a pasta térmica do processador:** Se o computador tiver um uso constante elevado, pode ser necessário reaplicar pasta térmica no processador.\n\n3. **Usar um suporte de refrigeração:** Se o seu computador for um portátil, um suporte com ventilação pode ajudar a reduzir a temperatura."
    ],
    "teclado": [
        "Se o seu teclado não está a funcionar corretamente, tente estas soluções:\n\n1. **Verificar a ligação:** Se for um teclado com fio, verifique se está bem ligado. Se for sem fio, verifique as pilhas ou a carga da bateria.\n\n2. **Verificar as configurações do teclado:** Aceda às configurações de idioma do teclado e verifique se está configurado corretamente.\n\n3. **Reinstalar os drivers do teclado:** Aceda ao 'Gestor de Dispositivos' e veja se há atualizações ou problemas com os drivers."
    ],
}

# Função para procurar palavras-chave na pergunta do utilizador
def encontrar_palavras_chave(pergunta):
    palavras_chave = []
    for chave in faq_keywords:
        if chave in pergunta.lower():
            palavras_chave.append(chave)
    return palavras_chave

# Função principal do chatbot
def chatbot():
    # Título da aplicação no Streamlit
    st.title("Chatbot de Suporte Técnico")
    st.write("Bem-vindo! Pergunte sobre problemas técnicos de computadores e impressoras.")

    # Caixa de texto onde o utilizador digita a pergunta
    pergunta = st.text_input("Qual é a sua dúvida?")

    # Verificar se há palavras-chave na pergunta
    if pergunta:
        palavras_chave = encontrar_palavras_chave(pergunta)

        # Se houver palavras-chave correspondentes, gerar a resposta
        if palavras_chave:
            for chave in palavras_chave:
                resposta = faq_keywords[chave][0]
                st.write(f"**Resposta sobre '{chave}':** {resposta}")
        else:
            st.write("Desculpe, não encontrei uma resposta para a sua dúvida. Tente usar outras palavras-chave.")

if __name__ == "__main__":
    chatbot()
