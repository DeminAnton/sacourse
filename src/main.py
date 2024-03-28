import orm_api.database as orm_db
import orm_api.models as orm_models
import orm_api.queries as qry
from core_api.database import metadata, sync_engine
from core_api.crud import insert_user, select_user_table, update_user, delete_user
# This import is necessary to ensure the models are loaded
import core_api.models

core = False

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
        with orm_db.Session(bind=orm_db.sync_engine) as session:       
            # Add sample users
            for i in range(5):
                user = orm_models.User(name=f'User {i+1}')
                session.add(user)
            
            session.commit()
            
            # Add sample posts and comments for each user
            for user in session.query(orm_models.User).all():
                for j in range(4):  # Ensuring at least 10 posts in total
                    post = orm_models.Post(user=user, text=f'Post {j+1} by {user.name}')
                    session.add(post)
                    session.commit()  # Commit to ensure we have a post ID
            
                    # Add comments to each post by all users
                    for commenter in session.query(orm_models.User).all():
                        comment = orm_models.Comment(user=commenter, post=post, text=f'Comment by {commenter.name} on {post.text}')
                        session.add(comment)
            
            session.commit()
        result = qry.all_posts("User 2")
        for row in result:
            print(row)
            input("press any key")
            # Now, the database is populated with users, posts, and comments.
        input("press any key for finish")
        orm_models.Base.metadata.drop_all(orm_db.sync_engine)
        