def diga_hora():
    from datetime import datetime
    agora = datetime.now().strftime("%H:%M:%S")
    return f"A hora atual é: {agora}"

def chatbot():
    print("Olá eu sou o seu chatbot! Como posso te ajudar? (digite 'sair' para encerrar)")

    respostas = {
        "olá": "olá como você está?",
        "tudo bem": "estou bem, obrigada por perguntar e você?",
        "sair": "até logo foi bom conversa com você",
        
    }
    comandos = {
        "diga o horario": diga_hora

    }

    while True:
        usuario = input("você: ").strip().lower()
        
        if usuario == "sair":
            break
        
        if usuario in respostas:
            print(f"chatbot: {respostas[usuario]}")

       
        elif usuario in comandos:
            print(f"chatbot: {comandos[usuario]()}")
        else:
            print("chatbot: desculpe, não entendi. Pode reformula sua pergunta?")

if __name__ == "__main__":
    chatbot()