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
from sqlalchemy.sql import func

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer(), primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now())
    bio = Column(Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
```

To define a student table as a model, we added the Student class to our ```models.py``` file.

Here, you created a ```Student``` model, which inherits from the ```Base``` class. This represents the student table. You use the [Column](https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column) class to define columns for your table. The first argument represents the column type, and additional arguments represent column configuration.

You define the following columns for the ```Student``` model:

- **id**: The student ID. You define it as an integer with ```Integer```. ```primary_key=True``` defines this column as a *primary key*, which will assign it a unique value by the database for each entry (that is a student).
- **firstname**: The student’s first name. A string with a maximum length of ```100``` characters. ```nullable=False``` signifies that this column should not be empty.
- **lastname**: The student’s last name. A string with a maximum length of ```100``` characters. ```nullable=False``` signifies that this column should not be empty.
- **email**: The student’s email. A string with a maximum length of ```80``` characters. ```unique=True``` signifies that each email should be unique for each student. ```nullable=False``` signifies that this column should not be empty.
- **age**: The student’s age.
- **created_at**: The time the student record was created at in the database. You use [DateTime](https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.DateTime) to define it as a Python [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) object. ```timezone=True``` enables timezone support. [server_default](https://docs.sqlalchemy.org/en/14/core/defaults.html#server-invoked-ddl-explicit-default-expressions) sets the default value in the database when creating the table, so that default values are handled by the database rather than the model. You pass it the [func.now()](https://docs.sqlalchemy.org/en/14/core/functions.html#sqlalchemy.sql.functions.now) function which calls the ```SQL now()``` datetime function. In SQLite, it is rendered as ```CURRENT_TIMESTAMP``` when creating the student table.
- **bio**: The student’s bio. ```Text()``` indicates the column holds long texts.

See the [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/core/type_basics.html) for column types other than the types you used in the preceding code block.

The special [__repr__](https://docs.python.org/3/reference/datamodel.html#object.__repr__) function allows you to give each object a string representation to recognize it for debugging purposes. In this case you use the student’s first name.