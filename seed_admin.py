"""
Crée (ou met à jour) le compte administrateur dans la base de données.

Usage:
    python seed_admin.py

Le compte créé :
    L'identifiant et le mot de passe sont fournis via
    ADMIN_USERNAME et ADMIN_PASSWORD.
"""
import asyncio
import asyncpg
import bcrypt
import os
import sys

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "").strip()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
ADMIN_FIRST = os.getenv("ADMIN_FIRST", "Administrateur").strip()
ADMIN_LAST = os.getenv("ADMIN_LAST", "").strip()


async def main():
    missing = [
        name for name, value in (
            ("DATABASE_URL", DATABASE_URL),
            ("ADMIN_USERNAME", ADMIN_USERNAME),
            ("ADMIN_PASSWORD", ADMIN_PASSWORD),
        ) if not value
    ]
    if missing:
        print(f"❌ Variables manquantes: {', '.join(missing)}")
        sys.exit(1)

    print("⏳ Connexion à la base de données...")
    try:
        pool = await asyncpg.create_pool(DATABASE_URL, ssl="require", min_size=1, max_size=2)
    except Exception as ssl_error:
        print(f"⚠️ Connexion SSL refusée ({ssl_error}); nouvelle tentative sans SSL...")
        pool = await asyncpg.create_pool(DATABASE_URL, min_size=1, max_size=2)

    async with pool.acquire() as conn:
        # Créer la table si absente, puis compléter une table existante.
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(120) UNIQUE NOT NULL,
                email    VARCHAR(120) UNIQUE,
                password_hash VARCHAR(256) NOT NULL,
                first_name TEXT,
                last_name  TEXT,
                is_admin    BOOLEAN DEFAULT FALSE,
                is_approved BOOLEAN DEFAULT FALSE,
                is_premium  BOOLEAN DEFAULT FALSE,
                subscription_expires_at    TIMESTAMPTZ,
                subscription_duration_minutes INTEGER,
                created_at TIMESTAMPTZ DEFAULT NOW()
            );
            ALTER TABLE users ADD COLUMN IF NOT EXISTS email VARCHAR(120);
            ALTER TABLE users ADD COLUMN IF NOT EXISTS password_hash VARCHAR(256);
            ALTER TABLE users ADD COLUMN IF NOT EXISTS first_name TEXT;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS last_name TEXT;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS is_admin BOOLEAN DEFAULT FALSE;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS is_approved BOOLEAN DEFAULT FALSE;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS is_premium BOOLEAN DEFAULT FALSE;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS subscription_expires_at TIMESTAMPTZ;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS subscription_duration_minutes INTEGER;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ DEFAULT NOW();
            ALTER TABLE users ADD COLUMN IF NOT EXISTS telegram_id BIGINT;
            ALTER TABLE users ADD COLUMN IF NOT EXISTS plain_password TEXT;
            CREATE UNIQUE INDEX IF NOT EXISTS users_telegram_id_uniq
                ON users(telegram_id) WHERE telegram_id IS NOT NULL;
            CREATE UNIQUE INDEX IF NOT EXISTS users_email_uniq
                ON users(email) WHERE email IS NOT NULL;
        """)

        pw_hash = bcrypt.hashpw(ADMIN_PASSWORD.encode(), bcrypt.gensalt()).decode()

        row = await conn.fetchrow("""
            INSERT INTO users
                (username, email, password_hash, first_name, last_name,
                 is_admin, is_approved, plain_password)
            VALUES ($1, $2, $3, $4, $5, TRUE, TRUE, $6)
            ON CONFLICT (username) DO UPDATE
                SET password_hash  = EXCLUDED.password_hash,
                    plain_password = EXCLUDED.plain_password,
                    is_admin       = TRUE,
                    is_approved    = TRUE,
                    first_name     = EXCLUDED.first_name,
                    last_name      = EXCLUDED.last_name
            RETURNING id, username, is_admin
        """, ADMIN_USERNAME, ADMIN_USERNAME, pw_hash,
             ADMIN_FIRST, ADMIN_LAST, ADMIN_PASSWORD)

        print("═" * 50)
        print("✅  Compte administrateur créé / mis à jour")
        print(f"   ID DB     : {row['id']}")
        print(f"   Identifiant: {row['username']}")
        print("   Mot de passe: défini via ADMIN_PASSWORD")
        print(f"   is_admin  : {row['is_admin']}")
        print("═" * 50)
        print()
        print("Étapes suivantes :")
        print("  1. Ouvrez le bot Telegram → /start")
        print("  2. Cliquez sur 🔐 Se connecter")
        print("  3. Utilisez ADMIN_USERNAME")
        print("  4. Utilisez ADMIN_PASSWORD")
        print("  → Vous verrez le panneau d'administration")

    await pool.close()


asyncio.run(main())
