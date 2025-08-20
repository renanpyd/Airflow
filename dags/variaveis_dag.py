<<<<<<< HEAD
# variaveis_dag.py

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.models import Variable

dag =  DAG('variaveis_dag', description="variaveis",
        schedule_interval=None,start_date=datetime(2023,3,5),
        catchup=False)

def print_variable(**context):
    minha_var = Variable.get('minhavar')
    print(f'O valor da variável é: {minha_var}')


task1 = PythonOperator(task_id="tsk1",python_callable=print_variable,dag=dag )

task1

=======
# variaveis_dag.py

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.models import Variable

dag =  DAG('variaveis_dag', description="variaveis",
        schedule_interval=None,start_date=datetime(2023,3,5),
        catchup=False)

def print_variable(**context):
    minha_var = Variable.get('minhavar')
    print(f'O valor da variável é: {minha_var}')


task1 = PythonOperator(task_id="tsk1",python_callable=print_variable,dag=dag )

task1

>>>>>>> 938d0b58fd40854fd0d30676f3b97195716e337d
