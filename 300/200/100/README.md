# 100 - Setting up The Database Connection

Open a file called ```app.py``` in your ```app``` directory. This file will have code for setting up the database and your Flask routes:

```
$ mkdir app
$ cd app
$ touch app.py
```

This file will connect to an SQLite database called ```database.db```, and have a class called ```Student``` that represents your database students table for storing student information, in addition to your Flask routes. Add the following ```import``` statements at the top of ```app.py```:

```python title="app.py"
#!/usr/bin/env python
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
```
app/app.py

Here, you import the [```os``` module](https://docs.python.org/3/library/os.html), which gives you access to miscellaneous operating system interfaces. You’ll use it to construct a file path for your ```database.db``` database file.

From the ```flask``` package, you then import the necessary helpers you need for your application: the ```Flask``` class to create a Flask application instance, the ```render_template()``` function to render templates, the ```request``` object to handle requests, the ```url_for()``` function to construct URLs for routes, and the ```redirect()``` function for redirecting users. For more information on routes and templates, see [How To Use Templates in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application).

You then import the ```SQLAlchemy``` class from the Flask-SQLAlchemy extension, which gives you access to all the functions and classes from SQLAlchemy, in addition to helpers, and functionality that integrates Flask with SQLAlchemy. You’ll use it to create a database object that connects to your Flask application, allowing you to create and manipulate tables using Python classes, objects, and functions without needing to use the SQL language.

You also import the ```func``` helper from the ```sqlalchemy.sql``` module to access [SQL functions](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#working-with-sql-functions). You’ll need it in your student management system to set a default creation date and time for when a student record is created.

Below the imports, you’ll set up a database file path, instantiate your Flask application, and configure and connect your application with SQLAlchemy. Add the following code:

```python title="app.py"
...
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```
app/app.py

Here, you construct a path for your SQLite database file. You first define a base directory as the current directory. You use the [os.path.abspath()](https://docs.python.org/3.8/library/os.path.html#os.path.abspath) function to get the absolute path of the current file’s directory. The special ```__file__``` variable holds the pathname of the current ```app.py``` file. You store the absolute path of the base directory in a variable called ```basedir```.

You then create a Flask application instance called ```app```, which you use to configure two Flask-SQLAlchemy [configuration keys](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/):

- ```SQLALCHEMY_DATABASE_URI```: The database URI to specify the database you want to establish a connection with. In this case, the URI follows the format ```sqlite:///path/to/database.db```. You use the [os.path.join()](https://docs.python.org/3.8/library/os.path.html#os.path.join) function to intelligently join the base directory you constructed and stored in the ```basedir``` variable, and the ```database.db``` file name. This will connect to a ```database.db``` database file in your ```app``` directory. **The file will be created once you initiate the database**.

- ```SQLALCHEMY_TRACK_MODIFICATIONS```: A configuration to enable or disable tracking modifications of objects. You set it to ```False``` to disable tracking and use less memory. For more, see [the configuration page](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) in the Flask-SQLAlchemy documentation.

> **Note**:
> 
> If you want to use another database engine such as PostgreSQL or MySQL, you’ll need to use the proper URI.
>
> For PostgreSQL, use the following format:
>
> ```postgresql://username:password@host:port/database_name```
>
> For MySQL:
>
> ```mysql://username:password@host:port/database_name```
>
> For more, see the SQLAlchemy documentation for engine configuration.

**OPTIMIZATION**: We move the configuration to a special ```config.py``` file.

Update the ```app.py``` file by adding the reference to a ```config.py``` file:

```
...
# configuration settings from config.py
app = Flask(__name__)
app.config.from_object(config)
...
```
app/app.py

Then add the following to the ```config.py``` file:

```python title="config.py"
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```
app/config.py

After configuring SQLAlchemy by setting a database URI and disabling tracking, you create a database object using the ```SQLAlchemy``` class, passing the application instance to connect your Flask application with SQLAlchemy. You store your database object in a variable called ```db```. You’ll use this ```db``` object to interact with your database.