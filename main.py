from flask import Flask, render_template
from model import User, db, app
import pdb

@app.route("/")
def home():
    joe = User(fullname='Joseph Nastasi', email='joe@jp.org', ssn='123-45-6789',phone_number='8106236861', monthly_income='1,000,000', value_of_assets='1,000,000', total_debt=200000,debt_dist1=10,debt_dist2=20,debt_dist3=70)
    average = User(fullname='AVERAGE', email='avg@jp.org', ssn='987-54-321',phone_number='12345678', monthly_income='2,000,000', value_of_assets='2,000,000',total_debt=300000,debt_dist1=50,debt_dist2=30,debt_dist3=20)
    
    
    joe_data = User.query.filter_by(fullname='Joseph Nastasi').first()
    avg_data = User.query.filter_by(fullname='AVERAGE').first()
    
    
    if not joe_data:
        db.session.add(joe)
    if not avg_data:
        db.session.add(average)
    joe_data = User.query.filter_by(fullname='Joseph Nastasi').first()
    avg_data = User.query.filter_by(fullname='AVERAGE').first()
    
    
    db.session.commit()
    bar = joe_data.total_debt
    val1 = joe_data.debt_dist1
    val2 = joe_data.debt_dist2
    val3 = joe_data.debt_dist3

    

    avg1 = avg_data.debt_dist1
    avg2 = avg_data.debt_dist2
    avg3 = avg_data.debt_dist3

    return render_template("chart.html", joe_data=joe_data, val1=val1, val2=val2, val3=val3, bar=bar, avg1=avg1, avg2=avg2, avg3=avg3)
    
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/tools")
<<<<<<< HEAD
def tools(): 
    return render_template("resources.html")    
    
if __name__ == "__main__":
    app.run(debug=True)
=======
def tools():
        return render_template("tools.html")

>>>>>>> 7ccd160b037e27e28bc3b2f282d26734d85215df

