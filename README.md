# Job Queue  Implementation using Redis and Celery  

## Files  
Dockerfile - instructions for docker howto build an image  
requirements.txt - list of required python packages  
docker-compose.yaml - instructions for docker to run containers  
task_queue.py - Celery application, main entry point and configuration hub for using Celery  
submit_task.py - demo of prioritization and failed jobs handling in Celery  

## build and run Celery  
```  
docker compose build  
docker compose up  
```

## run demo  
`docker exec celery-worker python /app/submit_task.py`  
, monitoring of Celery task executions should be accessible on Flower's URL http://localhost:5555/  

## refs:  
Dockerfile - https://docs.docker.com/reference/dockerfile/  
docker file - https://docs.docker.com/reference/dockerfile/  
Celery Application - https://docs.celeryq.dev/en/main/userguide/application.html  
Flower - https://flower.readthedocs.io/en/latest/  
How to Implement Priority Queues with Redis Sorted Sets - https://oneuptime.com/blog/post/2026-01-21-redis-priority-queues-sorted-sets/view   
broker_transport_options parameters: https://docs.celeryq.dev/en/latest/userguide/routing.html#:~:text=If%20you%20want%20more%20priority,%2C%20'celery:9'%5D
Routing Tasks(including priorities) - https://docs.celeryq.dev/en/latest/userguide/routing.html#redis-message-priorities  
Celery Tasks - https://docs.celeryq.dev/en/stable/userguide/tasks.html

