from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_TOKEN
from source.handlers.start import start
from source.handlers.escalacao import escalacao
from source.handlers.resultado import resultado
from source.handlers.proximo import proximo

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("escalacao", escalacao))
    app.add_handler(CommandHandler("resultado", resultado))
    app.add_handler(CommandHandler("proximo", proximo))

    app.run_polling()

if __name__ == "__main__":
    print("Bot rodando...")
    main()
    print("\nEncerrando o bot. Até mais! 👋")
