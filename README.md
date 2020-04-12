# Library Management System


#### Load initial data

Load initial data for the LibraryBranch model:

```bash
$ python manage.py loaddata library_branches.json --app lms --format json
```

Export Patron model data to patron.json

```bash
$ python manage.py dumpdata lms.patron --indent 4 --output patron.json
```