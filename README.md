# 🐾 InfoFurioso - Telegram Bot

Um bot de Telegram para fãs da FURIA Esports!  
Com ele, você pode acompanhar:

- Escalações atualizadas 🧒‍♂️  
- Resultados recentes 📊  
- Próximos jogos 🗕️

> Desenvolvido usando **Python** e **PandaScore API**.

---

## 🚀 Como Rodar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/victormacedov/infofurioso-bot.git
cd infofurioso-bot
```

2. Crie e configure o arquivo `.env`:
```
TELEGRAM_TOKEN=seu_token_telegram
PANDASCORE_TOKEN=seu_token_pandascore
FURIA_TEAM_SLUG=FURIA
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o bot:
```bash
python src/main.py
```

O bot estará rodando e esperando as mensagens no Telegram!

---

## 📚 Comandos Disponíveis

- `/start` → Dá boas-vindas e lista os comandos disponíveis.
- `/escalacao` → Mostra os jogadores das equipes da FURIA em todas as modalidades disponíveis/ativas.
- `/resultado` → Exibe os resultados das 5 últimas partidas dos times disponíveis/ativos.
- `/proximo` → Mostra os próximos jogos programados da FURIA.

---

## 🛠 Estrutura do Projeto

```
src/
├── config.py           # Configurações e variáveis do ambiente
├── main.py             # Ponto de entrada do bot
├── handlers/           # Handlers dos comandos do bot
│   ├── start.py
│   ├── escalacao.py
│   ├── resultado.py
│   └── proximo.py
└── services/
    └── furia_api.py    # Integração com a API da PandaScore
```

---

## 🧹 Tecnologias Utilizadas

- Python 3.12
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- API [PandaScore](https://developers.pandascore.co/)

---

## 🤝 Contribuindo

Contribuições são bem-vindas!  
Sinta-se livre para abrir uma _issue_ ou enviar um _pull request_.

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT.  
Veja o arquivo `LICENSE` para mais detalhes.

---

## ✨ Créditos

Criado com carinho por um e para todos os fãs da FURIA! 🖤

