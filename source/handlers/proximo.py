from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime, timezone, timedelta
from source.services.furia_api import buscar_proximas_partidas
from config import FURIA_IDS

async def proximo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    agora = datetime.now(timezone.utc)
    jogos_por_modalidade = {}

    for time in FURIA_IDS:
        try:
            partidas = buscar_proximas_partidas(time["id"])
        except Exception as e:
            await update.message.reply_text(f"Erro ao buscar partidas para {time['nome']}: {str(e)}")
            continue

        partidas_futuras = [
            p for p in partidas
            if p.get("begin_at") and datetime.fromisoformat(p["begin_at"].replace("Z", "+00:00")) > agora
        ]

        partidas_futuras.sort(key=lambda x: x["begin_at"])
        partidas_futuras = partidas_futuras[:3]

        for partida in partidas_futuras:
            opponents = partida.get("opponents", [])
            adversario = next(
                (op["opponent"]["name"] for op in opponents if op.get("opponent") and op["opponent"]["id"] not in [t["id"] for t in FURIA_IDS]),
                "Adversário indefinido"
            )

            campeonato = partida.get("league", {}).get("name", "Campeonato desconhecido")

            begin_at = datetime.fromisoformat(partida["begin_at"].replace("Z", "+00:00"))
            begin_at_brasilia = begin_at.astimezone(timezone(timedelta(hours=-3)))
            data_formatada = begin_at_brasilia.strftime("%d/%m/%Y às %H:%M")

            jogo_texto = f"🏆 {campeonato}\n🆚 FURIA x {adversario}\n📅 {data_formatada}"

            modalidade = time["nome"]
            if modalidade not in jogos_por_modalidade:
                jogos_por_modalidade[modalidade] = []
            jogos_por_modalidade[modalidade].append(jogo_texto)

    if not jogos_por_modalidade:
        await update.message.reply_text("Nenhuma próxima partida da FURIA encontrada.")
        return

    mensagem_final = "📅 *Próximos jogos da FURIA:*\n\n"
    for modalidade, jogos in jogos_por_modalidade.items():
        mensagem_final += f"🎮 *{modalidade}*\n"
        for jogo in jogos:
            mensagem_final += jogo + "\n\n"

    await update.message.reply_text(mensagem_final, parse_mode="Markdown")
