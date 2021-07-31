from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
# Retrieve variables from .env file
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB = os.getenv("POSTGRES_DB")

# Configure to use our PostgreSQL database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://"+USER+":"+PASSWORD+"@localhost:5432/"+DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


class Character(db.Model):
    """"Character information."""

    __tablename__ = "characters"

    character_id = db.Column(db.String(200), primary_key=True)
    character_name = db.Column(db.String(200), nullable=True)

    def __init__(self, character_id, character_name):
        self.character_id = character_id
        self.character_name = character_name

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Character character_id={self.character_id} character_name={self.character_name}>"


class Movie(db.Model):
    """Movie information"""

    __tablename__ = "movies"

    movie_id = db.Column(db.String(200), primary_key=True)
    movie_title = db.Column(db.String(30))

    def __init__(self, movie_id, movie_title):
        self.movie_id = movie_id
        self.movie_title = movie_title

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Movie movie_id={self.movie_id} movie_title={self.movie_title}>"


class Quote(db.Model):
    """"Quote information."""

    __tablename__ = "quotes"

    quote_id = db.Column(db.String(200), primary_key=True)
    character_id = db.Column(db.String(200), db.ForeignKey("characters.character_id"))
    movie_id = db.Column(db.String(200), db.ForeignKey("movies.movie_id"))

    def __init__(self, quote_id, character_id, movie_id):
        self.quote_id = quote_id
        self.character_id = character_id
        self.movie_id = movie_id

    character = db.relationship("Character", backref="quotes")
    movie = db.relationship("Movie", backref="quotes")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Quote quote_id={self.quote_id} character_id={self.character_id} movie_id={self.movie_id}>"
#

# @app.route("/", methods=["POST", "GET"])
# def index():
#     """Homepage"""
#
#     return render_template("index.html")

@app.route("/")
def hello():
    """Homepage"""

    return {"hello": "world"}
if __name__ == "__main__":

    app.run(debug=True)
