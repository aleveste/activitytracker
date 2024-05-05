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

def groupresult():
    query = request.args["query"]
    sql = text("SELECT group_name FROM groups WHERE group_name LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    results = result.fetchall()
    return results

def eventresult():
    query = request.args["query"]
    sql = text("SELECT event_name FROM events WHERE event_name LIKE :query")
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

def get_group_info(groupname):
    sql= text("""SELECT G.group_info
              FROM Groups G
              WHERE G.group_name = :groupname""")
    result = db.session.execute(sql, {"groupname": groupname})
    return result.fetchone()

def get_event_info(eventname):
    sql= text("""SELECT E.event_info
              FROM Events E
              WHERE E.event_name = :eventname""")
    result = db.session.execute(sql, {"eventname": eventname})
    return result.fetchone()

def get_group_member_count(groupname):
    sql= text("""SELECT COUNT(*)
              FROM Groupmembers GM
              LEFT JOIN Groups G ON GM.group_id = G.id
              WHERE G.group_name = :groupname""")
    result = db.session.execute(sql, {"groupname": groupname})
    return result.fetchone()

def get_event_member_count(eventname):
    sql= text("""SELECT COUNT(*)
              FROM Eventmembers EM
              LEFT JOIN Events E ON EM.event_id = E.id
              WHERE E.event_name = :eventname""")
    result = db.session.execute(sql, {"eventname": eventname})
    return result.fetchone()

def ingroup(groupname):
    session_id = user_id()
    sql= text("""SELECT *
              FROM Groupmembers GM
              LEFT JOIN Groups G ON GM.group_id = G.id
              WHERE G.group_name = :groupname AND GM.member_id = :session_id""")
    result = db.session.execute(sql, {"groupname": groupname, "session_id": session_id})
    if result.rowcount > 0:
        return True
    else: 
        return False
    
def inevent(eventname):
    session_id = user_id()
    sql= text("""SELECT *
              FROM Eventmembers EM
              LEFT JOIN Events E ON EM.event_id = E.id
              WHERE E.event_name = :eventname AND EM.member_id = :session_id""")
    result = db.session.execute(sql, {"eventname": eventname, "session_id": session_id})
    if result.rowcount > 0:
        return True
    else: 
        return False
    
def joingroup(groupname):
    session_id = user_id()
    sql= text("""INSERT INTO groupmembers (group_id, member_id)
              SELECT G.id, :session_id
              FROM groups G
              WHERE G.group_name = :groupname""")
    db.session.execute(sql, {"groupname": groupname, "session_id": session_id})
    db.session.commit()
    return True

def joinevent(eventname):
    session_id = user_id()
    sql= text("""INSERT INTO eventmembers (event_id, member_id)
              SELECT E.id, :session_id
              FROM events E
              WHERE E.event_name = :eventname""")
    db.session.execute(sql, {"eventname": eventname, "session_id": session_id})
    db.session.commit()
    return True

def getadmin():
    session_id = user_id()
    sql=text("""INSERT INTO admins (user_id)
             VALUES (:session_id)""")
    db.session.execute(sql, {"session_id": session_id})
    db.session.commit()
    return True

def is_admin():
    session_id = user_id()
    sql=text("""SELECT *
             FROM admins A
             WHERE A.user_id = :session_id""")
    result = db.session.execute(sql, {"session_id": session_id})
    if result.rowcount > 0:
        return True
    else:
        return False
    
def user_exist(username):
    sql=text("""SELECT *
             FROM users U
             WHERE U.username = :username""")
    result = db.session.execute(sql, {"username": username})
    if result.rowcount > 0:
        return True
    else:
        return False
    
def group_exist(groupname):
    sql=text("""SELECT *
             FROM groups G
             WHERE G.group_name = :groupname""")
    result = db.session.execute(sql, {"groupname": groupname})
    if result.rowcount > 0:
        return True
    else:
        return False
    
def event_exist(eventname):
    sql=text("""SELECT *
             FROM events E
             WHERE E.event_name = :eventname""")
    result = db.session.execute(sql, {"eventname": eventname})
    if result.rowcount > 0:
        return True
    else:
        return False
    