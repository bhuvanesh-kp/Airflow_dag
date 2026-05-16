import pendulum
import random

from airflow.sdk import dag, task

@dag(
    schedule=None,
    start_date=pendulum.datetime(2026, 5, 5),
    catchup=True,
    tags=["sample1"]
)
def example_dag_api():
    
    @task
    def random_number_generator() -> list:
        number_list = []
        for i in range(10):
            number_list.append(random.randint(0, 1000))
        return number_list
    
    @task(multiple_outputs=True)
    def number_evaluator(input: list) -> int:
        total = 0
        for num in input:
            if num % 2  == 0:
                total += num
            else:
                total -= num

        return total
    
    @task
    def print_function(value_obtained:int):
        print(value_obtained)

    

    first = random_number_generator()
    second = number_evaluator(first)
    print_function(second)

example_dag_api()
