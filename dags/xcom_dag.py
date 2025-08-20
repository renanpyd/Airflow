# xcom_dag.py

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
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

dag = DAG('xcom_dag', 
          description="Exemplo de como usar xcom pR wescrita e leitura", # XComs permitem que tarefas troquem metadados de tarefas ou pequenas quantidades de dados.
          schedule_interval=None,
          start_date=datetime(2025,7,8),
          catchup=False)
      
def task_write(**kwarg): # Convenção do python que permite passar um número arbitrario de parâmetros.
    kwarg['ti'].xcom_push(key='valorxcom1' ,value=10200)
    
task1 = PythonOperator(task_id="tsk1", python_callable= task_write, dag=dag)

def task_read(**kwarg):
    valor = kwarg['ti'].xcom_pull(key='valorxcom1')
    print(f"Valor recuperado: {valor}")

task2 = PythonOperator(task_id="tsk2", python_callable= task_read, dag=dag)

task1 >> task2

# O limite de tamanho dos XComs (Cross-Communication) no Apache Airflow depende do banco de dados utilizado. 
# Geralmente, é recomendado usar XComs para dados pequenos e evitar o compartilhamento de grandes volumes de dados através deles, 
# pois podem e vão impactar o desempenho. 
# Limites de tamanho por banco de dados:
#   SQLite: 2 GB
#   PostgreSQL: 1 GB
#   MySQL: 64 KB
#   Código-fonte: 48 KB 