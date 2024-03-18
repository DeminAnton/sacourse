import orm_api.database as orm_db
import orm_api.models as orm_models
from core_api.database import metadata, sync_engine
from core_api.crud import insert_user, select_user_table, update_user, delete_user
# This import is necessary to ensure the models are loaded
import core_api.models

core = True

if __name__  == "__main__":
    if core:
        metadata.create_all(sync_engine)
        insert_user("Tony", email="tony@mail.com")
        insert_user("Mark", email="mark@mail.com")
        insert_user("Xenia", email="xenia@mail.com")
        rows = select_user_table()
        print(rows)
        update_user(id=3, name="kseniya", email="kseniya@mail.com")
        delete_user(id=1)
        rows = select_user_table()
        print(rows)
        input("press any key")
        metadata.drop_all(sync_engine)
    else:
        orm_models.Base.metadata.create_all(orm_db.sync_engine)
        input("press any key")
        orm_models.Base.metadata.drop_all(orm_db.sync_engine)
