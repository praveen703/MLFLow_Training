import mlflow
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow.sklearn
from mlflow.models.signature import infer_signature

import joblib
import dagshub

dagshub.init(repo_owner='praveen703', repo_name='MLFLow_Training', mlflow=True)

mlflow.set_tracking_uri("https://dagshub.com/praveen703/MLFLow_Training.mlflow")

if __name__ == "__main__":
    #create a new workflow experiment
    mlflow.create_experiment(
        name="testing_mlflow1",
        tags={"env":"dev","version":"1.0.0"},
    )