# Réflexion

## TP2
1. Quel est le meilleur des 3 modèles ? Peut-on le prouver ?
   -> Oui : git log montre un commit distinct par essai, avec son message.
2. Peut-on redonner exactement le modèle de l'Essai 1 ?
   -> Oui : git checkout <commit> -- churn_model.py
3. Un camarade peut-il reproduire notre travail sur une autre machine ?
   -> Oui pour le code et les données : git clone.
## TP3
1. Meilleur modele ? -> MLflow trie les runs par f1, le resultat est date et conserve.
2. Redonner l'Essai 1 ? -> mlflow.sklearn.load_model('runs:/<id>/model').
3. Reproduire sur une autre machine ? -> En partie : code (Git), parametres et versions (requirements.txt du run). Reste l'environnement identique : Docker.

## TP4
1. Designer le modele officiel ? -> alias champion : models:/churn-model@champion.
2. Une application utilise le modele ? -> requete POST /predict avec un JSON.
3. Changer de champion ? -> deplacer l'alias et redemarrer l'API, le code ne change pas.

## TP5
1. Pourquoi Docker ? -> l'image contient Python, bibliotheques, code et modele : meme comportement partout.
2. Pourquoi Compose ? -> une commande demarre MLflow et l'API ensemble.
3. Role du volume ? -> les donnees MLflow survivent a docker compose down (sauf avec -v).
