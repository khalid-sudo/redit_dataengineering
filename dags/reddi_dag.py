from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.timetables.trigger import MultipleCronTriggerTimetable #from airflow.timetables.trigger import CronTriggerTimetable the diffrence is that the cron triggerteplate take one cron the multiple takes many


"""
this line will help us avoid the import modules errors casue when running the 
dag it will be looking for modules in the same directory the is in so to avoid 
that we used sys.path.insr to be able to specify the path where he can search for modules 
os.path.dirname(os.path.dirname(os.path.abspath(__file__))) -> /Users/khalid/personal/reditdataengineering
os.path.dirname(os.path.abspath(__file__)) -> /Users/khalid/personal/reditdataengineering/dags
os.path.abspath(__file__) ->  /Users/khalid/personal/reditdataengineering/dags/reddit_dag.py
So the python path will contain PYTHONPATH = /Users/khalid/personal/reditdataengineering
this way we'll avoid the problem of module not found
"""

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

default_args = {
    'owner': 'khalid laksantini',
    'start_date': datetime(2024,1,22)
}


file_postfix = datetime.now().strftime("%Y%m%d")


dag = DAG (
    dag_id = "reddit_etl_pip",
    default_args = default_args,
    schedule = MultipleCronTriggerTimetable("10 1 * * *", "40 2 * * *", timezone="UTC"),  # At 1:10 and 2:40 each day.
    catchup = False,
    tags = ["reddit", "pipeline", "etl"]    
)


# TODO exctract from reddit

# TODO upload to s3