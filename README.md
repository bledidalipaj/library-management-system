# Library Management System

This is my attempt to recreate (using Django) the library management system built by Wes Doyle. You can view
the code for the original application [here](https://github.com/wesdoyle/library-management-system).

The two applications are now exactly the same, because I have made some minor modifications and
additions.

#### Developement setup

Steps to locally setup development project.

##### Prerequisites

Ensure that you have Python 3.8 installed on your machine. You can check by running,

```bash
$ python --version
```

You will also need [Pipenv](https://github.com/pypa/pipenv) in order to install the necessary packages.

##### Installation

```bash
$ git clone https://github.com/bledidalipaj/library-management-system.git
$ cd library-management-system
$ pipenv install
```

The applicatation needs to read enviroment variables to run properly. To set those variables locally,
copy the .env.sample file as .env

```bash
$ cp .env.sample .env
```

Apply Django database migrations locally.

```bash
$ python manage.py migrate
```

Create a local superuser account.

```bash
$ python manage.py createsuperuser
```

Start the local webserver.

```bash
$ python manage.py startserver
```

You can stop the webserver by pressing Control + C

##### Set up email

In order for the application to work you will need to configure an email, which the application will use
to send the necessary notifications.

You can do that by setting the following environment variables in the .env file:

EMAIL_BACKEND=...
EMAIL_HOST=...
EMAIL_USE_TLS=...
EMAIL_PORT=...
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...

I write below an example of using gmail as an email service:

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=youremail
EMAIL_HOST_PASSWORD=yourpassword

If you do not want to configure the email, then you must set the following variable in the .env file and
ignore the other ones:

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

#### Load initial data

After the initial setup the application has no data. If you want you manually add data through the admin or
you can execute the following commands that will add some initial data for you:

1. Load initial data for the Author model:

```bash
$ python manage.py loaddata authors.json --app lms --format json
```

2. Load initial data for Status model:

```bash
$ python manage.py loaddata status.json --app lms --format json
```

3. Load initial data for LibraryBranch model:

```bash
$ python manage.py loaddata library_branches.json --app lms --format json
```

4. Load initial data for Book model

```bash
$ python manage.py loaddata books.json --app lms --format json
```

5. Load initial data for Patorn model:

```bash
$ python manage.py loaddata patrons.json --app lms --format json
```

#### Export data

Export Patron model data to patron.json

```bash
$ python manage.py dumpdata lms.patron --indent 4 --output lms/fixtures/patrons.json
```

#### Person information

Persons' information were generated using this website https://www.fakenamegenerator.com/gen-random-us-us.php

#### Design Inspiration

- https://dribbble.com/shots/8583284-Profile/attachments/846813?mode=media

#### Libraries Used

- Date Picker [flatpickr v4](https://flatpickr.js.org/)
