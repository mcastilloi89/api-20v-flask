from database import get_db

def create_post(title, content):
    db = get_db()
    cur = db.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    db.commit()
    return cur.lastrowid

def get_all_posts():
    db = get_db()
    cur = db.execute("SELECT * FROM posts ORDER BY id DESC")
    return [dict(r) for r in cur.fetchall()]

def get_post(post_id):
    db = get_db()
    cur = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    row = cur.fetchone()
    return dict(row) if row else None

def update_post(post_id, title, content):
    db = get_db()
    cur = db.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (title, content, post_id))
    db.commit()
    return cur.rowcount > 0

def delete_post(post_id):
    db = get_db()
    cur = db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    db.commit()
    return cur.rowcount > 0