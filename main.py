from flask import Flask, render_template      



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("chart.html")
    
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/tools")
def tools(): 
    return render_template("resources.html")    
    
if __name__ == "__main__":
    app.run(debug=True)
