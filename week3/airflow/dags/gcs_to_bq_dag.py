import os
import logging

from airflow import DAG
from airflow.utils.dates import days_ago

from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'trips_data_all')

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="gcs_to_bq_dag",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['dtc-de'],
) as dag:

    gcs_2_bq_ext_task = BigQueryCreateExternalTableOperator(
        task_id="gcs_2_bq_ext_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "external_yellow_tripdata_2019",
            },
            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/raw/yellow_tripdata/2019/*"],
            },
        },
    )

    CREATE_PART_TBL_QUERY = (
        f"CREATE OR REPLACE TABLE {PROJECT_ID}.{BIGQUERY_DATASET}.yellow_tripdata_partitoned \
        PARTITION BY DATE(tpep_pickup_datetime) AS \
        SELECT * FROM {PROJECT_ID}.{BIGQUERY_DATASET}.external_yellow_tripdata_2019;"
    )

    bq_ext_2_part_task = BigQueryInsertJobOperator(
        task_id="bq_ext_2_part_task",
        configuration={
            "query":{
                "query": CREATE_PART_TBL_QUERY,
                "useLegacySql": False,
            }
        }
    )

    gcs_2_bq_ext_task >> bq_ext_2_part_task