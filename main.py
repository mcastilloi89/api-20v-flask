from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from database import close_db
import post as repo

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

@app.teardown_appcontext
def _teardown(_):
    close_db()

def wants_json():
    return request.args.get("format") == "json"

def data_in():
    return (request.get_json(silent=True) or {}) if request.is_json else request.form

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", name_page="blog")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", name_page="about")

@app.route("/posts", methods=["GET"])
def get_all_post():
    posts = repo.get_all_posts()
    if wants_json():
        return jsonify(ok=True, data=posts)
    return render_template("post/post_list.html", posts_list=posts)

@app.route("/posts/<int:post_id>", methods=["GET"])
def get_one_post(post_id):
    p = repo.get_post(post_id)
    if not p:
        if wants_json():
            return jsonify(ok=False, message="Post no encontrado"), 404
        flash("Post no encontrado", "error")
        return redirect(url_for("get_all_post"))
    if wants_json():
        return jsonify(ok=True, data=p)
    return render_template("post/post.html", post=p)

@app.route("/posts/create", methods=["GET", "POST"])
def create_one_post():
    if request.method == "GET":
        return render_template("post/create.html")

    d = data_in()
    title = (d.get("title") or "").strip()
    content = (d.get("content") or "").strip()

    if not title or not content:
        msg = "Título y contenido son obligatorios."
        if wants_json():
            return jsonify(ok=False, message=msg), 400
        flash(msg, "error")
        return redirect(url_for("create_one_post"))

    new_id = repo.create_post(title, content)
    msg = f"Post creado (id={new_id})."
    if wants_json():
        return jsonify(ok=True, message=msg, id=new_id), 201
    flash(msg, "success")
    return redirect(url_for("get_all_post"))

@app.route("/posts/edit/<int:post_id>", methods=["GET", "POST"])
def edit_one_post(post_id):
    if request.method == "GET":
        p = repo.get_post(post_id)
        if not p:
            flash("Post no encontrado", "error")
            return redirect(url_for("get_all_post"))
        return render_template("post/update.html", post=p)

    d = data_in()
    title = (d.get("title") or "").strip()
    content = (d.get("content") or "").strip()

    if not title or not content:
        msg = "Título y contenido son obligatorios."
        if wants_json():
            return jsonify(ok=False, message=msg), 400
        flash(msg, "error")
        return redirect(url_for("edit_one_post", post_id=post_id))

    ok = repo.update_post(post_id, title, content)
    if not ok:
        if wants_json():
            return jsonify(ok=False, message="No se actualizó (id inexistente)"), 404
        flash("No se actualizó (id inexistente)", "error")
        return redirect(url_for("get_all_post"))

    if wants_json():
        return jsonify(ok=True, message="Actualizado", id=post_id)
    flash("Actualizado", "success")
    return redirect(url_for("get_all_post"))

@app.route("/posts/delete/<int:post_id>", methods=["POST", "DELETE"])
def delete_one_post(post_id):
    ok = repo.delete_post(post_id)
    if not ok:
        if wants_json():
            return jsonify(ok=False, message="No se borró (id inexistente)"), 404
        flash("No se borró (id inexistente)", "error")
        return redirect(url_for("get_all_post"))

    if wants_json():
        return jsonify(ok=True, message="Eliminado")
    flash("Eliminado", "success")
    return redirect(url_for("get_all_post"))

if __name__ == "__main__":
    app.run(debug=True)