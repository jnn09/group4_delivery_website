# Jessica Nelson 
# Senior Design Project. Spr 26
# This file is used for Flask and API integration to an automated robot to roam TIW.

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


from flask import Flask, render_template
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
@app.route("/new_order")
def new_order(): 
    return "<h1>Start a New Order</h1>"
