#!/usr/bin/env python
import os

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import config, socket

basedir = os.path.abspath(os.path.dirname(__file__))

# import the database models
from models import Base

# configuration settings from config.py
app = Flask(__name__)
app.config.from_object(config)

# define a database
db = SQLAlchemy(app)

# associate the models with the database
db.Model = Base