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