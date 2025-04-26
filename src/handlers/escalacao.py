import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from src.services.furia_api import buscar_equipe
from src.config import FURIA_TEAM_SLUG

async def escalacao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = buscar_equipe(FURIA_TEAM_SLUG)
    except Exception:
        await update.message.reply_text("Erro ao buscar equipes da FURIA.")
        return

    if not data:
        await update.message.reply_text("Nenhuma equipe da FURIA foi encontrada.")
        return

    mensagens = []

    for team in data:
        team_name = team.get("name", "Desconhecido")
        game = team.get("current_videogame", {}).get("name", "Desconhecido")
        players = team.get("players", [])

        if players:
            nomes = [f"- {p['name']}" for p in players]
            msg = f"🎮 Modalidade: {game}\n🏴 Time: {team_name}\n👥 Jogadores:\n" + "\n".join(nomes)
        else:
            msg = f"🎮 Modalidade: {game}\n🏴 Time: {team_name}\nA FURIA não tem escalações disponíveis no momento."

        mensagens.append(msg)

    for mensagem in mensagens:
        await update.message.reply_text(mensagem)
        await asyncio.sleep(1)
