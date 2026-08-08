"""Configuration du bot.

Les valeurs sensibles doivent être définies dans l'environnement du service
(Render Environment ou Replit Secrets), jamais dans le dépôt ou l'archive ZIP.
"""

import os


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(
            f"Variable d'environnement obligatoire absente: {name}. "
            "Ajoutez-la dans Render > Environment."
        )
    return value


BOT_TOKEN = "7989231030:AAGouDi684CxXUy2f5GpQTtNkyu6rQoVVoQ"

ADMINS_STR = "1190237801"
try:
    ADMINS = [int(x.strip()) for x in ADMINS_STR.split(",") if x.strip()]
except ValueError as exc:
    raise RuntimeError("ADMINS doit contenir des identifiants Telegram numériques séparés par des virgules.") from exc
if not ADMINS:
    raise RuntimeError("ADMINS doit contenir au moins un identifiant Telegram.")

PORT = int(os.getenv("PORT", "5000"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

TELETHON_API_ID = 29177661
TELETHON_API_HASH = "a8639172fa8d35dbfd8ea46286d349ab"
TELETHON_SESSION = "1BJWap1wBu5Q2QlA2XGCudsz-9zByA10uz2vjv__WqWqPKdRK67XZ48mI0kXJ9nTVfKHEit5iUXJEUnIP3nGWjNyxBKnQZ3ReKiGBfNpH05yVA_sNq5-7WdEAwwYyb0wbRp9gUH13fR1176pUNO5C92WsSFZ8KZaIgxWIMG8XdrZXd5dZaskufbaBH60pP_PmgdHZfERuJQKxqN1T1iQpR1n9jQWwjaBBCfGugF0r0-3A_u1lpzv-pQc-Uptx4XQbUpyzxXExx9hR3MFsCdv9s1Tjb4EawlLD3xcwgh4L_XOP9jwcwTCU5C_-B6Ur6kc8BKkb3h3Bs1efn--fID4y3fY7GpU7yis="  # à générer, voir message précédent

DATABASE_URL = "postgresql://base_de_donnees_hgxo_user:Y121g3HpUQE9YpORWPeudA1MrHPLjeXO@dpg-d9qtu967bikc73ejg52g-a/base_de_donnees_hgxo"

# Compte de secours créé après la migration du schéma.
ADMIN_USERNAME = "sossoukouam"
ADMIN_PASSWORD = "arrow2026"
ADMIN_FIRST = os.getenv("ADMIN_FIRST", "Administrateur").strip()
ADMIN_LAST = os.getenv("ADMIN_LAST", "").strip()

DATA_FILE = "channels_data.json"
CHECK_INTERVAL = 60
