import os
from db import db
from flask import abort , request , session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

def login(name, password):
    sql = "SELECT password, id FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    acc = result.fetchone()
    if not acc:
        return False
    if not check_password_hash(acc[0], password):
        return False
    session['user_id'] = acc[1]
    session['user_name'] = name
    session['csrf_token'] = os.urandom(16).hex()
    return True


def register(name, password):
    sql = "SELECT name FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    acc = result.fetchone()
    if acc:
        return False
    hash = generate_password_hash(password)
    sqlcom = "INSERT INTO users (name, password) VALUES (:name, :password)"
    db.session.execute(sqlcom, {"name":name, "password":hash})
    db.session.commit()
    return login(name, password)
    

def logout():
    del session['user_id']
    del session['user_name']

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

def user_id():
    return session.get("user_id", 0)

def delete_acc(user):
    sqlcom = "DELETE FROM users WHERE id=:user"
    db.session.execute(sqlcom, {"user":user})
    db.session.commit()
    return
