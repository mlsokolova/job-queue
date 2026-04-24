from task_queue import retry_test, sleep, Priority
import time


# Priority
for i in range(5):
   sleep.apply_async(queue='celery', priority=Priority.HIGH, task_id=f'sleep_high_{i}')
   sleep.apply_async(queue='celery', priority=Priority.NORMAL, task_id=f'sleep_normal_{i}')
   sleep.apply_async(queue='celery', priority=Priority.LOW, task_id=f'sleep_low_{i}')

# Expotential backoff retry
retry_test.apply_async()

