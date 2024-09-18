# 300 - Creating the Database

Now that you’ve set the database connection and the student model, you’ll use the Flask shell to create your database and your student table based on the ```Student``` model.

With your virtual environment activated, 

```
$ cd app
$ . .venv/bin/activate
```

set the ```app.py``` file as your Flask application using the ```FLASK_APP``` environment variable. Then open the Flask shell using the following command in your ```flask_app``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy/app (main) $ export FLASK_APP=app
(.venv) gitpod /workspace/flask-sqlalchemy/app (main) $ flask shell
```

You will be prompted as below:

```sql
Python 3.12.6 (main, Sep  9 2024, 10:33:54) [GCC 11.4.0] on linux
App: app
Instance: /workspace/flask-sqlalchemy/app/instance
>>> 
```

A Python interactive shell will be opened. This special shell runs commands in the context of your Flask application, so that the Flask-SQLAlchemy functions you’ll call are connected to your application.

Import the database object and the student model, and then run the db.create_all() function to create the tables that are associated with your models. In this case you only have one model, which means that the function call will only create one table in your database:

```sql
>>> from app import db
>>> from models import Student
>>> db.create_all()
```

Leave the shell running, open another terminal window and navigate to your ```app``` directory. You will now see a new file called ```database.db``` in the ```app/instance``` directory.

**Note**: The ```db.create_all()``` function does **not** recreate or update a table if it already exists. For example, if you modify your model by adding a new column, and run the ```db.create_all()``` function, the change you make to the model will **not** be applied to the table if the table already exists in the database. The solution is to delete all existing database tables with the ```db.drop_all()``` function and then recreate them with the ```db.create_all()``` function like so:

```
>>> db.drop_all()
>>> db.create_all()
```

This will apply the modifications you make to your models, but **will also delete all the existing data in the database**. To update the database and preserve existing data, you’ll need to use [schema migration](https://en.wikipedia.org/wiki/Schema_migration), which allows you to modify your tables and preserve data. You can use the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html) extension to perform SQLAlchemy schema migrations through the Flask command-line interface.

If you receive an error, make sure your database URI and your model declaration are correct.