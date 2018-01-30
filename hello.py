from flask import Flask, render_template, request, url_for
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route("/")
def show_index():
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

