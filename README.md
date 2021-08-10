# C19VS
A simulation of a database application system for the COVID-19 Public Health Care Vaccination System (C19VS)

## How to run project
Prerequites: have python and node.js installed

### Set up python's virtual environment
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Set up vue cli
```
$ sudo npm install -g @vue/cli
```

### Run backend
```
$ cd backend
$ python manage.py migrate
$ python manage.py runserver
```

### Run frontend
```
$ cd frontend
$ npm install
$ npm run serve
```
Vue server will be listening on http://localhost:8080/
