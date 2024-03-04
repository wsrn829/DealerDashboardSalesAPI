# DealerDashboard(SalesAPI) - Microservice
This is a full-stack car dealership management application to streamline and optimize all aspects of dealership operations.

### Project Deployment: https://dealerdashboard.netlify.app

- (Docker + Microservices) + (Polling + Celery + Redis)
- Heroku + Netlify
- Django + PostgreSQL + React 

--------

### These are what I (Sarina) did:

- Created PostgreSQL databases with Django, SQL, and migrations for efficient data management and retrieval
- Created REST API endpoints for streamlined data communication between the React frontend and the databases
- Utilized Docker, Microservices, and polling strategies to optimize data synchronization across various services
- Established four CI/CD pipelines for backend and frontend deployment on Heroku and Netlify, incorporating
database migrations, environment variable configuration, and extensive debugging to ensure continuous delivery
- Implemented distributed task processing and scheduling using Celery and Redis for efficient task execution and management during deployment on Heroku

--------

### The following is how I (Sarina) set up a distributed task system using Celery and Redis:   

During the deployment of DealerDashboard, I encountered a problem with data synchronization between the Inventory and Sales Microservices. Despite successfully deploying the three Microservices (Inventory, Service, Sales) on Heroku separately, along with three PostgreSQL databases, the Sales Microservice was not polling Automobile VIN from the Inventory Microservice. Consequently, the SalesForm could not create new Sale records.

After troubleshooting, I found that the issue stemmed from the polling function not functioning correctly after the deployment of Microservices and PostgreSQL databases on Heroku. I solved this problem by implementing a distributed task system using Celery and Redis.

Implementation Steps in Detail:

1. Install Celery with pip: `pip install celery`

2. Configure Celery in the Django settings.py file:
```
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```
3. Create a Celery instance: In the Django project root (where manage.py is located), create a new file celery.py:
```
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from sales_project import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales_project.settings')
app = Celery('sales_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

import poll.poller
app.autodiscover_tasks()
```
4. Import the Celery instance: In the Django project's __init__.py file, add the following lines to import the Celery instance:
```
from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

__all__ = ('celery_app',)
```
5. Create a Celery task: Convert the polling function into a Celery task by adding the @app.task decorator:
```
import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_project.settings")
django.setup()

from sales_rest.models import AutomobileVO
from sales_project.celery import app

def get_automobiles():
    response = requests.get("https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com/automobiles/")
    content = json.loads(response.content)
    print(AutomobileVO.objects.all)
    print("POLLER_CONTENT", content)
    for automobile in content["autos"]:
        AutomobileVO.objects.update_or_create(
            vin=automobile["vin"], 
            defaults={
                "vin": automobile["vin"],
                "color": automobile["color"],
                "year": automobile["year"],
                "sold": automobile["sold"]
            },
        )

@app.task
def poll(repeat=True):
    while True:
        print('Before get_automobiles()')
        try:
            get_automobiles()
            print('After get_automobiles()')
        except Exception as e:
            print(e, file=sys.stderr)
        if not repeat:
            break

        time.sleep(60)
        
if __name__ == "__main__":
    poll()
```
6. Schedule the task: Use Celery's periodic task feature to run the polling task every 60 seconds. In the Django settings.py file, add:
```
from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    'poll-every-60-seconds': {
        'task': 'poll.poller.poll',
        'schedule': timedelta(seconds=60),
    },
}
```
7. Install Redis: Celery requires a message broker to handle requests. On Heroku, I used the Heroku Redis add-on. I installed it and set the REDIS_URL config var.

8. Add a worker dyno: In Procfile, add a line for the worker dyno that will run the Celery worker process:
```
worker: celery -A sales_project worker --loglevel=info
```
9. Add a beat dyno: In Procfile, add a line for the beat dyno that will run the Celery beat process:
```
beat: celery -A sales_project beat --loglevel=info
```
10. Deploy to Heroku: Push these changes to Heroku. Heroku should start the worker and beat dynos automatically.

11. Summary:
- The reason why the previous poller might not have been working after deployment on Heroku could be due to how Heroku manages its dynos. Heroku dynos are ephemeral, which means they can restart or move at any time. This can interrupt long-running processes like a polling function.
- Celery and Redis are used to handle these types of background tasks in a more robust way. Celery is a task queue that can distribute work across threads or machines. Redis is used as the message broker for Celery, storing the tasks until they can be processed.
- When we use Celery and Redis, the polling function becomes a task that is managed by Celery. Even if the Heroku dyno restarts or moves, the task remains in the Redis queue and can be picked up by a Celery worker when it's available. This ensures that the polling function continues to run as expected.
- While Celery and Redis are often used in production environments due to their robustness and scalability, they can also be used in development environments. They are not strictly for production only. However, they do add complexity to your application, so they are typically used when the benefits (like improved robustness and scalability) outweigh the added complexity.

-----------

## Diagram of the Project

<img width="800" alt="wireframe" src="https://github.com/wsrn829/wsrn829/assets/67284951/898834b9-20c4-416b-b788-387b2342e9ae">

----------

Brought to you by:

* Alan Y.C. Cheng:
  - Service Microservice Source Code
  - Service Frontend Code
  - Inventory Frontend Code
  - Original README
* Sarina Wu:
  - Sales Microservice Source Code
  - Sales Frontend Code
  - Backend and frontend deployment on Heroku and Netlify with four CI/CD Pipelines and three PostgreSQL Databases
  - Distributed task processing and scheduling using Celery and Redis
  - Wireframe and Diagram
  - Styling and layout design using CSS and Bootstrap
  - Updated README

---------

Step-by-step Instructions to Run the Project

1. Open Terminal on your computer

2. Go to the folder where you want to save this program (replace the path with the path to your folder destination):

```
cd {path to your folder}
```

3. Run the following command in your Terminal to download the code of this program to your computer via the "Clone with HTTPS" method:

```
git clone https://github.com/wsrn829/DealerDashboard.git
```

4. Dive into the newly downloaded program folder:

```
cd DealerDashboard
```

5. Create a new database (Docker Volume) with the name "beta-data" in your local computer for this program to store data in:

```
docker volume create beta-data
```

6. Create the blueprints (Docker Images) for the program:

```
docker-compose build
```

7. Create the isolated environments (Docker Containers) for the program:

```
docker-compose up
```

8. The program is now running, please go to the following link to visit the front end in your browser:

http://localhost:3000

9. Enjoy the program.




## Explicitly defined URLs and ports for each of the services

Program Front End: http://localhost:3000/

Inventory (Monolith): http://localhost:8100/

Service Microservice: http://localhost:8080/

Sales Microservice: http://localhost:8090/




