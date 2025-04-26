import sys
import os

# Adiciona o diretório 'src' ao caminho de busca de módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_TOKEN
from handlers.start import start
from handlers.escalacao import escalacao
from handlers.resultado import resultado
from handlers.proximo import proximo

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("escalacao", escalacao))
    app.add_handler(CommandHandler("resultado", resultado))
    app.add_handler(CommandHandler("proximo", proximo))

    print("Bot rodando... 🐾")
    app.run_polling()

if __name__ == "__main__":
    main()
