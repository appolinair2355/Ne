"""
Bot Telegram - Gestionnaire d'Accès Multi-Canal
Configuration pour déploiement Render.com
Toutes les valeurs sensibles doivent venir des variables d'environnement Render.
"""

import os


def _env(name: str, default: str = "") -> str:
    """Lit une variable d'environnement en nettoyant espaces et guillemets
    (une valeur collée avec des quotes dans Render casse sinon la connexion)."""
    val = os.getenv(name)
    if val is None:
        return default
    val = val.strip().strip('"').strip("'").strip()
    return val or default


BOT_TOKEN = _env("BOT_TOKEN")

ADMINS_STR = _env("ADMINS", "")
ADMINS = [int(x.strip()) for x in ADMINS_STR.split(",") if x.strip().isdigit()]

PORT = int(_env("PORT", "10000"))

GEMINI_API_KEY = _env("GEMINI_API_KEY")

TELETHON_API_ID = int(_env("TELETHON_API_ID", "0") or 0)
TELETHON_API_HASH = _env("TELETHON_API_HASH")
TELETHON_SESSION = _env("TELETHON_SESSION")

# ═══════════════════════════════════════════════════════════
# BASE DE DONNÉES POSTGRESQL (Render.com)
# ═══════════════════════════════════════════════════════════
# Utilisez l'"Internal Database URL" si le web service est dans la même région
# que la base, sinon l'"External Database URL" (SSL obligatoire).
DATABASE_URL = _env("DATABASE_URL")

# asyncpg n'accepte pas le préfixe "postgres://" ni les options ?sslmode=
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = "postgresql://" + DATABASE_URL[len("postgres://"):]
if "?" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.split("?", 1)[0]

DATA_FILE = "channels_data.json"
CHECK_INTERVAL = 60
