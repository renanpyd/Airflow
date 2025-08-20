<<<<<<< HEAD
# producer_dag.py

from airflow import DAG
from airflow import Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd


dag =  DAG('producer', description="producer",
        schedule_interval=None,start_date=datetime(2023,3,5),
        catchup=False)

mydataset = Dataset("/opt/airflow/data/Churn_new.csv")

def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/Churn_new.csv", sep=";")

t1 = PythonOperator(task_id='t1', python_callable=my_file,dag=dag,outlets=[mydataset])
=======
# producer_dag.py

from airflow import DAG
from airflow import Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd


dag =  DAG('producer', description="producer",
        schedule_interval=None,start_date=datetime(2023,3,5),
        catchup=False)

mydataset = Dataset("/opt/airflow/data/Churn_new.csv")

def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/Churn_new.csv", sep=";")

t1 = PythonOperator(task_id='t1', python_callable=my_file,dag=dag,outlets=[mydataset])
>>>>>>> 938d0b58fd40854fd0d30676f3b97195716e337d
t1