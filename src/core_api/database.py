from sqlalchemy import create_engine, MetaData
from config import Settings

settings = Settings()

# Create an engine instance
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

# Create a MetaData instance
metadata = MetaData()