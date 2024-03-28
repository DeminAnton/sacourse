import orm_api.database as orm_db
import orm_api.models as orm_models
from sqlalchemy import select


def all_posts(name: str):
    with orm_db.Session(bind=orm_db.sync_engine) as session:
        stmt = select(orm_models.User, orm_models.Post)\
        .join(orm_models.User.posts)\
        .where(orm_models.User.name == name)
        r = session.execute(stmt)
        result = [(i.User.name, i.Post.text) for i in r]
        
    return result
