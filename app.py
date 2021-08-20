from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from model import *
from dotenv import load_dotenv
import os, random

app = Flask(__name__)

# Retrieve variables from .env file
load_dotenv()
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB = os.getenv("POSTGRES_DB")

# Configure to use our PostgreSQL database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://"+USER+":"+PASSWORD+"@localhost:5432/"+DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

# FlaskSeeder extnesion to load database
seeder = FlaskSeeder()
seeder.init_app(app, db)


@app.route("/")
def hello():
    """Homepage"""

    quote1 = Quote.query.random()

    return render_template(
    "base.html",
    quote1=quote1
    )

if __name__ == "__main__":

    app.run(debug=True)
