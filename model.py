"""Models and database functions."""
# from database import *

from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

# Model definitions

class Character(db.Model):
    """"Characters"""

    __tablename__ = "characters"

    character_id = db.Column(db.String(200), primary_key=True)
    character_name = db.Column(db.String(200), nullable=True)

    # # many to many relationship
    # characters = db.relationship("Mood", backref="users", secondary="entries")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Character character_id={self.character_id} character_name={self.character_name}>"


class Movie(db.Model):
    """Movies"""

    __tablename__ = "movies"

    movie_id = db.Column(db.String(200), primary_key=True)
    movie_title = db.Column(db.String(30))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Movie movie_id={self.movie_id} movie_title={self.movie_title}>"


class Quote(db.Model):
    """"Quotes"""

    __tablename__ = "quotes"

    quote_id = db.Column(db.String(200), primary_key=True)
    character_id = db.Column(db.String(200), db.ForeignKey("characters.character_id"))
    movie_id = db.Column(db.String(200), db.ForeignKey("movies.movie_id"))

    # one to many relationship
    character = db.relationship("Character", backref="quotes")
    movie = db.relationship("Movie", backref="quotes")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Quote quote_id={self.quote_id} character_id={self.character_id} movie_id={self.movie_id}>"


################################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB = os.getenv("POSTGRES_DB")

    # Configure to use our PstgreSQL database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://"+USER+":"+PASSWORD+"@localhost:5432/"+DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    if db.init_app(app):
        print("db.app working")
    else:
        print("db.app not working")
    # Used to recreate my database if I need to drop
    # db.create_all()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    if connect_to_db(app):
        print("Model connected to DB.")
    else:
        print("not model")
