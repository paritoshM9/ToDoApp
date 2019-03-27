# ToDoApp

A simple ToDo webapp written in Django with Postgresql database. 

Screenshot:

![](G:\python\ToDoApp\screenshot.png)



Functionalities include:

i) Adding tasks <br/>
ii) Deleting Tasks <br/>
iii) Editing already added tasks <br/>
iv) Marking the tasks which are completed <br/>

Instructions for setting up the database:

i) Go to https://www.elephantsql.com/plans.html and select a 'tinyTurtle' free database.<br/>
ii) Open settings.py file from ToDo/todo_project/todo_project directory <br/>
iii) Find a dictionary named DATABASES and modify the credentials according to your instance details on elephantsql <br/>

In 'NAME' and 'USER', paste the value from 'User & Default database' section in elephantsql <br/>
Similarly, fill the value of 'PASSWORD' and 'HOST' ('SERVER' in elephantsql) <br/>

iv) In command prompt run the following command <br/>

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

v) Finally, go to 127.0.0.1/todo 

