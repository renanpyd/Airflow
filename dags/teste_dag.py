<<<<<<< HEAD
﻿# teste_dag.py

from airflow import DAG
from datetime import datetime
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "Renan",
    "start_date": datetime(2025, 7, 8),
}

dag = DAG(
    "teste_dag",
    default_args=default_args,
    schedule_interval="15 10 * * 1-5",
    max_active_runs=1,
)

primeira_task = DummyOperator(
    task_id="primeira_task",
    dag=dag
)

def test_function():
    print('Primeira DAG')
    print('Primeira DAG print 2')

task_python_operator = PythonOperator(
    task_id='task_python_operator',
    python_callable=test_function,
    dag=dag
)

segunda_task = DummyOperator(
    task_id="segunda_task",
    dag=dag
)

ultima_task = DummyOperator(
    task_id="ultima_task",
    dag=dag
)

=======
﻿# teste_dag.py

from airflow import DAG
from datetime import datetime
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "Renan",
    "start_date": datetime(2025, 7, 8),
}

dag = DAG(
    "teste_dag",
    default_args=default_args,
    schedule_interval="15 10 * * 1-5",
    max_active_runs=1,
)

primeira_task = DummyOperator(
    task_id="primeira_task",
    dag=dag
)

def test_function():
    print('Primeira DAG')
    print('Primeira DAG print 2')

task_python_operator = PythonOperator(
    task_id='task_python_operator',
    python_callable=test_function,
    dag=dag
)

segunda_task = DummyOperator(
    task_id="segunda_task",
    dag=dag
)

ultima_task = DummyOperator(
    task_id="ultima_task",
    dag=dag
)

>>>>>>> 938d0b58fd40854fd0d30676f3b97195716e337d
primeira_task >> task_python_operator >> segunda_task >> ultima_task