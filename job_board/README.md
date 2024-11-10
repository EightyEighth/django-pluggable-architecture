[//]: # (Write documatation for the job board)

[//]: # (how to run the job board)


## Job Board Example

This is a simple example of pluggable application that can be used to create a job board. The job board is a Django application that can be used to post job listings and apply for jobs. The job board is a pluggable application that can be easily integrated into any Django project.


## Installation

1. Git clone the repository
2. Install the requirements
```bash 
pip install -r requirements.txt 
pip install -e apps/users apps/jobs apps/companies
```
3. Run the migrations
```bash
python manage.py migrate
```
4. Run the server
```bash
python manage.py runserver
```

## Usage
Open the browser and go to the following URL:
```
http://localhost:8000/job_board/
```
