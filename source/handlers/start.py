from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Fala, torcedor da FURIA!\n"
        "Fique por dentro de tudo que rola com os times da Pantera usando os comandos abaixo:\n\n"
        "/escalacao - Veja a escalação atual dos times da FURIA em todas as modalidades ativas.\n"
        "/resultado - Confira os resultados das 5 últimas partidas dos times em atividade.\n"
        "/proximo - Saiba quando e contra quem são os próximos jogos da FURIA."
    )
