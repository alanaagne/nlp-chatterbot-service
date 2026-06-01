# NLP Chatterbot Service

## Visão geral

Esse projeto foi desenvolvido para a disciplina inteligência artificial do curso de Sistemas de Informação e embora tenha um tema ficcional, pode ser adaptado facilmente para diversos contextos, pois foi desenvolvido de forma modularizada de baixo acoplamento.

`nlp-chatterbot-service` é um sistema de atendimento conversacional em Python que usa `ChatterBot` para criar um assistente de bordo com cenário espacial. O projeto reúne um serviço REST em Flask, um módulo de treinamento com dados JSON e um conjunto de padrões de conversação focados em saudações, telemetria de sistema e navegação/segurança.

## Recursos principais

- Assistente conversacional em português com respostas pré-treinadas.
- Treinamento baseado em arquivos JSON de intenção e resposta.
- Serviço HTTP leve para consulta de respostas por mensagem.
- Modelo orientado a serviço com separação clara entre treinamento, runtime e interface.
- Estrutura preparada para extensão com novos domínios de conversa.

## Arquitetura do projeto

- `treinamento.py` - carrega conversas de arquivos JSON e treina o chatbot.
- `robo.py` - inicializa o bot e expõe função para obter respostas e confiança.
- `servico.py` - serviço Flask que fornece endpoints REST para consulta do assistente.
- `conversas/` - corpus de exemplo com intenções e respostas.
- `requirements.txt` - dependências Python necessárias.

## Dados de conversação

Os arquivos JSON em `conversas/` contêm blocos de `mensagens` e `resposta`, organizados em temas como:

- `saudacoes.json`
- `navegacao_seguranca.json`
- `telemetria_sistema.json`

Esses arquivos permitem treinar o bot com múltiplas variações de entrada para cada resposta.

## Tecnologias

- Python 3.x
- Flask
- ChatterBot
- JSON

## Execução

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Treinamento

Treine o assistente utilizando os dados de conversação:

```bash
python treinamento.py
```

Após o treinamento, o ChatterBot persiste o conhecimento localmente no backend padrão da biblioteca.

### Execução do serviço

Inicie a API REST Flask:

```bash
python servico.py
```
Depois dentro da pasta chat execute:

```bash
npm start
```

O serviço ficará disponível localmente.

### Endpoints disponíveis

- `GET /` - retorne informações do assistente.
- `GET /resposta/<mensagem>` - retorne a resposta gerada e o nível de confiança.

Exemplo:

```bash
curl http://127.0.0.1:5000/resposta/qual%20o%20status%20do%20sistema
```

## Uso interativo

Também é possível utilizar o módulo `robo.py` diretamente em modo interativo:

```bash
python robo.py
```

Digite mensagens em português e o assistente responderá com texto e confiança.

## Objetivos do Projeto

- Demonstra aplicação de NLP em um assistente conversacional.
- Mostra integração entre Python, Flask e dados estruturados JSON.
- Apresenta prática de criação de serviço REST e arquitetura modular.
- Permite fácil ampliação para projetos mais avançados de IA e automação.

## Observação

O diretório `chat/` contém um exemplo adicional de aplicação com `socket.io` e `express` que pode ser explorado para criar uma interface em tempo real, embora o núcleo do projeto esteja no serviço Flask Python.
