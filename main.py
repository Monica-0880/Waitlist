from flask import Flask, render_template
# from routes.py import *


app = Flask (__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')




    