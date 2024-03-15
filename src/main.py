import orm_api.database as orm_db
import orm_api.models as orm_models
from core_api.database import metadata, sync_engine
import core_api.models as core_models

core = True

if __name__  == "__main__":
    if core:
        core_models.user_table
        metadata.create_all(sync_engine)
        input("press any key")
        metadata.drop_all(sync_engine)
    else:
        orm_models.Base.metadata.create_all(orm_db.sync_engine)
        input("press any key")
        orm_models.Base.metadata.drop_all(orm_db.sync_engine)
