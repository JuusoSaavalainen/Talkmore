from app import app
from flask import render_template, request, redirect, session
import accounts
import topics

@app.route("/")
def index():
    comments = topics.get_topic_comments_len()
    titles = topics.get_all_topic_titles_desc()
    categorys=topics.get_categorys()
    return render_template('index.html', titles=titles, comments=comments, categorys=categorys)

@app.route("/newtopic", methods=["get","post"])
def newtopic():
    if request.method == 'GET':
        return render_template('newtopic.html', categorys=topics.get_categorys())

    if request.method == 'POST':
        accounts.check_csrf()

        topic_name = request.form['Topicname']
        if ' ' in topic_name[0]:
            return render_template('error.html', message='Name of the topic cant start with empty space')

        first_comm = request.form['comments']
        if ' ' in first_comm[0]:
            return render_template('error.html', message='Name of the comment cant start with empty space')


        topic_category = request.form['category']
        topic_id = topics.add_topic(topic_name, first_comm, accounts.user_id(), topic_category)
        return redirect("/topic/"+str(topic_id))

@app.route("/topic/<int:topic_id>", methods=["get","post"])
def show_topic(topic_id):
    if request.method == 'GET':
        listlikes = []
        info = topics.get_topic_info(topic_id)
        all_comments = topics.get_topic_comments(topic_id)
        for i in all_comments:
            listlikes.append(topics.get_likes(i[2]))
        return render_template('topic.html', id=topic_id, title=info[0], creator=info[1], comments=all_comments, likes=listlikes)

    if request.method == 'POST':
        accounts.check_csrf()
        topic_id = request.form["topic_id"]
        comm = request.form['comments']
        if len(comm) == 0  or ' ' in comm[0]:
            return render_template('error.html', message='Name of the comment cant start with empty space')
        topics.add_comment(comm, topic_id, accounts.user_id())
        return redirect("/topic/"+str(topic_id))


@app.route("/likess", methods=["post"])
def likes():
    if request.method == 'POST':
        accounts.check_csrf()
        liker_id = request.form['comm_id']
        t_id = request.form['topic_idr']
        tpc_id = request.form['topic_id']
        topics.add_likes(liker_id,t_id)
        return redirect("/topic/"+str(tpc_id))

@app.route("/delcom", methods=["post"])
def delcom():
    if request.method == 'POST':
        accounts.check_csrf()
        c_id = request.form['comm_id']
        tpc_id = request.form['topic_id']
        bool_ean = topics.del_comment(c_id, tpc_id)
        if bool_ean:
            return redirect("/topic/"+str(tpc_id))
        else:
            return redirect("/")

@app.route("/deltopic", methods=["post"])
def deltopic():
    if request.method == "POST":
        accounts.check_csrf()
        tpc_id = request.form['topic_id']
        topics.del_topic(tpc_id)
        return redirect("/")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        usern = request.form['Username'].lower()
        passw = request.form['Password']

        if not accounts.login(usern, passw):
            return render_template('error.html', message='Invalid credentials please try again', route='/login')
        return render_template('succes.html', message='logged in!', route='/')

@app.route("/logout")
def logout():
    accounts.logout()
    return render_template('succes.html', message='logged out!', route='/')

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        usern = request.form["username"].lower()
        passw1 = request.form["password1"]
        passw2 = request.form["password2"]

        if ' ' in usern:
            return render_template("error.html", message='Username cannot include whitespaces', route='/register')

        if len(usern) < 3:
            return render_template("error.html", message='Username must be atleast 3 char', route='/register')

        if passw1 != passw2:
            return render_template("error.html", message='Passwords dont match', route='/register')

        if len(passw1) < 8:
            return render_template("error.html", message='Password must be atleast 8 char', route='/register')

        if accounts.register(usern, passw1) == False:
            return render_template("error.html", message='Username was already taken', route='/register')

        accounts.login(usern, passw1)
        return render_template('succes.html', message='registered, i logged you in!',route='/')

@app.route("/result")
def result():
    query = request.args["query"]
    return render_template("result.html", messages=topics.search_comm(query))

@app.route("/account", methods=["get", "post"])
def myacc():
    if request.method == 'GET':
        return render_template('account.html')

    if request.method == 'POST':
        accounts.check_csrf()
        user = request.form["topic_idr"]
        accounts.logout()
        accounts.delete_acc(user)
        return redirect("/register")
        

@app.route("/about")
def about():
    return render_template('about.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', message='500', route='/')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', message='404', route='/')
