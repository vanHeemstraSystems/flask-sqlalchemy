# 400 - Populating the Table

After creating the database and student table, you’ll use the flask shell to add some students to your database through the ```Student``` model.

Use the same flask shell you opened earlier, or open a new one with your virtual environment activated in your ```app``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy/app (main) $ export FLASK_APP=app
(.venv) gitpod /workspace/flask-sqlalchemy/app (main) $ flask shell
```

You will be prompted as below:

```
Python 3.12.6 (main, Sep  9 2024, 10:33:54) [GCC 11.4.0] on linux
App: app
Instance: /workspace/flask-sqlalchemy/app/instance
>>> 
```

To add a student to your database, you’ll import the database object and the ```Student``` model, and create an instance of the ```Student``` model, passing it student data through keyword arguments as follows:

```
>>> from app import db
>>> from models import Student
>>> student_john = Student(firstname='john', lastname='doe',
>>>                        email='jd@example.com', age=23,
>>>                        bio='Biologu student')
```

MORE