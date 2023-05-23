# Ticket Management Backend
 
Simple application in Python Django to manage tickets.


## Scope
The application allows user to:
1. Create, Update, Delete, View Employees
2. List of Employees
3. List of Employee Duty Roster
4. List of Tickets


## Tech Stack
1. Python
2. Django
3. Django Rest Framework
4. PostgreSQL
5. Celery
6. Redis


## Installation
1. Clone Repository
```
git clone git@github.com:Vidhya-Rajendran/ticket_mgmt_backend.git
git checkout master
git pull
```
2. Installing project requirements
```
sudo apt update
sudo apt install postgresql
pip install -r requirements.txt
```
3. To run the project
```
python manage.py runserver
```
4. To run Redis
```
sudo systemctl start redis
```
5. To check Redis status
```
sudo systemctl status redis
```
6. To Run Postgresql
```
sudo service postgresql start
```
7. To check postgresql Status
```
sudo service postgresql status
```
8. To view celery worker log
```
celery -A ticket_management worker --loglevel=info
```
