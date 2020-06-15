# Library Management System

#### Load initial data

Load initial data for the LibraryBranch model:

```bash
$ python manage.py loaddata library_branches.json --app lms --format json
```

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
