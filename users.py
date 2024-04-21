from db import db
from sqlalchemy.sql import text
from flask import session, request
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    stmt = text(sql).bindparams(username=username)
    result = db.session.execute(stmt)
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        stmt = text(sql).bindparams(username=username, password=hash_value)
        db.session.execute(stmt)
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)

def result():
    query = request.args["query"]
    sql = text("SELECT username FROM users WHERE username LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    results = result.fetchall()
    return results

def get_user_events(username):
    sql = text("""SELECT E.event_name 
               FROM Events E 
               LEFT JOIN Eventmembers EM ON E.id = EM.event_id 
               LEFT JOIN users U ON EM.member_id = U.id 
               WHERE U.username = :username""")
    result = db.session.execute(sql, {"username": username})
    return result.fetchall()


def get_user_groups(username):
    sql = text("""SELECT G.group_name 
               FROM Groups G 
               LEFT JOIN Groupmembers GM ON G.id = GM.group_id 
               LEFT JOIN users U ON GM.member_id = U.id 
               WHERE U.username = :username""")
    result = db.session.execute(sql, {"username": username})
    return result.fetchall()