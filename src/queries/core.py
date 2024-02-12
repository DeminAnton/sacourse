from sqlalchemy import insert, text
from src.database import sync_engine, async_engine
from src.models import metadata_obj, workers_table

async def get123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()}")

def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def insert_data():
    with sync_engine.connect() as conn:
        # stmt = """INSERT INTO workers (username) VALUES
        # ('Bobr'),
        # ('Volk');
        # """
        stmt = insert(workers_table).values(
            [
                {"username": "Bobr"},
                {"username": "Volk"}
            ]
        )
        conn.execute(stmt)
        conn.commit()
