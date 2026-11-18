import shutil
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("churn_data.csv")
X = pd.get_dummies(df.drop(columns=["churn"]), columns=["abonnement"])
y = df["churn"]

# random_state=42 : même résultat à chaque exécution (indispensable en CI)
modele = RandomForestClassifier(n_estimators=100, random_state=42)
modele.fit(X, y)

# save_model refuse un dossier non vide : on supprime l'ancien d'abord
shutil.rmtree("model", ignore_errors=True)
mlflow.sklearn.save_model(modele, "model", serialization_format="cloudpickle")
print("Modèle entraîné et écrit dans le dossier model/")