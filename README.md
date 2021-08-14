# 💉C19VS 
A UI simulation of a database application system for the COVID-19 Public Health Care Vaccination System (C19VS)

## 🎬 Demo
#### 1. Execute SQL queries
![image](https://user-images.githubusercontent.com/60008262/129432526-638f71c9-1b14-4381-92fb-3e1e5e04a85d.png)
#### 2.Display tables
![image](https://user-images.githubusercontent.com/60008262/129432549-f61633f2-ee3b-4577-ac92-b6f099cbfe8c.png)
#### 3. Create new records
![image](https://user-images.githubusercontent.com/60008262/129432595-984c8682-0488-4b80-a37d-502db73a34dc.png)
#### 4. Edit records
![image](https://user-images.githubusercontent.com/60008262/129432564-138093a2-11af-4059-90f4-dcf399c8f0b1.png)
#### 5. Delete records
![image](https://user-images.githubusercontent.com/60008262/129432628-40865ea5-cffc-4d07-8216-0f1ce80b4b2e.png)

![image](https://user-images.githubusercontent.com/60008262/129432641-788590b1-12af-430b-95ca-eb1d1017cf2a.png)



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
