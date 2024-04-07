from celery import Celery
import time
import celeryconfig

app = Celery('tasks')
app.config_from_object(celeryconfig)

@app.task
def process_task(task_id):
    time.sleep(2)
    print(f"Task {task_id} completed")
    return task_id

for i in range(100):
    task_id = f"task_{i}"
    process_task.delay(task_id)
