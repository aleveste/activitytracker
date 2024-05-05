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
    if users.is_admin():
        return render_template("newevent.html")
    else:
        return render_template("error.html", message="Vain ylläpitäjä voi luoda tapahtumia")

@app.route("/send", methods=["POST"])
def send():
    laji = request.form["laji"]
    if len(laji) > 25:
        return render_template("error.html", message="Lajin nimi on liian pitkä (yli 25 merkkiä)")
    kesto = request.form["kesto"]
    if len(kesto) > 25:   
        return render_template("error.html", message="Kesto ylittää merkkirajan 25")
    extra = request.form["extra"]
    if len(extra) > 200:
        return render_template("error.html", message="Extraosio ylittää merkkirajan 200")
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
        if len(username) > 20 or len(username) < 3:
            return render_template("error.html", message="Väärä käyttäjänimipituus (3-20)")
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if len(password1) > 20 or len(password1) < 8:
            return render_template("error.html", message="Väärä käyttäjänimipituus (8-20)")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
@app.route("/result")
def result():
    result = users.result()
    group = users.groupresult()
    event = users.eventresult()
    return render_template("result.html", result=result, groups=group, events=event)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/profile/<username>")
def user_profile(username):
    if users.user_exist(username) == False:
        return render_template("error.html", message="Käyttäjää ei ole olemassa")
    groups = users.get_user_groups(username)
    events = users.get_user_events(username)
    userposts = posts.get_user_posts(username)
    return render_template("profile.html", posts=userposts, groups=groups, events=events, username=username)

@app.route("/group/<groupname>")
def group_page(groupname):
    if users.group_exist(groupname) == False:
        return render_template("error.html", message="Ryhmää ei ole olemassa")
    info = users.get_group_info(groupname)
    member_count = users.get_group_member_count(groupname)
    group_posts = posts.get_group_posts(groupname)
    ingroup = users.ingroup(groupname)
    return render_template("group.html", groupname=groupname, posts=group_posts, count=member_count, info=info, ingroup=ingroup)

@app.route("/event/<eventname>")
def event_page(eventname):
    if users.event_exist(eventname) == False:
        return render_template("error.html", message="Tapahtumaa ei ole olemassa")
    info = users.get_event_info(eventname)
    member_count = users.get_event_member_count(eventname)
    inevent = users.inevent(eventname)
    return render_template("event.html", eventname=eventname, info=info, count=member_count, inevent=inevent)

@app.route("/joingroup/<groupname>")
def joingroup(groupname):
    users.joingroup(groupname)
    return redirect("/group/" + groupname)

@app.route("/joinevent/<eventname>")
def joinevent(eventname):
    users.joinevent(eventname)
    return redirect("/event/" + eventname)

@app.route("/getadmin")
def getadmin():
    if users.is_admin():
        return render_template("error.html", message="Olet jo ylläpitäjä")
    else:
        users.getadmin()
        return redirect("/")