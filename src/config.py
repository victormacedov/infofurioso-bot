import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
PANDASCORE_TOKEN = os.getenv('PANDASCORE_TOKEN')
FURIA_TEAM_SLUG = os.getenv('FURIA_TEAM_SLUG')

HEADERS = {"Authorization": f"Bearer {PANDASCORE_TOKEN}"}

FURIA_IDS = [
    {"slug": "csgo", "id": 124530, "nome": "CS2 Masculino"},
    {"slug": "csgo", "id": 129384, "nome": "CS2 Feminino"},
    {"slug": "valorant", "id": 128477, "nome": "Valorant"},
    {"slug": "valorant", "id": 136455, "nome": "Valorant Academy"},
    {"slug": "r6siege", "id": 127596, "nome": "Rainbow Six"},
    {"slug": "lol", "id": 126688, "nome": "League of Legends"},
    {"slug": "lol", "id": 128523, "nome": "League of Legends Academy"},
    {"slug": "rl", "id": 128933, "nome": "Rocket League"}
]
