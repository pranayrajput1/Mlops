import logging
from pathlib import Path
from src.data import process_pipeline_image_details

path = Path(__file__).resolve().parent

logger = logging.getLogger('tipper')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


PROJECT_ID = "nashtech-ai-dev-389315"
REGION = "us-central1"
SERVICE_ACCOUNT_ML = "nashtech-ai-dev-app-sa@nashtech-ai-dev-389315.iam.gserviceaccount.com"

MODEL_DISPLAY_NAME = "db_scan_model"

PIPELINE_NAME = "clustering-kubeflow"
PIPELINE_DESCRIPTION = "Kubeflow pipeline tutorial."

PIPELINE_ROOT_GCS = f"gs://{PROJECT_ID}-kubeflow-pipeline"

BASE_IMAGE_QUALIFIER = "db-scan-image"
SERVE_IMAGE_QUALIFIER = "dbscan-serve-image"


PIPELINE_DETAILS_BUCKET = "clustering-pipeline-artifact"
PIPELINE_DETAILS_FILE = "pipeline_configuration.json"
PIPELINE_IMAGE_TAG_KEY = "pipeline_image_tag"

IMAGE_TAG = process_pipeline_image_details(PIPELINE_DETAILS_BUCKET, PIPELINE_DETAILS_FILE, PIPELINE_IMAGE_TAG_KEY)

BASE_IMAGE = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/clustering-pipeline/{BASE_IMAGE_QUALIFIER}:{IMAGE_TAG}"
logger.info(f"Base Image URI: {BASE_IMAGE}")

SERVING_IMAGE = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/clustering-pipeline/{SERVE_IMAGE_QUALIFIER}:{IMAGE_TAG}"
logger.info(f"Serve Image URI: {BASE_IMAGE}")

STAGING_BUCKET = "gs://dbscan-model/"
BATCH_SIZE = 10000

PIPELINE_JSON = "dbscan_pipeline.json"
PIPELINE_ARTIFACT = "nashtech_vertex_ai_artifact"

TRIGGER_ID = "8ecef415-9458-48aa-a848-730f41924d9b"

dataset_bucket = "nashtech_vertex_ai_artifact"
dataset_name = "household_power_consumption.txt"

fit_db_model_name = "db_scan"
fit_k_means_model_name = "k_means"

cluster_image_bucket = "clustering-pipeline-artifact"

model_details_file_name = "model_details.json"
validated_file_name = "validated_model.json"

experiment_pipeline = "experiment_pipeline.json"

models_list = ["db_scan", "k_means"]

# PIPELINE_IMAGE = "us-central1-docker.pkg.dev/nashtech-ai-dev-389315/clustering-pipeline/db-scan-image"
# SERVING_IMAGE = "us-central1-docker.pkg.dev/nashtech-ai-dev-389315/clustering-pipeline/dbscan-serve-image"



