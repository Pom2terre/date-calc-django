# 🛠️ Guide de contribution et de mise en production

Ce document décrit les étapes à suivre pour modifier, tester, et déployer ton application Django `date-calc-django`.

---

## ✅ 1. Modifier l’interface utilisateur (HTML / CSS)

Si tu modifies uniquement les fichiers HTML/CSS :

* Ex: `app/templates/calculate_duration.html`
* Aucune modification de `views.py` n’est nécessaire

### Etapes :

1. Modifier le HTML/CSS localement
2. Tester avec `python manage.py runserver`
3. Commit + push

```bash
git add app/templates/calculate_duration.html
git commit -m "💄 Amélioration UI"
git push origin main
```

---

## ✅ 2. Ajouter un nouveau champ dans le formulaire

Exemple : case à cocher "Inclure la date du jour"

### Etapes :

1. Modifier `forms.py` : ajouter un champ
2. Modifier `views.py` : le lire et l’ajouter au contexte `context['nom']`
3. Modifier le template : afficher le champ avec `{{ form.nom }}`

---

## ✅ 3. Afficher une nouvelle donnée dynamique

Exemple : la version de l’application ou l’environnement actif

### Etapes :

1. Ajouter la variable dans `views.py` :

```python
context['app_version'] = settings.APP_VERSION
```

2. L’afficher dans le template :

```django
<p>{{ app_version }}</p>
```

---

## 🚀 4. Déploiement sur Azure via GitHub Actions

Chaque push sur la branche `main` :

* Lance le workflow GitHub Actions
* Incrémente automatiquement la version `app/version.py`
* Déploie l’app sur Azure

### Pour forcer un redeploiement :

```bash
echo "# trigger" >> README.md
git add README.md
git commit -m "🚀 Redeploiement test"
git push origin main
```

---

## 📌 Bonnes pratiques

* Ne jamais inclure de secrets en clair (clefs, tokens, etc.)
* Toujours tester localement avant un push
* Nommer les commits clairement (ex: `✨ ajout bouton retour`, `🔥 suppression debug`, etc.)
* Utiliser `app/version.py` pour définir manuellement une version majeure (`1.3.0`)

---

✅ Tu es maintenant prêt(e) à modifier, tester et déployer sans erreur !
