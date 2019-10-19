from flask import Flask, render_template
from model import User, db, app
import pdb

@app.route("/")
def home():
    joe = User(fullname='Joseph Nastasi', email='joe@jp.org', ssn='123-45-6789',phone_number='8106236861', monthly_income='1,000,000', value_of_assets='1,000,000', total_debt=200000,debt_dist1=10,debt_dist2=20,debt_dist3=70)
    cajevamiel = User(fullname='Caj Evamiel', email='caj@jp.org', ssn='987-54-321',phone_number='12345678', monthly_income='2,000,000', value_of_assets='2,000,000',total_debt=300000,debt_dist1=50,debt_dist2=30,debt_dist3=20)
    db.session.add(joe)
    db.session.add(cajevamiel)
    db.session.commit()
    # name = User.query.filter_by(fullname='Joseph Nastasi').first()
    dynamic_bar = User.query.filter_by(fullname='Joseph Nastasi').first()
    
    val1 = dynamic_bar.debt_dist1
    val2 = dynamic_bar.debt_dist2
    val3 = dynamic_bar.debt_dist3

    return render_template("chart.html", dynamic_bar=dynamic_bar, val1=val1, val2=val2, val3=val3)
    
@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run()
