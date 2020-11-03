# Implement notification features 

Allowing users to subscribe to a notification about choosed by them specific sport event via a simple form.


## How does it work?

Users can subscribe to notifications in two ways:
* via Email
* via Webhook

They can also choose 3 frequencies for sending notifications:
* Weekly
* Daily
* Live

For simplicity, users can view 3 types of events and filter them:
* Future - have not yet taken place
* Ongoing - now they are going on
* Past - they have already taken place

## How to do it?

1. Go to the application: 
2. Register your account (without an account you will not be able to sign up to notify and view all teams - guests can only watch events)
3. If you are logged in you can move from homepage to notifications (and register the choosen one) or go to check future, past or ongoing events (you can see the results of the matches played LIVE!))

# Usage
### Installation

Create a virtual environment to install dependencies in and activate it:

    $ virtualenv
    $ source env/bin/activate

Then install the dependencies:

    (env)$ pip install -r requirements.txt

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.
Once pip has finished downloading the dependencies:

    (env)$ cd sport_events

### Database
Change the default DATABASES in setting.py:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Schema name in DataBase',
        'USER':'root',
        'PASSWORD':'Database password',
        'HOST':'127.0.0.1',
        'PORT':'3306'
        }
    }

Migrate database structure

    (env)$ python manage.py migrate
    
### Start Django
    
    (env)$ python manage.py runserver
    
And navigate to `http://127.0.0.1:8000`

### Cron management
Activate crons - you can find all of them in the CRONTAB section in settings.py - 
after activating crons, all users will receive notifications of their choice in a timely manner

Add all crons from settings.py:

    python manage.py crontab add

Check them:

    python manage.py crontab show
    
Remove them:

    python manage.py crontab remove
    
For details check [documentation](https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/).

## API
API [documentation](https://app.swaggerhub.com/apis/hubert-hernoga/Notificator/1.0.0)
## Features

* Creating your own account
* Login panel
* Password change
* Logout
* Filtering tables with teams and events for whatever value we want using one simple form
* Break down events into future, ongoing and past
* Only upcoming events can be selected when setting notifications
* You can choose a notification depending on the receiver - Email / Webhook
* You can choose a notification depending on the frequency - Weekly / Daily / Live
* After successfully saving the notification, we get a confirmation email (only when selecting the notification by email)

## Main libraries used
* Crispy forms - is an application that helps to manage Django forms,
* Crontab - running crons in the background at the required frequency,
* Sengrid - sending e-mail notifications and confirmations,
* reguests - allow to send HTTP/1.1 requests using Python
* mysqlclient - is a fork of MySQLdb that supports Python with mysql integration