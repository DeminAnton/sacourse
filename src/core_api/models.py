import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime
from core_api.database import metadata

user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(50)),
                   Column('email', String(50), unique=True),
                   Column('created_at', DateTime, default=datetime.datetime.now(datetime.UTC)) 
                   )
