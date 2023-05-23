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
pip install --upgrade pip
pip install --upgrade setuptools
sudo apt-get install libpq-dev
sudo apt-get install redis-server
pip install -r requirements.txt

3. To run Redis
```
sudo systemctl start redis
```
4. To check Redis status
```
sudo systemctl status redis
```
5. To Run Postgresql
```
sudo service postgresql start
```
6. To check postgresql Status
```
sudo service postgresql status
```
7. To view celery worker log
```
celery -A ticket_management worker --loglevel=info
```
```
8. To migrate 
```
python3 manage.py migrate
```
9. To create super user
```
python3 manage.py createsuperuser
enter user name, enter mail id, enter password (login with this credentials to access django admin)
```
10. To run the project
```
python3 manage.py runserver
```
