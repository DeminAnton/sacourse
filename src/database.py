from asyncio import run
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine, text
from config import settings

sync_engine = create_engine(
    url = settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10   
)

async_engine = create_async_engine(
    url = settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10   
)

async def get123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()}")
        
run(get123())