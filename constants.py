from pathlib import Path

path = Path(__file__).resolve().parent

PROJECT_ID = "nashtech-ai-dev-389315"
REGION = "us-central1"
SERVICE_ACCOUNT_ML = "nashtech-ai-dev-app-sa@nashtech-ai-dev-389315.iam.gserviceaccount.com"

MODEL_DISPLAY_NAME = "db_scan_model"

PIPELINE_NAME = "clustering-kubeflow"
EXPERIMENT_PIPELINE_NAME = "experiment-pipeline"
PIPELINE_DESCRIPTION = "Kubeflow pipeline tutorial."

PIPELINE_ROOT_GCS = f"gs://{PROJECT_ID}-kubeflow-pipeline"

BASE_IMAGE_QUALIFIER = "db-scan-image"
SERVE_IMAGE_QUALIFIER = "dbscan-serve-image"

BASE_IMAGE_TAG = "0.0.1"
SERVING_IMAGE_TAG = "0.0.1"

BASE_IMAGE = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/clustering-pipeline/{BASE_IMAGE_QUALIFIER}:{BASE_IMAGE_TAG}"
SERVING_IMAGE = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/clustering-pipeline/{SERVE_IMAGE_QUALIFIER}:{BASE_IMAGE_TAG}"


STAGING_BUCKET = "gs://dbscan-model/"
BATCH_SIZE = 10000

TRIGGER_ID = "7ac634d9-8b3e-4ba3-8afa-fbff056388ad"

dataset_bucket = "nashtech_vertex_ai_artifact"
dataset_name = "household_power_consumption.txt"

fit_db_model_name = "db_scan"
fit_k_means_model_name = "k_means"

cluster_image_bucket = "clustering-pipeline-artifact"

model_details_file_name = "model_details.json"
validated_file_name = "validated_model.json"

experiment_pipeline = "experiment_pipeline.json"

models_list = ["db_scan", "k_means"]

# PIPELINE_IMAGE = "us-central1-docker.pkg.dev/nashtech-ai-dev-389315/clustering-pipeline/db-scan-image:0.0.1"
# SERVING_IMAGE = "us-central1-docker.pkg.dev/nashtech-ai-dev-389315/clustering-pipeline/dbscan-serve-image:0.0.1"