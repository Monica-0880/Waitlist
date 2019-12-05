from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from routes.py import *

app = Flask (__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://url_name:Sky08880@localhost:8889/Restaurant_waitlist'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLALchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if__name__== "__main__":
app.run()



    