from app import app
from flask import render_template, request, redirect
import accounts
import topics

@app.route("/")
def index():
    return render_template('index.html', titles=topics.get_all_topic_titles())

@app.route("/newtopic", methods=["get","post"])
def newtopic():
    if request.method == 'GET':
        return render_template('newtopic.html')

    if request.method == 'POST':
        accounts.check_csrf()
        
        topic_name = request.form['Topicname']
        if ' ' in topic_name[0]:
            return render_template('error.html', message='Name of the topic cant start with empty space')
        first_comm = request.form['comments']
        #virheen käsittely tähän
        topic_idr = topics.add_topic(topic_name, first_comm, accounts.user_id()) 
        return redirect("/topic/"+str(topic_idr))

@app.route("/logout")
def logout():
    accounts.logout()
    return redirect("/")


@app.route("/topic/<int:topic_id>", methods=["get","post"])
def show_topic(topic_id):
    if request.method == 'GET':
        info = topics.get_topic_info(topic_id)
        all_comments = topics.get_topic_comments(topic_id)
        return render_template('topic.html', id=topic_id, title=info[0], creator=info[1], comments=all_comments)

    if request.method == 'POST':
        accounts.check_csrf()
        topic_id = request.form["topic_id"]
        #virhe käsittely tähän
        comm = request.form['comments']
        #virheen käsittely tähän
        topics.add_comment(comm, topic_id, accounts.user_id()) 
        return redirect("/topic/"+str(topic_id))


@app.route("/login", methods=["get","post"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        usern = request.form['Username']
        passw = request.form['Password']

        if not accounts.login(usern, passw):
            return render_template('error.html', message='Invalid credentials please try again')
        return redirect("/")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        usern = request.form["username"]
        passw1 = request.form["password1"]
        passw2 = request.form["password2"]
        accounts.register(usern, passw1)
        return redirect("/")
