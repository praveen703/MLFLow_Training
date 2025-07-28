import mlflow
from mlflow_utils import get_mlflow_experiment
import dagshub

dagshub.init(repo_owner='praveen703', repo_name='mlflow', mlflow=True)

mlflow.set_tracking_uri("https://dagshub.com/praveen703/mlflow.mlflow")


if __name__ == "__main__":

    # retrieve the mlflow experiment
    experiment = get_mlflow_experiment(experiment_id="d", experiment_name="testing_mlflow2")

    print("Name: {}".format(experiment.name))
    print("Experiment_id: {}".format(experiment.experiment_id))
    print("Artifact Location: {}".format(experiment.artifact_location))
    print("Tags: {}".format(experiment.tags))
    print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
    print("Creation timestamp: {}".format(experiment.creation_time))
