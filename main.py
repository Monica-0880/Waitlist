from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from routes.py import *

app = Flask (__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://url_name:Sky08880@localhost:8889/Restaurant_waitlist'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

class Restaurant(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    company_name = db.Column( db.String(120))
    username = db.Column( db.String(120))
    password = db.Column( db.String(120))

    def __init__(self, company_name, username, password):
        self.company_name = company_name
        self.username = username
        self.password = password
        
