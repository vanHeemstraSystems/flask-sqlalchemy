# 100 - Setting up The Database Connection

Open a file called ```app.py``` in your ```app``` directory. This file will have code for setting up the database and your Flask routes:

```
$ mkdir app
$ cd app
$ touch app.py
```

This file will connect to an SQLite database called ```database.db```, and have a class called ```Student``` that represents your database students table for storing student information, in addition to your Flask routes. Add the following ```import``` statements at the top of ```app.py```:

```
#!/usr/bin/env python
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
```
app/app.py


MORE