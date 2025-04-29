from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Fala, fã da FURIA! 🐾\n"
        "Use:\n"
        "/escalacao -> Mostra os jogadores das equipes da FURIA em todas as modalidades disponíveis / ativas.\n"
        "/resultado -> Exibe os resultados das 5 últimas partidas dos times disponíveis / ativos.\n"
        "/proximo -> Mostra os próximos jogos programados da FURIA dos times disponíveis / ativos."
    )

