from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from send_mail import send_mail
app = Flask(__name__)


import os
basedir = os.path.abspath(os.path.dirname(__file__))


ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3050manu@localhost/flap'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer,primary_key=True)
    customer = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    rating = db.Column(db.String(200))
    comments = db.Column(db.String(200))

    def __init__(self,customer,dealer,rating,comment):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comment = comment

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        print(customer,comments)
        if customer == '' or dealer == '':
            return render_template('index.html',message="Please enter the required fields")
        feedback = Feedback(customer,dealer,rating,comments)
        db.session.add(feedback)
        db.session.commit()
        # db.save()
        send_mail(customer)
        return render_template('success.html')
    return render_template('index.html')


if __name__ == "__main__":
    
    app.run()