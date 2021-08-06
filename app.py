from flask import Flask, request
from flask_migrate import Migrate
from model import *
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
# Retrieve variables from .env file
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB = os.getenv("POSTGRES_DB")

# Configure to use our PostgreSQL database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://"+USER+":"+PASSWORD+"@localhost:5432/"+DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello():
    """Homepage"""

    return {"hello": "world"}

if __name__ == "__main__":

    app.run(debug=True)
