from celery import Celery
from kombu import Queue
import time
from enum import IntEnum

class Priority(IntEnum):
    """
    Priority levels for tasks.
    Celery and Redis supports priority range from 0 to 9
    Lower value corresponds higher priority level
    """

    LOW = 9
    NORMAL = 4
    HIGH = 0


task_queue = Celery(
    "task_queue",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
)

#A dict of additional options passed to the underlying transport(Redis in our case)
task_queue.conf.broker_transport_options = { 
    'priority_steps': list(range(9)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}

#workers’ default prefetch count
task_queue.conf.worker_prefetch_multiplier = 1 

# Late ack means the task messages will be acknowledged after the task has been executed, not right before (the default behavior).
task_acks_late = True 

# default task priority
task_queue.conf.task_default_priority = Priority.NORMAL 

# default queue priority
task_queue.conf.task_queue_max_priority = 9 

@task_queue.task(queue='celery', priority=Priority.LOW)
def sleep():
    time.sleep(5)    

@task_queue.task(bind=True,
                 autoretry_for=(ValueError,),
                 )
def retry_test(self):
    print(f"Exacuting task id {self.request.id}")
    print(f"retry count {self.request.retries}")
    if self.request.retries < 8:
        raise ValueError
      