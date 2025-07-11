# dagrundag1_dag.py

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime

dag=DAG('dagrundag1_dag', 
          description="DAG executa DAG",
          schedule_interval=None,
          start_date=datetime(2025,7,8),
          catchup=False)
    
task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(task_id="tsk2", trigger_dag_id="dagrundag2_dag", dag=dag)

task1 >> task2