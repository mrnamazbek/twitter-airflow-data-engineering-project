from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from twitter_etl import run_twitter_etl

# Constants
SCHEDULE_INTERVAL = timedelta(days=1)
DEFAULT_EMAIL = ['airflow@example.com']

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': DEFAULT_EMAIL,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the DAG
twitter_etl_dag = DAG(
    'twitter_etl_dag',
    default_args=default_args,
    description='A DAG for executing the Twitter ETL process',
    schedule_interval=SCHEDULE_INTERVAL,
)

# Define the ETL task
complete_twitter_etl_task = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=twitter_etl_dag,
)
