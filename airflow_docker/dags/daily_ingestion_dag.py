from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "guido",
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="daily_stock_ingestion",
    start_date=datetime(2025, 4, 21, tz="Europe/Amsterdam"),
    schedule="0 16 * * *",          # every day at 16:00 local‑time
    catchup=False,                  # don’t backfill the entire past
) as dag:
    

    fetch_data = BashOperator(
        task_id="fetch_stock_data",
        bash_command="python /opt/airflow/data_ingestion/fetch_from_api.py",
    )

    upload_data = BashOperator(
        task_id="upload_to_s3",
        bash_command="python /opt/airflow/data_ingestion/upload_to_s3.py",
    )

    fetch_data >> upload_data  # Define task order