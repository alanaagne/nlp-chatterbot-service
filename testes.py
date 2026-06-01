import unittest
from robo import *


LIMIAR_ACEITACAO = 0.6

class TestTerminalBordoSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.iniciado, cls.robo = iniciar()

    def testar_01_inicializacao(self):
        self.assertTrue(self.iniciado)
        self.assertIsNotNone(self.robo)

    def testar_02_saudacao_padrao(self):
        saudacoes = ["oi", "olá", "ola", "oi, tudo bem?", "como vai?", "olá, como vai?"]
        for saudacao in saudacoes:
            print(f"[TESTE SAUDAÇÃO] Avaliando: '{saudacao}'")
            confianca, resposta = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("assistente de bordo", resposta.lower())

    def testar_03_saudacao_periodo(self):
        periodos = ["bom dia", "oi, bom dia", "boa tarde", "boa noite"]
        for periodo in periodos:
            print(f"[TESTE PERÍODO] Avaliando: '{periodo}'")
            confianca, resposta = get_resposta(self.robo, periodo)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIsNotNone(resposta)


class TestTelemetriaSistemas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.robo = iniciar()

    def testar_04_suporte_vida(self):
        variacoes = [
            "relatorio do sistema de suporte a vida",
            "como esta o oxigenio e os niveis vitais",
            "status do suporte a vida",
            "verificar suporte a vida"
        ]
        for pergunta in variacoes:
            print(f"[TESTE ENG] Avaliando: '{pergunta}'")
            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Suporte à vida operando", resposta)

    def testar_05_combustivel(self):
        variacoes = [
            "nivel de combustivel e combustiveis aceitaveis",
            "quanto resta de combustivel",
            "quais elementos posso usar como combustivel",
            "status dos tanques de energia"
        ]
        for pergunta in variacoes:
            print(f"[TESTE ENG] Avaliando: '{pergunta}'")
            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertTrue(
                "motores térmicos" in resposta.lower() or
                "tanques principais" in resposta.lower(),
                f"Resposta inesperada: {resposta}"
            )

    def testar_06_defesas_casco(self):
        variacoes = [
            "status dos escudos e integridade do casco",
            "como estao as defesas da nave",
            "relatorio de danos no casco",
            "verificar blindagem"
        ]
        for pergunta in variacoes:
            print(f"[TESTE ENG] Avaliando: '{pergunta}'")
            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Defletor de escudos", resposta)


class TestNavegacaoSeguranca(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.robo = iniciar()

    def testar_07_setor_atual(self):
        variacoes = [
            "informacoes sobre o planeta e setor atual",
            "onde estamos navegando agora",
            "dados escaneados do planeta atual",
            "localizar posicao espacial"
        ]
        for pergunta in variacoes:
            print(f"[TESTE NAV] Avaliando: '{pergunta}'")
            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Quadrante Delta", resposta)

    def testar_08_logs_missao(self):
        variacoes = [
            "historico de logs de bordo",
            "quais sao as ordens de missao",
            "mostrar registros do diario de bordo",
            "revisar logs operacionais"
        ]
        for pergunta in variacoes:
            print(f"[TESTE TÁTICO] Avaliando: '{pergunta}'")
            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Diretriz atual:", resposta)

    def testar_09_radar_base(self):
        variacoes = [
            "localizacao da base mais proxima",
            "onde fica o porto seguro mais perto",
            "radar encontrar estacao espacial proxima",
            "procurar coordenadas de ancoragem"
        ]
        for pergunta in variacoes:
            print(f"[TESTE NAV] Avaliando: '{pergunta}'")
            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Estação de Reabastecimento Alfa", resposta)

    def testar_10_varredura_ameacas(self):
        variacoes = [
            "protocolo de emergencia ou varredura de ameacas",
            "procurar por naves inimigas no setor",
            "ativar varredura tatica de ameacas",
            "verificar assinaturas de energia hostis"
        ]
        for pergunta in variacoes:
            print(f"[TESTE TÁTICO] Avaliando: '{pergunta}'")
            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Varredura de curto alcance", resposta)


if __name__ == "__main__":
    unittest.main()