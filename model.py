from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    ssn = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=False)
    monthly_income = db.Column(db.String(120), unique=True, nullable=False)
    value_of_assets = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '%r' % self.fullname

db.create_all()
db.session.commit()