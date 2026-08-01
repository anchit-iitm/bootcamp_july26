from app import create_flask_server
from celery import Celery, Task
from celery.schedules import crontab

app = create_flask_server()

class Config():
    broker_url = "redis://localhost:6379/1"
    result_backend = "redis://localhost:6379/2"

init_celery = Celery(app.import_name)

init_celery.config_from_object(Config)

class TaskContext(Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

init_celery.Task = TaskContext

init_celery.conf.beat_schedule = {
    "run_hello_task": {
        "task": "jobs.tasks.hello_task",
        "schedule": crontab(day_of_month="1", hour=7, minute=2),
    }
}

import jobs.tasks


