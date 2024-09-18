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
>>> from app import db, Student
>>> student_john = Student(firstname='john', lastname='doe',
>>>                        email='jd@example.com', age=23,
>>>                        bio='Biology student')
```

The ```student_john``` object represents a student that will be added to the database, but this object has not been written to the database yet. Check out the object in the flask shell to see its representation string you constructed with the ```__repr__()``` method:

```
>>> student_john
```

You'll receive the following output:

```
<Student john>
```

Remember that you set ```firstname``` as the reference earlier on, here ```john```.

You can get the value of columns using the class attributes you defined in the ```Student``` model:

```
>>> student_john.firstname
```

Output:

```
'john'
```

```
>>> student_john.bio
```

Output:

```
'Biology student'
```

Because this student has not been added to the database yet, its ID will be ```None```:

```
>>> print(student_john.id)
```

Output:

```
None
```

To add this student to the database, you’ll first need to add it to a *database session*, which manages a database transaction. Flask-SQLAlchemy provides the ```db.session``` object through which you can manage your database changes. Add the ```student_john``` object to the session using the ```db.session.add()``` method to prepare it to be written to the database:

```
>>> db.session.add(student_john)
```

This will issue an ```INSERT``` statement, but you won’t get an ID back because the database transaction is still not committed. To commit the transaction and apply the change to database, use the ```db.session.commit()``` method:

```
>>> db.session.commit()
```

Now that student John is added to the database, you can get its ID:

```
>>> print(student_john.id)
```

Output:

```
1
```

You can also use the ```db.session.add()``` method to edit an item in the database. For example, you can modify the student’s email like so:

```
>>> student_john.email = 'john_doe@example.com'
>>> db.session.add(student_john)
>>> db.session.commit()
```

Use the Flask shell to add a few more students to your database:

```
>>> student_sammy = Student(firstname='sammy', lastname='shark', email='sammy_shark@example.com', age=20, bio='Marine biology student')
>>> student_carl = Student(firstname='carl', lastname='white', email='carl_white@example.com', age=22, bio='Marine geology student')
>>> db.session.add(student-sammy)
>>> db.session.add(student_carl)
>>> db.session.commit()
```

Now, you can query all the records in the student table using the ```query``` attribute with the ```all()``` method:

```
>>> Student.query.all()
```

You’ll receive the following output:

```
[<Student john>, <Student sammy>, <Student carl>]
```

At this point, you have three students in your database. Next, you’ll create a Flask route for the index page and display all of the students in your database on it.