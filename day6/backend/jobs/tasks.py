from jobs.worker import init_celery
import time

@init_celery.task
def hello_task():
    time.sleep(5)
    return "Hello, World!"

@init_celery.task
def db_query_task():
    from models import data
    all_data = data.query.all()
    rows = [{"id": row.id, "name": row.name} for row in all_data]
    return {
        "data": rows,
        "message": "data retrieved successfully"
        }