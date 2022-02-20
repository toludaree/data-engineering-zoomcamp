import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from dag_python_tasks import convert_to_parquet, upload_to_gcs


PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

URL_PREFIX = "https://s3.amazonaws.com/nyc-tlc/trip+data"

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

def download_parquetize_upload_remove_dag(
    dag,
    url_template,
    csv_file_template,
    parquet_file_template,
    gcs_path_template,
):
    with dag:
        download_dataset_task = BashOperator(
            task_id="download_dataset_task",
            bash_command=f"curl -sSLf {url_template} > {AIRFLOW_HOME}/{csv_file_template}",
        )

        convert_to_parquet_task = PythonOperator(
            task_id = "convert_to_parquet_task",
            python_callable=convert_to_parquet,
            op_kwargs=dict(
                src_file=f"{AIRFLOW_HOME}/{csv_file_template}",
                dest_file=f"{AIRFLOW_HOME}/{parquet_file_template}"
            ),
        )

        local_to_gcs_task = PythonOperator(
            task_id="local_to_gcs_task",
            python_callable=upload_to_gcs,
            op_kwargs=dict(
                bucket=BUCKET,
                object_name=gcs_path_template,
                local_file=f"{AIRFLOW_HOME}/{parquet_file_template}",
            ),
        )

        remove_local_files_task = BashOperator(
            task_id="remove_local_files_task",
            bash_command=f"rm {AIRFLOW_HOME}/{csv_file_template} {AIRFLOW_HOME}/{parquet_file_template}",
        )

        download_dataset_task >> convert_to_parquet_task >> local_to_gcs_task >> remove_local_files_task


YELLOW_TAXI_URL_TEMPLATE = URL_PREFIX + "/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv"
YELLOW_TAXI_CSV_FILE_TEMPLATE = "/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv"
YELLOW_TAXI_PARQUET_FILE_TEMPLATE = YELLOW_TAXI_CSV_FILE_TEMPLATE.replace(".csv", ".parquet")
YELLOW_TAXI_GCS_PATH_TEMPLATE = "raw/yellow_tripdata/{{ execution_date.strftime(\'%Y\') }}/{{ execution_date.strftime(\'%Y-%m\') }}.parquet"

yellow_taxi_dag = DAG(
    dag_id="yellow_taxi_data_dag",
    default_args=default_args,
    schedule_interval="0 6 2 * *",
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2021, 12, 31),
    catchup=True,
    max_active_runs=3,
    tags=['dtc-de'],
)

download_parquetize_upload_remove_dag(
    yellow_taxi_dag,
    YELLOW_TAXI_URL_TEMPLATE,
    YELLOW_TAXI_CSV_FILE_TEMPLATE,
    YELLOW_TAXI_PARQUET_FILE_TEMPLATE,
    YELLOW_TAXI_GCS_PATH_TEMPLATE
)

GREEN_URL_TEMPLATE = URL_PREFIX + "/green_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv"
GREEN_CSV_FILE_TEMPLATE = "/green_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv"
GREEN_PARQUET_FILE_TEMPLATE = GREEN_CSV_FILE_TEMPLATE.replace(".csv", ".parquet")
GREEN_GCS_PATH_TEMPLATE = "raw/green_tripdata/{{ execution_date.strftime(\'%Y\') }}/{{ execution_date.strftime(\'%Y-%m\') }}.parquet"


green_taxi_dag = DAG(
    dag_id="green_taxi_data_dag",
    default_args=default_args,
    schedule_interval="0 6 2 * *",
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2019, 12, 31),
    catchup=True,
    max_active_runs=3,
    tags=['dtc-de'],
)

download_parquetize_upload_remove_dag(
    green_taxi_dag,
    GREEN_URL_TEMPLATE,
    GREEN_CSV_FILE_TEMPLATE,
    GREEN_PARQUET_FILE_TEMPLATE,
    GREEN_GCS_PATH_TEMPLATE
)


FHV_URL_TEMPLATE = URL_PREFIX + "/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv"
FHV_CSV_FILE_TEMPLATE = "/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv"
FHV_PARQUET_FILE_TEMPLATE = FHV_CSV_FILE_TEMPLATE.replace(".csv", ".parquet")
FHV_GCS_PATH_TEMPLATE = "raw/fhv_tripdata/{{ execution_date.strftime(\'%Y\') }}/{{ execution_date.strftime(\'%Y-%m\') }}.parquet"


fhv_dag = DAG(
    dag_id="fhv_data_dag",
    default_args=default_args,
    schedule_interval="0 6 2 * *",
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2019, 12, 31),
    catchup=True,
    max_active_runs=3,
    tags=['dtc-de'],
)

download_parquetize_upload_remove_dag(
    fhv_dag,
    FHV_URL_TEMPLATE,
    FHV_CSV_FILE_TEMPLATE,
    FHV_PARQUET_FILE_TEMPLATE,
    FHV_GCS_PATH_TEMPLATE
)


ZONES_URL_TEMPLATE = "https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"
ZONES_CSV_FILE_TEMPLATE = "/taxi_zone_lookup.csv"
ZONES_PARQUET_FILE_TEMPLATE = ZONES_CSV_FILE_TEMPLATE.replace(".csv", ".parquet")
ZONES_GCS_PATH_TEMPLATE = "raw/taxi_zones/taxi_zone_lookup.parquet"

zones_dag = DAG(
    dag_id="zones_dag",
    default_args=default_args,
    schedule_interval="@once",
    start_date=days_ago(1),
    catchup=False,
    max_active_runs=3,
    tags=['dtc-de'],
)

download_parquetize_upload_remove_dag(
    zones_dag,
    ZONES_URL_TEMPLATE,
    ZONES_CSV_FILE_TEMPLATE,
    ZONES_PARQUET_FILE_TEMPLATE,
    ZONES_GCS_PATH_TEMPLATE
)