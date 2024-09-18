#!/usr/bin/env python
import os
import datetime, time

from sqlalchemy import create_engine, select, update, func
from sqlalchemy.sql import func
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import config, socket

# configuration settings from config.py
app = Flask(__name__)
app.config.from_object(config)

# define a database
db = SQLAlchemy(app)

# models
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'

# routes

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)