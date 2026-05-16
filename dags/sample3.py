from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sdk import task
import os
import requests
from airflow.providers.postgres.hooks.postgres import PostgresHook

create_employee = SQLExecuteQueryOperator(
    task_id= "create employee table",
    conn_id="connecting_airlfow_with_postgres_sql",
    sql="""
CREATE TABLE IF NOT EXISTS employees (
            "Serial Number" NUMERIC PRIMARY KEY,
            "Company Name" TEXT,
            "Employee Markme" TEXT,
            "Description" TEXT,
            "Leave" INTEGER
        );""",
)

create_employee_temporay_table = SQLExecuteQueryOperator(
    task_id= "create employee temporary table",
    conn_id="connecting_airlfow_with_postgres_sql",
    sql="""
DROP TABLE IF EXISTS employees_temp;
        CREATE TABLE employees_temp (
            "Serial Number" NUMERIC PRIMARY KEY,
            "Company Name" TEXT,
            "Employee Markme" TEXT,
            "Description" TEXT,
            "Leave" INTEGER,
            "Joke Variable" INTEGER,
        );""",
)