from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import os
import time

NOME_ROBO = "assistente_de_bordo"
LIMIAR_ACEITACAO = 0.6

CONVERSAS_FILES = [
    "conversas/saudacoes.json",
    "conversas/navegacao_seguranca.json",
    "conversas/telemetria_sistema.json"
]

time.clock = time.time


def carregar_conversas():
    conversas = []

    for arquivo_conversas in CONVERSAS_FILES:
        try:
            with open(arquivo_conversas, "r", encoding="utf-8") as arquivo:
                treinamento = json.load(arquivo)
                conversas.extend(treinamento.get("conversas", []))
        except Exception as e:
            print(f"Erro carregando conversas: {e}")

    return conversas


def treinar(robo):
    treinador = ListTrainer(robo)
    conversas = carregar_conversas()

    for mensagem_resposta in conversas:
        mensagens = mensagem_resposta.get("mensagens", [])
        resposta = mensagem_resposta.get("resposta", "")

        for mensagem in mensagens:
            treinador.train([mensagem.lower(), resposta])


def iniciar():
    iniciado, robo = False, None

    try:
        database_path = "db.sqlite3"
        needs_training = not os.path.exists(database_path)

        if not needs_training:
            db_mtime = os.path.getmtime(database_path)
            for arquivo_conversas in CONVERSAS_FILES:
                if os.path.getmtime(arquivo_conversas) > db_mtime:
                    needs_training = True
                    break

        if needs_training:
            if os.path.exists(database_path):
                os.remove(database_path)

            bot_para_treino = ChatBot(NOME_ROBO, database_uri=f"sqlite:///{database_path}")
            treinar(bot_para_treino)
            
            

        robo = ChatBot(NOME_ROBO, read_only=True, database_uri=f"sqlite:///{database_path}")
        iniciado = True

    except Exception as e:
        print(f"Erro iniciando robô: {e}")

    return iniciado, robo


def get_resposta(robo, mensagem):
    resposta = robo.get_response(mensagem.lower())
    return resposta.confidence, resposta.text


if __name__ == "__main__":
    iniciado, robo = iniciar()

    if iniciado:
        while True:
            mensagem = input("👩‍🚀 ")

            confianca, resposta = get_resposta(robo, mensagem)
            if confianca >= LIMIAR_ACEITACAO:
                print(f"🤖 {resposta}, confiança = {confianca}")
            else:
                # enviar pergunta não respondida para o log
                print("🤖 Não sei responder esta pergunta, por favor, pergunte outra coisa ou reformule sua pergunta")