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
