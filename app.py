# Jessica Nelson 
# Senior Design Project. Spr 26
# This file is used for Flask and API integration to an automated robot to roam and deliver inside TIW.

# Included pages of the site should be: 
#   Home and Welcome
#   Log of parts to be ordered
#   Information and 'submit order'
#   Status updates

####################################################################
# To run, put: flask --app app run
#
# Run the following when debugging and building for ease of editing:
# flask --app app --debug run
#
# Or to turn off debug mode for testing: 
# flask --app app --debug --no-debug --no-reload
####################################################################


from flask import Flask, render_template, request, redirect, url_for
#import sqlite3                      #SQLite is included with python, it just needs to be imported
#conn = sqlite3.connect(DB_FILE)

#DB_FILE = 'order.db'                # Connects the order.db file to parse through and create commands via python
app = Flask(__name__)               # name of the module, __name__ = main


#below is a simple example to test basic commands
@app.route("/")
@app.route("/home")                 # another alias for the home page
def home():
    return render_template('home.html')

# Example of a route, made by me
@app.route("/login")
def login(): 
    return render_template('login.html')

@app.route("/order_list")
def order_list():
    return render_template('order_list.html')

@app.route("/exit_tab")
def exit_tab():
    return render_template('exit_tab.html')

@app.route("/submit_items", methods=["POST"])
def submit_items():
    name = request.form.get("name")
    eid = request.form.get("eid")
    location = request.form.get("location")
    selected_items = request.form.getlist("items")

    print("\n--- NEW ORDER ---")
    print("Name:", name)
    print("EID:", eid)
    print("Location:", location)
    print("Items:", selected_items)

    return render_template(
        "order_confirmation.html",
        name=name,
        eid=eid,
        location=location,
        items=selected_items
    )

