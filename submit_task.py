from task_queue import high_priority, low_priority
import time

for i in range(7):
    high_priority.apply_async()
    low_priority.apply_async()
