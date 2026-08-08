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


BOT_TOKEN = required_env("BOT_TOKEN")

ADMINS_STR = required_env("ADMINS")
try:
    ADMINS = [int(x.strip()) for x in ADMINS_STR.split(",") if x.strip()]
except ValueError as exc:
    raise RuntimeError("ADMINS doit contenir des identifiants Telegram numériques séparés par des virgules.") from exc
if not ADMINS:
    raise RuntimeError("ADMINS doit contenir au moins un identifiant Telegram.")

PORT = int(os.getenv("PORT", "5000"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

TELETHON_API_ID = int(required_env("TELETHON_API_ID"))
TELETHON_API_HASH = required_env("TELETHON_API_HASH")
TELETHON_SESSION = required_env("TELETHON_SESSION")

DATABASE_URL = required_env("DATABASE_URL")

# Compte de secours créé après la migration du schéma. Ces valeurs sont
# également des variables Render afin que le mot de passe ne soit pas publié.
ADMIN_USERNAME = required_env("ADMIN_USERNAME")
ADMIN_PASSWORD = required_env("ADMIN_PASSWORD")
ADMIN_FIRST = os.getenv("ADMIN_FIRST", "Administrateur").strip()
ADMIN_LAST = os.getenv("ADMIN_LAST", "").strip()

DATA_FILE = "channels_data.json"
CHECK_INTERVAL = 60
