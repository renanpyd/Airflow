# agrupamento_dag.py

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

with DAG('agrupamento_dag', 
          description="DAG com agrupamento de tasks",
          schedule_interval=None,
          start_date=datetime(2025,7,8),
          catchup=False) as dag:
    
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")
    task4 = BashOperator(task_id="tsk4", bash_command="sleep 5")
    task5 = BashOperator(task_id="tsk5", bash_command="sleep 5")
    task6 = BashOperator(task_id="tsk6", bash_command="sleep 5")
    tsk_group = TaskGroup("tsk_group", dag=dag)
    task7 = BashOperator(task_id="tsk7", bash_command="sleep 5", task_group=tsk_group)
    task8 = BashOperator(task_id="tsk8", bash_command="sleep 5", task_group=tsk_group)
    task9 = BashOperator(task_id="tsk9", bash_command="sleep 5", task_group=tsk_group,
                         trigger_rule='one_failed')

task1 >> task2
task3 >> task4
[task2,task4] >> task5 >> task6
task6 >> tsk_group