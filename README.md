# 🐾 InfoFurioso - Telegram Bot

Um bot de Telegram para fãs da FURIA Esports!  
Com ele, você pode acompanhar:

- Escalações atualizadas
- Resultados recentes
- Próximos jogos

> Desenvolvido usando **Python** e **PandaScore API**.

---

## 📱 Bot Online!

O **InfoFurioso Bot** já está no ar e disponível no **Telegram**!  
É só acessar o link abaixo para começar a usar:

👉 [**Clique aqui para abrir o InfoFurioso Bot**](https://t.me/InfoFurioso_bot)

Adicione o bot no grupo da torcida mais **FURIOSA** do mundo e fique sempre por dentro dos jogos, escalações e resultados da nossa equipe! ♥️🐾

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
python main.py
```

O bot estará rodando e esperando as mensagens no Telegram!

---

## 📚 Comandos Disponíveis

- `/start` → Dá boas-vindas e lista os comandos disponíveis.
- `/escalacao` → Exibe a escalação dos jogadores das equipes da FURIA em todas as modalidades nas quais atuam ou atuaram, conforme disponibilizado pela API.
- `/resultado` → Exibe os resultados das 5 últimas partidas dos times disponíveis / ativos.
- `/proximo` → Mostra os próximos jogos programados da FURIA dos times disponíveis / ativos.

---

## 🛠 Estrutura do Projeto

```
infofurioso-bot/
🖊️ config.py               # Configurações e variáveis de ambiente
🖊️ main.py                 # Arquivo principal de execução do bot
🖊️ source/                 
🖊️🖊️ handlers/           # Contém os handlers dos comandos do bot
    🖊️ escalacao.py    # Handler para o comando /escalacao
    🖊️ proximo.py      # Handler para o comando /proximo
    🖊️ resultado.py    # Handler para o comando /resultado
    🖊️ start.py        # Handler para o comando /start
🖊️🖊️ services/           # Contém os serviços (integrações externas, lógicas)
    🖊️ furia_api.py    # Serviço para a integração com a API da PandaScore
🖊️ .env                    # Arquivo para armazenar variáveis de ambiente
```

---

## 🧹 Tecnologias Utilizadas

- Python 3.12
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- API [PandaScore](https://developers.pandascore.co/)
- Railway (deploy em nuvem)

**Algumas informações podem estar desatualizadas, pois a API pode demorar um pouco para atualizar, porém seu funcionamento está 100%.**

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

Criado com carinho por um e para todos os fãs da FURIA! ♥️  
**InfoFurioso Bot**: Conectando a torcida furiosa a cada jogada!

