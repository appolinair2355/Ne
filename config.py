"""
Bot Telegram - Gestionnaire d'Accès Multi-Canal
Configuration pour déploiement Render.com (port 10000)
"""

import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8359623168:AAHno00lno02QOw5OvGukP0TIgn4sDFB158")

ADMINS_STR = os.getenv("ADMINS", "1190237801")
ADMINS = [int(x.strip()) for x in ADMINS_STR.split(",") if x.strip()]

PORT = int(os.getenv("PORT", "5000"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

TELETHON_API_ID = int(os.getenv("TELETHON_API_ID", "29177661"))
TELETHON_API_HASH = os.getenv("TELETHON_API_HASH", "a8639172fa8d35dbfd8ea46286d349ab")
TELETHON_SESSION = os.getenv("TELETHON_SESSION", "1BJWap1wBu5Q2QlA2XGCudsz-9zByA10uz2vjv__WqWqPKdRK67XZ48mI0kXJ9nTVfKHEit5iUXJEUnIP3nGWjNyxBKnQZ3ReKiGBfNpH05yVA_sNq5-7WdEAwwYyb0wbRp9gUH13fR1176pUNO5C92WsSFZ8KZaIgxWIMG8XdrZXd5dZaskufbaBH60pP_PmgdHZfERuJQKxqN1T1iQpR1n9jQWwjaBBCfGugF0r0-3A_u1lpzv-pQc-Uptx4XQbUpyzxXExx9hR3MFsCdv9s1Tjb4EawlLD3xcwgh4L_XOP9jwcwTCU5C_-B6Ur6kc8BKkb3h3Bs1efn--fID4y3fY7GpU7yis=")

# ═══════════════════════════════════════════════════════════
# BASE DE DONNÉES POSTGRESQL (Render.com) — codée en dur
# ═══════════════════════════════════════════════════════════
# URL interne : ne fonctionne QUE depuis un service Render de la même région/compte.
DATABASE_URL_INTERNAL = "postgresql://base_de_donnees_hgxo_user:Y121g3HpUQE9YpORWPeudA1MrHPLjeXO@dpg-d9qtu967bikc73ejg52g-a/base_de_donnees_hgxo"
# URL externe : fonctionne partout (SSL obligatoire). C'est la valeur par défaut.
DATABASE_URL_EXTERNAL = "postgresql://base_de_donnees_hgxo_user:Y121g3HpUQE9YpORWPeudA1MrHPLjeXO@dpg-d9qtu967bikc73ejg52g-a.oregon-postgres.render.com/base_de_donnees_hgxo"

DATABASE_URL = os.getenv("DATABASE_URL") or DATABASE_URL_EXTERNAL

DATA_FILE = "channels_data.json"
CHECK_INTERVAL = 60
