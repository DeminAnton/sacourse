import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean
from core_api.database import metadata

user_table = Table('users', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(50)),
                   Column('email', String(50), unique=True),
                   Column('created_at', DateTime, default=datetime.datetime.now(datetime.UTC)) 
                   )

task_table = Table('tasks', metadata,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('name', String(30)),
                   Column('user_id', Integer),
                   Column('category', String(30)),
                   Column('status', Boolean, unique=False, default=True) 
                   )

time_track = Table('time_track', metadata,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('task_id', Integer),
                   Column('start', DateTime, default=datetime.datetime.now(datetime.UTC)),
                   Column('end', DateTime, default=None)
                   )

