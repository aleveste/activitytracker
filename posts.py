from db import db
from sqlalchemy.sql import text
import users

def get_posts():
    sql = """
    SELECT P.laji, P.kesto, P.extra, U.username, P.sent_at 
    FROM posts P
    JOIN users U ON P.user_id = U.id
    ORDER BY P.id
    """
    result = db.session.execute(text(sql))
    return result.fetchall()

def send(laji, kesto, extra):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = """
    INSERT INTO posts (laji, kesto, extra, user_id, sent_at) 
    VALUES (:laji, :kesto, :extra, :user_id, NOW())
    """
    stmt = text(sql).bindparams(laji=laji, kesto=kesto, extra=extra, user_id=user_id)
    db.session.execute(stmt)
    db.session.commit()
    return True


