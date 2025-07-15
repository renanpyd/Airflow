# defaultargs_dag.py

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2025,7,12),
    'email': ['renan.pyd@gamil.com', 'rm.garlug@gmail.com'],
    'email_on_failure': 'rlandrade@gmail.com', # Posso colocar: False
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

with DAG('defaultargs_dag', 
          description="DAG de exemplo de argumento padrão",
          default_args=default_args, 
          schedule_interval='@hourly',
          start_date=datetime(2025,7,12),
          catchup=False,
          default_view='graph',
          tags=['processos', 'pipeline', 'argumentos']
     ) as dag:
    
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", retries=3)
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")

task1 >> task2 >> task3