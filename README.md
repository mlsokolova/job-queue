# Celery tasks prioritization  
build and run:  
```  
docker compose build  
docker compose up  
```
run Celery jobs:  
`docker exec celery-worker python /app/submit_task.py`  

refs:  
https://docs.celeryq.dev/en/main/reference/celery.states.html  
https://hub.docker.com/_/redis  
https://hub.docker.com/_/celery  
https://oneuptime.com/blog/post/2026-01-21-redis-priority-queues-sorted-sets/view  
http://localhost:5555/  
broker_transport_options parameters: https://docs.celeryq.dev/en/latest/userguide/routing.  html#:~:text=If%20you%20want%20more%20priority,%2C%20'celery:9'%5D
https://docs.celeryq.dev/en/latest/userguide/routing.html#redis-message-priorities  
https://docs.celeryq.dev/en/stable/userguide/tasks.html
https://flower.readthedocs.io/en/latest/prometheus-integration.html
