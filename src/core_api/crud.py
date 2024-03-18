from core_api.models import task_table, user_table, time_track
from sqlalchemy import select, update
import datetime
from core_api.database import sync_engine

def insert_user(name: str, email:str, creation_time: datetime.datetime=None):
    if creation_time is None:
        stmt = user_table.insert().values(name=name, email=email)
    else:
        stmt = user_table.insert().values(name=name, email=email, created_at=creation_time)
    with sync_engine.connect() as connection:
    # Execute the statement
        print("statement is : ", stmt)
        result = connection.execute(stmt)
        connection.commit()
        return result

def select_user_table():
    with sync_engine.connect() as connection:
        stmt = select(user_table.c.id, user_table.c.name, user_table.c.email)
        result = connection.execute(stmt)
        rows = result.fetchall()
        return rows
    
def update_user(id, name, email):
    with sync_engine.connect() as connection:
        stmt = user_table.update().\
            values(name=name, email=email).where(user_table.c.id == id)
        result = connection.execute(stmt)
        connection.commit()
        return(result)
 
def delete_user(id):
    with sync_engine.connect() as connection:
        stmt = user_table.delete().where(user_table.c.id == id)
        result = connection.execute(stmt)
        connection.commit()
        return(result)       