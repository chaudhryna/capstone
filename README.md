# Capstone Project for CS50 Web

## Overview

The project I created is a Help Desk ticketing system for a small office.  The program allows a user to submit a simple trouble ticket that the IT Support staff receives.  The project is built with Django 4.2, Python 3.11, Bootstrap 5.3, Fontawesome, Crispy-forms, Pillow, Cropper.js, Chart.js, and Postgres SQL 15.  

I built this project because of my experience as a system admin in various companies and organizations.  We would always have different ticketing systems but they were usually so complicated that our customers wouldn't bother to fill them out so we had to fill the tickets out and then work them so that the managers could justify the expense.   

To take care of this I made the ticket super simple to fill out and had a field that the tech could leave notes on any issue that came up in case the ticket needed to be escalated or worked by another tech. 

## Distinctiveness and Complexity

### Why it's Distinctive and Complex

The other Django projects that we've built in this course have a project that contained one app.  I built a project called "Capstone" and three apps called "Accounts", "Tickets", and "Helpdesk".  I broke the project into 3 apps so that individual apps could be reused and new apps added as needed. [This is a feature mentioned in the Django official docs.](https://docs.djangoproject.com/en/4.2/ref/applications/)  

I also used the Group model to apply permissions to the IT Staff so that certain views and database permissions were restricted to the staff only.  I created the group in the Django admin area where I also added the users, but then I created a "decorators.py" file in the Helpdesk app to check if the user was in the group so that I could use the decorator in views to restrict access to the IT team.

### What's Contained in Each File that I Created

#### Top Level
At the top level (where the manage.py resides) I created a "templates" folder for the templates that didn't belong to a particular app such as the "base.html" that will be extended to all the rest of the templates and the "partials" folder. In order to keep to the DRY principle (Don't Repeat Yourself) I used partials as much as possible and included them in various templates.

The "partials" folder contains:
- "_messages.html" To insert success and error message in each template.
- "_navbar.html" To insert the navbar in the base template.
- "_profile-modal.html" To insert the model in the profile template that will allow the user to modify some of their profile fields and change their picture.
- "_ticket_detail.html" This opens up a modal to show the ticket details.
- "_tickets.html" A listing of tickets.  This is used in the Dashboard and in the Profile view to load all the tickets that a user has submitted.  

The top level also contains a requirements.txt file that lists all of the programs that were installed with pip.  Some of them may be leftover from different things I tried but I left them in because I wasn't sure what file was dependant on another file.  

The files that I installed that need to be there are:
- django-crispy-forms==2.0. Used to make the forms look nicer.
- [django-environ==0.10.0](https://django-environ.readthedocs.io/en/latest/) Used to create environment variables in a .env file. 
- [Pillow==10.0.0](https://pypi.org/project/Pillow/) A Python imaging library 
- [psycopg==3.1.10](https://www.psycopg.org/psycopg3/docs/basic/install.html) Both psycopy and psycopy-binary are needed for connecting to PostgreSQL 
- psycopg-binary==3.1.10 
- [whitenoise==6.5.0](https://whitenoise.readthedocs.io/en/latest/) This is used to simplify static file serving. 

In addition to these files at the top layer there is a .gitignore file and the "venv" folder for the virtual environment.  The media, .env, and venv files are not uploaded to github.

There is a media folder with a default profile image called "default.jpg" and a subfolder under the media folder for the user uploaded images called "profile_pics". This will need to be recreated if the project is downloaded.

There is a static folder with 4 subfolders that will also need to be recreated.  The static subfolders are:

- css: That contains css files for Fontawesome, Bootstrap 5 minified and Bootstrap 5 map, and finally a local styles.css file.
- img: Containing the favicon.ico for the browser tab, the helpdesk.jpg file used in various forms, and the logo.png used in the navbar.
- js: Containing a cropperjs subfolder with all the files for cropperjs. The js folder also contains the bootstrap bundle minified js file as well as the bootstrap bundle map.  The final file in the js folder is called "main.js" and contains the JavaScript that I used to customize the Chart.js and Cropper.js that I used in the program.
- webfonts: This is a folder with all the free Fontawesome icons.

#### Project level
All the files in the Capstone project level were already there with the exception of the .env file.  I moved the setting for Debug, the Django secret key and all the database settings to this file and configured the environment setting in the Capstone settings file.  This file will not be uploaded to Github but will need to be recreated if the project is downloaded.

The project urls.py file contains the default admin path as well as an include path to each of the apps.  I included the path to the dashboard from the accounts app so that it could be used at the project level.  In addition I added:
```
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
so that the media files could be used in development. 

#### Accounts App
The accounts app is where all the user account logic is handled (i.e. login, logout, registration, dashboard, and profile display and update). I added the urls.py file to handle these paths.  

Accounts has a User model based on Abstract User, a Profile model with a "OneToOne" relationship to the User model and a Department model.  I ended up not using the Department but I left it in for use later.  

There is a forms.py file to update the profile and a signals.py file to create and save the profile when the user is created. 

There is a templates folder with the following templates:
- dashboard.html
- login.html
- profile.html
- register.html

#### Tickets App
This app handles the logic of creating, updating, deleting, and reading tickets.  The urls.py file handles all the routes for these database functions. 

There are two models in the app: Ticket and TechNotes.  The views.py file contains the logic to create and update the ticket as well as show the ticket detail. The update_ticket logic calls a decorator.py file from the helpdesk app to limit the access of this view to the IT Support team.

The templates folder within the app contains:
- create_ticket.html
- update_ticket.html 

#### Helpdesk App
This app contains the logic for the IT Dashboard (limited to the IT Support group) and the logic for feeding data from the Ticket model to the main.js file that's used to create the two charts that are displayed on the IT Dashboard (using Chart.js).  

The views.py file also has the logic to display two Bootstrap accordian files that display all the tickets assigned to the tech that's logged in and all the tickets that are contained in the database.  The tech may have to add notes to someone else's ticket so they need to be able to see all the tickets.  

The urls.py file contains the path to the dashboard and the path to the chart data for both charts.  

The template folder contains only the it_dashboard.html template. 

There is also a decorators.py file that imports a "user_passes_test" decorator for checking if the logged in user is in the IT Support group.  If true then they will be able to see the IT Dashboard and they will be able to update tickets. 

### How to Run the Program Locally
  
The user can download the code from [github.com](https://github.com/chaudhryna/capstone).  Then they will need to:
```[tasklist]
### My tasks
- [ ] setup a virtual environment
- [ ] run the virtual environment
- [ ] install files from the requirements.txt file including django 
- [ ] setup a Postgres database (with a name of their choice)
- [ ] create a .env file in the capstone folder with their own values for:

    - DEBUG (True if in development and False if in production)
    - SECRET_KEY (The django secret key that's created when they install django)
    - DB_NAME (What they set their database name to)
    - DB_USER (Which account can run the database)
    - DB_PASSWORD (The password that account uses to login)
    - DB_HOST (if in development this will be localhost)
    - DB_PORT (if in development and localhost this is usually 5432 for Postgres)

- [ ] setup a superuser account to access the admin area of the project 
```

That should be everything.

