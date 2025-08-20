# bigdata_dag.py

from airflow import DAG
from datetime import datetime
from big_data_operator import BigDataOperator

dag =  DAG('bigdata_dag', description="Big Data Dag",
        schedule_interval=None,start_date=datetime(2025,7,9),
        catchup=False)

big_data = BigDataOperator(
        task_id="big_data",
        path_to_csv_file = '/opt/airflow/data/Churn.csv',
        path_to_save_file = '/opt/airflow/data/Churn.json',
        file_type = 'json',
        dag=dag
        )

big_data