from app import app
from flask import render_template, request, redirect, session
import posts, users

@app.route("/")
def index():
    list = posts.get_posts()
    return render_template("index.html", posts=list)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/newgroup")
def newgroup():
    return render_template("newgroup.html")

@app.route("/newevent")
def newevent():
    return render_template("newevent.html")

@app.route("/send", methods=["POST"])
def send():
    laji = request.form["laji"]
    kesto = request.form["kesto"]
    extra = request.form["extra"]
    if posts.send(laji, kesto, extra):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/eventcreate", methods=["POST"])
def eventcreate():
    nimi = request.form["nimi"]
    info = request.form["info"]
    if posts.eventcreate(nimi, info):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/groupcreate", methods=["POST"])
def groupcreate():
    nimi = request.form["nimi"]
    info = request.form["info"]
    if posts.groupcreate(nimi, info):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
@app.route("/result")
def result():
    result = users.result()
    return render_template("result.html", result=result)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/profile/<username>")
def user_profile(username):
    groups = users.get_user_groups(username)
    events = users.get_user_events(username)
    userposts = posts.get_user_posts(username)
    return render_template("profile.html", posts=userposts, groups=groups, events=events, username=username)
