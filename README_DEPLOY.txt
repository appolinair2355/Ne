╔══════════════════════════════════════════════════════════════╗
║         ASSISNT PAYEMENT — DÉPLOIEMENT RENDER.COM           ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÉTAPES DE DÉPLOIEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Créer un compte sur https://render.com

2. Nouveau service → "Web Service"

3. Choisir "Deploy from a Git repository"
   OU utiliser "Manual Deploy" avec ce ZIP

4. Paramètres du service :
   - Name      : assisnt-payement (ou votre choix)
   - Runtime   : Python 3
   - Build Cmd : pip install -r requirements.txt
   - Start Cmd : python main.py
   - Plan      : Free (suffisant pour démarrer)

5. Variables d'environnement à configurer (onglet "Environment") :

   AUCUNE variable obligatoire : tout est codé en dur dans config.py
   (BOT_TOKEN, Telethon, et DATABASE_URL = base_de_donnees_hgxo).

   Optionnel : PORT = 10000
   Optionnel : DATABASE_URL (si défini, il remplace la valeur du code)

   ⚠️ La base utilisée est l'URL EXTERNE (oregon-postgres.render.com)
   avec SSL, car l'URL interne (dpg-...-a sans domaine) ne fonctionne
   qu'entre services Render de la même région. Les deux URLs sont dans
   config.py (DATABASE_URL_EXTERNAL / DATABASE_URL_INTERNAL).
   Les tables et le compte admin sossoukouam / arrow2026 sont créés
   automatiquement au démarrage.

6. Cliquer "Create Web Service" → Render installe et démarre

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CORRECTIF (colonne telegram_id)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

La colonne users.telegram_id est de type TEXT dans la base
base_de_donnees_hgxo, alors que le code envoyait un entier (int).
asyncpg refusait la requête ("expected str, got int"), ce qui faisait
échouer : la liaison du compte à la connexion, la création de compte
depuis le bot et la reconnaissance de l'administrateur.

Corrections appliquées :
  - lectures : WHERE telegram_id::text = $1  avec str(telegram_id)
  - écritures : UPDATE/INSERT avec str(telegram_id)
  - schéma : telegram_id forcé en TEXT au démarrage
  - message d'erreur explicite si la liaison échoue

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FONCTIONNEMENT DU SYSTÈME DE PAIEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. INSCRIPTION (nouveaux utilisateurs)
   - L'utilisateur envoie /start au bot
   - Le bot demande : prénom, nom, email, mot de passe
   - Un compte est créé dans la base de données PostgreSQL
   - L'email et le mot de passe servent à se connecter sur
     https://paiement-s-curis-50u2.onrender.com

2. PAIEMENT
   - L'utilisateur clique "💳 Payer mon abonnement"
   - Le bot affiche le lien vers le site de paiement avec
     ses identifiants de connexion
   - L'utilisateur paie sur le site
   - L'utilisateur revient dans le bot et clique
     "✅ J'ai payé — Vérifier mon accès"
   - Le bot consulte la base de données pour vérifier
     que subscription_expires_at > maintenant
   - Si confirmé : accès accordé au(x) canal(aux) +
     message de remerciement Sossou Kouamé

3. EXPIRATION
   - Le bot vérifie toutes les 30 secondes
   - À expiration : l'utilisateur est retiré du canal
   - Message envoyé pour renouveler via /start

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FONCTIONNALITÉS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Inscription avec email/mot de passe (identique au site)
✅ Vérification paiement via base de données PostgreSQL
✅ Gestion multi-canaux avec accès payants
✅ IA multi-fournisseurs (Gemini, OpenAI, Groq, DeepSeek)
✅ Gestion des membres : accorder, rallonger, retirer, bloquer
✅ Mode d'emploi par canal configurable
✅ Interface admin complète par boutons
✅ Support multilingue (FR, EN, AR, ES, RU, PT, ZH...)
✅ Session Telethon persistante

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMMANDES ADMIN PRINCIPALES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/start        → Menu principal
/grant        → Accorder l'accès à un utilisateur
/extend       → Rallonger l'accès
/remove       → Retirer un membre
/channels     → Voir tous les canaux gérés
/members      → Voir les membres d'un canal
/connect      → Connecter Telethon

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FICHIERS INCLUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

main.py              → Code principal du bot
config.py            → Configuration (valeurs codées en dur)
telethon_manager.py  → Gestionnaire session Telethon
requirements.txt     → Dépendances Python
render.yaml          → Configuration Render.com
Procfile             → Commande de démarrage
runtime.txt          → Version Python (3.12)
channels_data.json   → Base de données locale (canaux/membres)
README_DEPLOY.txt    → Ce fichier

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

--------------------------------------------------------------
MISE A JOUR : GESTION DES COMPTES (admin)
--------------------------------------------------------------
- Nouvelle commande /comptes (alias /accounts) : liste paginee de TOUS les
  comptes enregistres dans la base de donnees. Reservee a l'administrateur.
- Nouveau bouton "Comptes enregistres (BD)" dans le panneau administrateur.
- Pour chaque compte : fiche detaillee (identifiant, email, prenom, nom,
  mot de passe, Telegram ID, role, approbation, abonnement, date de creation).
- Actions admin : modifier identifiant / email / prenom / nom / mot de passe,
  basculer admin, premium, approuve, delier le Telegram ID,
  et supprimer le compte (avec confirmation).
- ID administrateur : 1190237801 (variable ADMINS dans config.py).
