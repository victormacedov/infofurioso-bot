from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
from source.services.furia_api import buscar_partidas_passadas
from config import FURIA_IDS

async def resultado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.today().date().isoformat()
    data_inicio = "2020-12-01"

    for equipe in FURIA_IDS:
        try:
            partidas = buscar_partidas_passadas(equipe["slug"], equipe["id"], data_inicio, today)
        except Exception as e:
            await update.message.reply_text(f"❌ Erro ao buscar partidas de {equipe['nome']}: {e}")
            continue

        if not partidas:
            await update.message.reply_text(f"⚠️ Não encontrei partidas recentes da FURIA em {equipe['nome']}.")
            continue

        msg = [f"📊 Últimas partidas da FURIA em {equipe['nome']}:\n"]
        for partida in partidas:
            try:
                opponents = partida.get("opponents", [])
                if len(opponents) != 2:
                    continue

                nome1 = opponents[0]["opponent"]["name"]
                nome2 = opponents[1]["opponent"]["name"]
                score = partida.get("results", [])
                placar = f"{nome1} x {nome2}"
                if len(score) == 2:
                    placar = f"{nome1} {score[0]['score']} x {score[1]['score']} {nome2}"

                campeonato = partida.get("league", {}).get("name", "Desconhecido")
                data_partida = partida.get("begin_at", "sem data")[:10]
                msg.append(f"🏆 {campeonato}\n📅 {data_partida}\n{placar}\n")
            except Exception as e:
                msg.append(f"(⚠️ Erro ao processar uma partida: {e})")

        await update.message.reply_text("\n".join(msg))
