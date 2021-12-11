import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    # renders home page template when going to the main website link

    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    # sign up page, allows users to signup for an account
    # if username dosen't already exist.

    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "name": request.form.get("name").lower(),
            "username": request.form.get("username").lower(),
            "eamil": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # checks users collection for user and password to allow registered
    # users to sign in. Redirects to profile on successful sign in.
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                 existing_user["password"], request.form.get("password")):
                  session["user"] = request.form.get("username").lower()
                  flash("Welcome, {}".format(
                        request.form.get("username")))
                  return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
           # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # takes the session user's username from 'users' database
    # and returns them to their profile page.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie and returns them to the signin page
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_events")
def get_events():
    # reads all events in events collection 
    # displays events on events.html.
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


@app.route("/search", methods=["GET", "POST"])
def search():
    # returns search results from user input query or drop down
    # selection from events page and saves them to events list.
    # renders template for events.html.
    query = request.form.get("query")
    events = list(mongo.db.events.find({"$text": {"$search": query}}))
    return render_template("events.html", events=events)


@app.route("/create_event", methods=["GET", "POST"])
def create_event():
    # gets values from create event form and stores values
    # into MongoDB collection events. renders create_event.html.
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        event = {
             "category_name": request.form.get("category_name"),
             "date": request.form.get("date"),
             "event_description": request.form.get("event_description"),
             "event_name": request.form.get("event_name"),
             "is_urgent": is_urgent,
             "location": request.form.get("location"),
             "created_by": session["user"]
        }
        mongo.db.events.insert_one(event)
        flash("Event Successfully Created")
        return redirect(url_for("get_events"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_event.html", categories=categories)


@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    # allows user to edit an event. If successful, flash message is displayed
    # to alert user. after edit, user is redirected to events page
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "date": request.form.get("date"),
            "event_description": request.form.get("event_description"),
            "event_name": request.form.get("event_name"),
            "is_urgent": is_urgent,
            "location": request.form.get("location"),
            "created_by": session["user"]
        }
        # update unique event
        mongo.db.events.update_one(
            {"_id": ObjectId(event_id)}, {"$set": submit})
        flash("Event Successfully Updated")

    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_event.html", event=event, categories=categories)


@app.route("/delete_event/<event_id>")
def delete_event(event_id):
     # allows user to delete an event if they created it.
     # returns user back to events page.
    mongo.db.events.delete_one({"_id": ObjectId(event_id)})
    flash("Event Successfully Deleted")
    return redirect(url_for("get_events"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    # allows the site owner/admin create a category. if successful, flash message is displayed
    # to alert site owner/admin. after edit, site owner/admin is redirected to manage categories page
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Created")
        return redirect(url_for("get_categories"))

    return render_template("create_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # allows the site owner/admin to edit any category. if successful, flash message is displayed
    # to alert site owner/admin. after edit, site owner/admin is redirected to manage categories page
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # allows site owner/admin to delete any category.
    # returns site owner/admin back to manage category page.
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


@app.route("/contact")
def contact():
    # renders contact template
    return render_template("contact.html")


@app.route("/about")
def about():
    # renders about page
    return render_template("about.html")  


@app.errorhandler(404)
def not_found_error(error):
    # Route to handle 404 error
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    # Route to handle 500 error
    return render_template('500.html', error=error), 500    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
