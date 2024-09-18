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

MORE