from google.cloud import aiplatform
from datetime import datetime
import os
from constants import EXPERIMENT_PIPELINE_NAME, PROJECT_ID, REGION, SERVICE_ACCOUNT_ML, experiment_pipeline, dataset_bucket


def run_pipeline_job(
        sync: bool = False, *,
        pipeline_template_name: str = f'gs://{dataset_bucket}/{experiment_pipeline}',
        cleanup_compiled_pipeline: bool = False,
        enable_caching: bool = False,
) -> aiplatform.PipelineJob:
    job_id = f'{EXPERIMENT_PIPELINE_NAME}-{datetime.now().strftime("%Y%m%d%H%M%S")}'
    experiment_name = f'{EXPERIMENT_PIPELINE_NAME}-experiments'

    params = dict(
        project_id=PROJECT_ID,
        job_id=job_id,
    )

    aiplatform.init(project=PROJECT_ID, location=REGION)

    pipeline_job = aiplatform.PipelineJob(
        project=PROJECT_ID,
        location=REGION,
        display_name=EXPERIMENT_PIPELINE_NAME,
        template_path=pipeline_template_name,
        parameter_values=params,
        job_id=job_id,
        enable_caching=enable_caching,
    )

    try:
        pipeline_job.submit(service_account=SERVICE_ACCOUNT_ML, experiment=experiment_name)
        if sync:
            pipeline_job.wait()
    finally:
        if cleanup_compiled_pipeline:
            os.remove(pipeline_template_name)

    return pipeline_job


if __name__ == "__main__":
    run_pipeline_job()
