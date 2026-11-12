import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("sqlite:///mlflow.db")

model = mlflow.sklearn.load_model("models:/churn-model@champion")

# Dossier ordinaire "model", copié ensuite dans l'image Docker
mlflow.sklearn.save_model(model, "model", serialization_format="cloudpickle")
print("Champion exporté dans le dossier model/")