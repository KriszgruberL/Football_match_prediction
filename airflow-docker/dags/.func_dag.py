

# from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator

# from utils.testairflow import func_test



# default_args = { 
#                    "owner" : "lukiwa",
#                    "start_date": datetime(2024, 9, 9),
#                    "retries" : 1
# }

# with DAG(
#     "func_dag",
#     default_args = default_args,
#     schedule = "@once",
#     catchup = False,
#     tags = ["test"]) as dag :
    
#     run_this = PythonOperator(
#     task_id = "run_this",
#     python_callable = func_test,
# ) 
    

    
