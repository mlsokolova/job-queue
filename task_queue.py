from celery import Celery
from kombu import Queue
import time

task_queue = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
)

#task_queue.conf.task_queues = (
#    Queue("LOW"),
#    Queue("NORMAL"),
#    Queue("HIGH"),
#)

#task_queue.conf.task_default_queue = "NORMAL"


task_queue.conf.broker_transport_options = {
    'queue_order_strategy': 'priority',
}

task_queue.conf.broker_transport_options = {
    'priority_steps': list(range(3)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}

task_queue.conf.task_create_missing_queues = True

task_queue.conf.worker_prefetch_multiplier = 1
task_acks_late = True

task_queue.conf.task_default_priority = 1
task_queue.conf.task_queue_max_priority = 3

@task_queue.task(queue='celery', priority=0)
def high_priority():
    time.sleep(10)


@task_queue.task(queue='celery', priority=1)
def low_priority():
    time.sleep(10)