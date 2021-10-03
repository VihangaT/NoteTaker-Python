from datetime import timezone
from enum import unique
from operator import ipow
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id=db.column(db.integer,primary_key=True)
    data=db.column(db.String(100000))
    date=db.column(db.DateTime(timezone=True),default=func.now())

class User(db.Model,UserMixin):
    id =db.column(db.integer,primary_key=True)
    email=db.column(db.String(150),unique=True)
    password=db.column(db.String(150))
    first_name=db/column(db.String(150))