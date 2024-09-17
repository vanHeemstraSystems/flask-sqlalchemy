#!/usr/bin/env python
import os

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration settings from config.py
app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)