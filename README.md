# DealerDashboard
Project Deployment: https://dealerdashboard.netlify.app
- React + Django + PostgreSQL 
- Docker + Microservices + Polling
- Heroku + Netlify
- Celery + Redis

--------

This is a full-stack car dealership management application to streamline and optimize all aspects of dealership operations.\
These are what I (Sarina) did:
- Created PostgreSQL databases with Django, SQL, and migrations for efficient data management and retrieval
- Created REST API endpoints for streamlined data communication between the React frontend and the databases
- Utilized Docker, Microservices, and polling strategies to optimize data synchronization across various services
- Established four CI/CD pipelines for backend and frontend deployment on Heroku and Netlify, incorporating
database migrations, environment variable configuration, and extensive debugging to ensure continuous delivery
- Implemented distributed task processing and scheduling using Celery and Redis for efficient task execution and management during deployment on Heroku

--------

## Diagram of the Project

<img width="800" alt="wireframe" src="https://github.com/wsrn829/wsrn829/assets/67284951/898834b9-20c4-416b-b788-387b2342e9ae">

----------

Brought to you by:

* Alan Y.C. Cheng:
  - Service Microservice Source Code
  - Service Frontend Code
  - Inventory (Monolith) Frontend Code
  - Original README
* Sarina Wu:
  - Sales Microservice Source Code
  - Sales Frontend Code
  - Backend and Frontend Deployment on Heroku and Netlify with Four CI/CD Pipelines and three PostgreSQL Databases
  - Distributed task processing and scheduling using Celery and Redis
  - Styling and layout design using CSS and Bootstrap
  - Wireframe
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




