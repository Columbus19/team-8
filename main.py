from flask import Flask, render_template
from model import User, db, app

@app.route("/")
def home():
    return render_template("chart.html")
    
@app.route("/profile")
def profile():
    joe = User(fullname='Joseph Nastasi', email='joe@jp.org', ssn='123-45-6789',phone_number='8106236861', monthly_income='1,000,000', value_of_assets='1,000,000')
    cajevamiel = User(fullname='Caj Evamiel', email='caj@jp.org', ssn='987-54-321',phone_number='12345678', monthly_income='2,000,000', value_of_assets='2,000,000')
    db.session.add(joe)
    db.session.add(cajevamiel)
    db.session.commit()
    result = User.query.filter_by(fullname='Joseph Nastasi').first()
    print(result)
    return render_template("profile.html")

@app.route("/tools")
def tools(): 
    return render_template("resources.html")    
    
if __name__ == "__main__":
    app.run(debug=True)

