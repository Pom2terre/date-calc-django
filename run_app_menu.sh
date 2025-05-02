#!/bin/bash

# Détection ou choix de l’environnement
echo "Choisir l'environnement :"
select ENV in "local" "azure"; do
  case $ENV in
    local )
      echo "Lancement en local..."
      export DJANGO_ENV=dev
      export DJANGO_DEBUG=True
      python manage.py runserver
      break;;
    azure )
      echo "Ouverture de l'app sur Azure..."
      xdg-open "https://my-python-app123.azurewebsites.net" 2>/dev/null || start "https://my-python-app123.azurewebsites.net"
      break;;
    * )
      echo "Choix invalide";;
  esac
done
