import requests
from src.config import HEADERS

def buscar_equipe(slug):
    url = f"https://api.pandascore.co/teams?search[name]={slug}"
    res = requests.get(url, headers=HEADERS, timeout=10)
    res.raise_for_status()
    return res.json()

def buscar_partidas_passadas(game_key, team_id, data_inicio, data_fim, limite=5):
    url = (
        f"https://api.pandascore.co/{game_key}/matches/past"
        f"?filter[opponent_id]={team_id}"
        f"&range[begin_at]={data_inicio},{data_fim}"
        f"&sort=-begin_at&per_page={limite}"
    )
    res = requests.get(url, headers=HEADERS, timeout=10)
    res.raise_for_status()
    return res.json()

def buscar_proximas_partidas(team_id):
    url = f"https://api.pandascore.co/teams/{team_id}/matches"
    res = requests.get(url, headers=HEADERS, timeout=10)
    res.raise_for_status()
    return res.json()
