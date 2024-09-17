# 200 - Declaring The Table

With the database connection established and the database object created, you’ll use the database object to create a database table for students, which is represented by a model — a Python class that inherits from a base class Flask-SQLAlchemy provides through the ```db``` database instance you created earlier. To reference your database models, add the following to your ```app.py``` file:

```python title="app.py"
...
# import the database models
from models import Base
```
app/app.py

Next, create a file ```models.py``` in the same directory as ```app.py``` with the following content:

```python title="models.py"
#!/usr/bin/env python
from datetime import datetime
from sqlalchemy import Column, Table, DateTime, Boolean
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
```

To define a student table as a model, we added the Student class to our ```models.py``` file.

MORE