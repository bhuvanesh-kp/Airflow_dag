from airflow.sdk import dag, task
import datetime

@dag(
    schedule=None,
    start_date=datetime.datetime(2026,5,5),
    end_date=datetime.datetime(2026,5,30),
    catchup=True,
    dag_id="multi_tag_dag",
    tags=["dag_topic_1", "dag_topic_2", "dag_topic_3"]
)
def dag_definer():
    @task
    def task_1():
        print("hello to dag 1")
        

    @task
    def task_2(**context):
        print("hello from dag 2")
    
    task_1() >> task_2()

dag_definer()