from datetime import datetime,timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.oracle_operator import OracleOperator

default_args = {
'owner': 'mpaysan',
'depends_on_past': False,
'start_date': airflow.utils.dates.days_ago(2),
'email': ['mpaysan@cccd.edu'],
'email_on_failure': True,
'email_on_retry': False,
'retries': 0,
'retry_delay': timedelta(minutes=5)
}


with DAG('example_sql_dag',
     default_args=default_args,
     catchup=False,
     schedule_interval='*/10 * * * *'
     ) as dag:
    opr_sql = OracleOperator(task_id='task_sql',
                                       oracle_conn_id='Baninst1_DEVL',
                                       sql= 'select * from perleav')