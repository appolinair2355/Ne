# Déploiement Render

1. Importez ce projet comme **Web Service** ou utilisez `render.yaml`.
2. Build command : `pip install -r requirements.txt`.
3. Start command : `python main.py`.
4. Dans **Environment**, ajoutez toutes les variables obligatoires listées dans `.env.example`.
5. Pour `DATABASE_URL`, utilisez l'**Internal Database URL** de la base Render située dans la même région.
6. Pour l'administrateur initial, définissez `ADMIN_USERNAME`, `ADMIN_PASSWORD`, `ADMIN_FIRST` et `ADMIN_LAST`.
7. Redéployez et vérifiez les logs : `Connexion PostgreSQL établie`, `Compte admin prêt`, puis `Bot multi-canal démarré avec succès`.

Les valeurs secrètes ne sont volontairement pas incluses dans cette archive. Ne mettez jamais une URL PostgreSQL, un token Telegram ou une session Telethon dans Git, un ZIP partagé ou le code source.
