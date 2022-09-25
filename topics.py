from db import db

def add_topic(title, comment, creator_id):
    sqlcom = "INSERT INTO topic (creator_id, title, visible) VALUES (:creator_id, :title, 1) RETURNING id"
    topic_id = db.session.execute(sqlcom, {"creator_id":creator_id, "title":title}).fetchone()[0]

    sqlcom = "INSERT INTO comments (creator_id, topic_id, comment) VALUES (:creator_id, :topic_id, :comment)"
    db.session.execute(sqlcom, {"creator_id":creator_id, "topic_id":topic_id, "comment":comment})

    db.session.commit()
    return topic_id

def get_topic_info(topic_id):
    sqlcom = "SELECT t.title, u.name FROM topic t, users u WHERE t.id=:topic_id AND t.creator_id=u.id"
    return db.session.execute(sqlcom, {"topic_id": topic_id}).fetchone()

def get_all_topic_titles():
    sqlcom = "SELECT id, title FROM topic"
    return db.session.execute(sqlcom).fetchall()

def get_topic_comments(topic_id):
    sqlcom = "SELECT u.name, c.comment FROM comments c, users u WHERE c.creator_id=u.id AND c.topic_id=:topic_id ORDER BY c.id"
    return db.session.execute(sqlcom, {"topic_id": topic_id}).fetchall()

def add_comment(comment, topic_id, creator_id):
    sqlcom = "INSERT INTO comments (creator_id, topic_id, comment) VALUES (:creator_id, :topic_id, :comment)"
    db.session.execute(sqlcom, {"creator_id":creator_id, "topic_id":topic_id, "comment":comment})
    db.session.commit()
