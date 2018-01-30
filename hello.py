from flask import Flask, render_template, request, url_for
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[YOUR_DATABASE_NAME]'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/index')
def show_index():
        return render_template('index.html')
