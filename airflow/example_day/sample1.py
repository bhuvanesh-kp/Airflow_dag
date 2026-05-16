import textwrap
from datetime import datetime, timedelta

# Operators; we need this to operate!
from airflow.providers.standard.operators.bash import BashOperator, PythonOperator

# The DAG object; we'll need this to instantiate a DAG
from airflow.sdk import DAG

with DAG(
    "sample1",
    default_args = {
        "depends_on_past" : False,
        "retries": 1, 
        "retry_delay": timedelta(minutes=5),
    },
    description = "This is a sample airflow dag testing",
    schedule = timedelta(days=10),
    start_date = datetime(2026, 1 ,1),
    catchup = True
) as dag:
    
    t1 = BashOperator(
        task_id = "print_date",
        bash_command = "date",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )

    templated_command = textwrap.dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
    )

    t3 = BashOperator(
        task_id = "templated",
        depends_on_past = False,
        bash_command = templated_command,
    )

    t1 >> [t2 , t3]