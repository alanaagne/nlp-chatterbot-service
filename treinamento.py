from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import time

NOME_ROBO = "assistente_de_bordo"

time.clock = time.time

ARQUIVOS_CONVERSAS = [
    "conversas/saudacoes.json",
    "conversas/navegacao_seguranca.json",
    "conversas/telemetria_sistema.json"
]

def iniciar():
    iniciado, robo, treinador = False, None, None

    try:

        robo = ChatBot(NOME_ROBO)
        treinador = ListTrainer(robo)

        iniciado = True

    except Exception as e:
        print(f"Erro iniciando robô: {e}")

    return iniciado, robo, treinador

def carregar_conversas():
    carregadas, conversas = False, []

    for aquivo_conversas in ARQUIVOS_CONVERSAS:
        try:

            with open(aquivo_conversas, "r", encoding="utf-8") as arquivo:
                treinamento = json.load(arquivo)
                conversas.append(treinamento["conversas"])

                arquivo.close()

            carregadas = True

        except Exception as e:
            print(f"Erro carregando conversas: {e}")

    return carregadas, conversas

def treinar(treinador, conversas):
    for conversas in conversas:
        for mensagens_resposta in conversas:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            for mensagem in mensagens:
                print(f"Treinando a mensagem: '{mensagem}' + resposta '{resposta}'")
                treinador.train([mensagem.lower(), resposta])

if __name__ == "__main__":
    iniciado, robo, treinador = iniciar()
    if iniciado:
        carregadas, conversas = carregar_conversas()
        if carregadas:
            treinar(treinador, conversas)