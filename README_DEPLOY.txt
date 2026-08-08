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

   Obligatoires :
   - BOT_TOKEN          → token du bot Telegram
   - ADMINS             → identifiants Telegram admin, ex. 1190237801
   - DATABASE_URL       → Internal Database URL de la base Render
   - ADMIN_USERNAME     → identifiant du compte administrateur initial
   - ADMIN_PASSWORD     → mot de passe du compte administrateur initial
   - TELETHON_API_ID    → identifiant API Telegram
   - TELETHON_API_HASH  → hash API Telegram
   - TELETHON_SESSION   → session Telethon

   Facultatives :
   - ADMIN_FIRST / ADMIN_LAST
   - GEMINI_API_KEY

   PORT doit être 10000 pour Render (render.yaml le configure déjà).
   Utilisez l'Internal Database URL lorsque le bot est un service Render
   situé dans la même région que la base. Ne publiez jamais cette URL dans
   un dépôt ou une archive : elle contient le mot de passe PostgreSQL.

6. Cliquer "Create Web Service" → Render installe et démarre.

7. Vérifier les logs :
   - `✅ Connexion PostgreSQL établie`
   - `✅ Compte admin prêt`
   - `✅ Bot multi-canal démarré avec succès!`

Le compte administrateur initial est créé automatiquement au premier
démarrage dans cette même base. Connectez-vous dans le bot via « Se
connecter » avec ADMIN_USERNAME et ADMIN_PASSWORD. Les inscriptions sont
enregistrées dans la table `users`.

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
