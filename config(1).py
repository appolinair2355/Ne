"""
Bot Telegram - Gestionnaire d'Accès Multi-Canal
Configuration pour déploiement Render.com (port 10000)
"""

import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7573497633:AAHk9K15yTCiJP-zruJrc9v8eK8I9XhjyH4")

ADMINS_STR = os.getenv("ADMINS", "1190237801")
ADMINS = [int(x.strip()) for x in ADMINS_STR.split(",") if x.strip()]

PORT = int(os.getenv("PORT", "5000"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

TELETHON_API_ID = int(os.getenv("TELETHON_API_ID", "29177661"))
TELETHON_API_HASH = os.getenv("TELETHON_API_HASH", "a8639172fa8d35dbfd8ea46286d349ab")
TELETHON_SESSION = os.getenv("TELETHON_SESSION", "1BJWap1wBu5Q2QlA2XGCudsz-9zByA10uz2vjv__WqWqPKdRK67XZ48mI0kXJ9nTVfKHEit5iUXJEUnIP3nGWjNyxBKnQZ3ReKiGBfNpH05yVA_sNq5-7WdEAwwYyb0wbRp9gUH13fR1176pUNO5C92WsSFZ8KZaIgxWIMG8XdrZXd5dZaskufbaBH60pP_PmgdHZfERuJQKxqN1T1iQpR1n9jQWwjaBBCfGugF0r0-3A_u1lpzv-pQc-Uptx4XQbUpyzxXExx9hR3MFsCdv9s1Tjb4EawlLD3xcwgh4L_XOP9jwcwTCU5C_-B6Ur6kc8BKkb3h3Bs1efn--fID4y3fY7GpU7yis=")

_DATABASE_URL_FALLBACK = "postgresql://carriere_user:UEnfn3QJDKcW8TVu0j2CQnNDkq3lcyLI@dpg-d9n6e4rl550s739d2fsg-a/carriere"
DATABASE_URL = os.getenv("DATABASE_URL", _DATABASE_URL_FALLBACK)

if not os.getenv("DATABASE_URL"):
    import logging
    logging.getLogger(__name__).warning(
        "⚠️ DATABASE_URL non défini dans l'environnement — utilisation de la valeur codée en dur dans config.py. "
        "Si cette base a expiré (bases gratuites Render supprimées après 90 jours) ou a été recréée, "
        "définis la variable d'environnement DATABASE_URL sur Render avec l'URL actuelle."
    )

DATA_FILE = "channels_data.json"
CHECK_INTERVAL = 60
