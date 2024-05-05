from db import db
from sqlalchemy.sql import text
import users

def get_posts():
    sql = """
    SELECT P.laji, P.kesto, P.extra, U.username, P.sent_at 
    FROM posts P
    JOIN users U ON P.user_id = U.id
    ORDER BY P.id DESC
    """
    result = db.session.execute(text(sql))
    return result.fetchall()

def get_user_posts(username):
    sql = """
    SELECT P.laji, P.kesto, P.extra, P.sent_at 
    FROM posts P
    JOIN users U ON P.user_id = U.id
    WHERE U.username = :username
    ORDER BY P.id DESC
    """
    result = db.session.execute(text(sql), {"username": username})
    return result.fetchall()

def get_group_posts(groupname):
    sql = """
    SELECT P.laji, P.kesto, P.extra, U.username, P.sent_at 
    FROM posts P
    JOIN users U ON P.user_id = U.id
    JOIN groupmembers GM ON U.id = GM.member_id
    JOIN groups G ON GM.group_id = G.id
    WHERE G.group_name = :groupname
    ORDER BY P.id DESC
    """
    result = db.session.execute(text(sql), {"groupname": groupname})
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

def eventcreate(nimi, info):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = """
    INSERT INTO events (event_name, event_info, organizer_id)
    VALUES (:nimi, :info, :user_id)"""
    stmt = text(sql).bindparams(nimi=nimi, info=info, user_id=user_id)
    db.session.execute(stmt)
    db.session.commit()
    return True


def groupcreate(nimi, info):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = """
    INSERT INTO groups (group_name, group_info, owner_id)
    VALUES (:nimi, :info, :user_id)"""
    stmt = text(sql).bindparams(nimi=nimi, info=info, user_id=user_id)
    db.session.execute(stmt)
    db.session.commit()
    return True


