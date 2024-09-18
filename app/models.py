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