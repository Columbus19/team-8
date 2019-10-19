from flask import Flask, render_template      
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator


app = Flask(__name__)
nav = Nav(app)

nav.register_element('my_navBar', Navbar(
	'Nav',
View('Home Page', 'home'),
View('Profile', 'profile'))
)

@app.route("/")
def home():
    return render_template("chart.html")
    
@app.route("/profile")
def profile():
    return render_template("profile.html")
    
if __name__ == "__main__":
    app.run(debug=True)