# Trackitt
## Live stock tracker
Live stock tracker webapp built using Django, yahoo_fin, django-channels, celery, celery-beat and redis

This is a Django project that allows you to track the live stock prices of companies using Yahoo_fin API. The project includes functionality to track multiple companies at once and provides real-time updates of the stock prices through WebSockets using Channels. The project uses Celery and Django-celery-beat for task scheduling.


#### Demo of Webapp: 

https://user-images.githubusercontent.com/91488051/229072304-4ec6aedf-2110-4906-9d8d-6b15c2f3bbf9.mp4




## Below instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
   - Python 3.6+
   - Django 3.0+
   - yahoo_fin
   - redis
   - Channels 3.0+
   - Celery 5.0+
   - Django-celery-beat 2.2+


### Clone the repository:

In bash type:
```
git clone https://github.com/HaardPatel5620/Stockify.git
```

## Running this project

To get this project up and running you should start by having Python installed on your computer. 

Chenge the directory to the base directory of project usig

cd Trackitt/


It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

After clonig the project open terminal and run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Apply migrations
```
python manage.py migrate
```

Now you can run the project with this command

```
python manage.py runserver
```
    
In another terminal, start the Celery worker
```
celery -A live_stock_tracker worker -l info
```

After that In another terminal, start the Celery beat scheduler
```
celery -A live_stock_tracker beat -l info
```


## Features

The following features are available in the application:

 - User authentication: user can create an account and login/logout the website
 - Stock selection: select the desired stocks for watch-list
 - Watch list: live stocks watch list table

## Usage

 - Navigate to http://localhost:8000/ in your browser
 - Login/Signup the account
 - Select the Company(s) and click on 'Get live data'
 - The stock prices for the selected companies will be displayed in real-time
