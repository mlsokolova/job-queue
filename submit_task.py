from task_queue import retry_test, sleep, Priority
import time


# Priority
for i in range(5):
   sleep.apply_async(queue='HIGH', priority=Priority.HIGH, task_id=f'HIGH_train_sentiment_model_mock{i}')
   sleep.apply_async(queue='NORMAL', task_id=f'NORMAL_critical_fraud_model_mock{i}')
   sleep.apply_async(priority=Priority.LOW, task_id=f'LOW_routine_rerank_model_mock{i}')

# Expotential backoff retry
retry_test.apply_async(priority=Priority.NORMAL,
                       retry_kwargs={'max_retries': 9, 'countdown': 5},
                       retry_backoff_max=600,
                       retry_backoff=True
                       )

