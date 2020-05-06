from models import *
import db
import os

if __name__ == '__main__':
    path = SQLITE3_NAME
    if not os.path.isfile(path):
        Base.metadata.create_all(db.engine)
    
    admin = User(username='admin',password='fastapi',mail='hoge@example.com')
    db.session.add(admin)
    db.session.commit()
    task = Task(
        user_id=admin.id,
        content='何かしらの締め切り',
        deadline=datetime(2020,5,12,14,40,00)
    )
    
    db.session.add(task)
    db.session.commit()
    db.session.close()