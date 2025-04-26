from telegram.ext import ApplicationBuilder, CommandHandler
from src.config import TELEGRAM_TOKEN
from src.handlers.start import start
from src.handlers.escalacao import escalacao
from src.handlers.resultado import resultado
from src.handlers.proximo import proximo

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
