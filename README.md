# 📅 date-calc-django

![Commits signés](https://img.shields.io/badge/Commits-Vérifiés-green?style=flat-square&logo=github)

Une application Django 🐍 permettant de calculer intelligemment des intervalles de dates utiles pour la planification, les délais, et la gestion de durées légales ou techniques.

---

## 🚀 Fonctionnalités principales

- Calcul d’intervalle entre deux dates
- Ajout/soustraction de jours ouvrés ou calendaires
- Interface web intuitive avec modèles HTML
- Système Django MVC complet

---

## ⚙️ Installation rapide

1. Clone le projet :

```bash
git clone git@github.com:pom2terre/date-calc-django.git
cd date-calc-django
```

2. Crée un environnement virtuel :
   python3 -m venv venv
   source venv/bin/activate

3. Installe les dépendances :
   pip install -r requirements.txt

4. Applique les migrations & lance le serveur :
   python manage.py migrate
   python manage.py runserver

5. Puis visite : http://127.0.0.1:8000

```markdown
## 📂 Structure du projet

date-calc-django/
├── app/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── templates/
│ │ ├── index.html
│ │ └── calculate_duration.html
│ └── migrations/
│ └── **init**.py
├── settings.py
├── urls.py
├── wsgi.py
├── asgi.py
├── manage.py
├── db.sqlite3
├── requirements.txt
├── duration.py
├── startup.sh
├── signature.txt
├── signature-final.txt
└── README.md
```

## ✍️ Commits signés

Tous les commits de ce projet sont signés via une clé SSH vérifiée par GitHub, assurant leur authenticité ✅

## 📜 Licence

Distribué sous licence MIT
© 2025 pom2terre

```

```
# redeploy
