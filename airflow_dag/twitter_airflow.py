from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl,run_twitter_post

default_args= {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['test@sample.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}
dag = DAG(
    'twitter_dag',
    default_args = default_args,
    description = 'Post Daily Covid Wordcloud on Twitter',
    schedule_interval = '0 09 * * *',
)

start = DummyOperator(task_id = 'start',dag=dag)

run_etl = PythonOperator(
    task_id = 'run_etl',
    python_callable = run_twitter_etl,
    dag=dag,
)

run_post = PythonOperator(
    task_id = 'run_post',
    python_callable = run_twitter_post,
    dag=dag
)

end = DummyOperator(task_id = 'end',dag=dag)

start >> run_etl >> run_post >> end
