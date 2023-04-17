import requests
import time
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
# from airflow.operators.python import BranchPythonOperator
# from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta





def get_data(**kwrgs):
    API_key = 'IC06NDYISZLLRPU3'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey='+API_key
    r = requests.get(url)

    try:
        data = r.json()
        path = 'mnt/c/Users/riccardo/Desktop/corso_programmazione/DATA_CENTER/DATA_LAKE'
        with open(path + str(time.time()), 'w') as outfile:
            json.dump(data, outfile)
    except:
        pass


default_dag_args = {
    'start_date': datetime(2022, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False, 
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
    }

with DAG("market_data_alphavantage_dag", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:

    task_0 = PythonOperator(task_id = "get_market_data", python_callable = get_data, op_kwargs = {'tickers' : []})

    task_0