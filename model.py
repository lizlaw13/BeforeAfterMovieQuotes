"""Models for database."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tables for database
class Character(db.Model):
    """"Character information."""

    __tablename__ = "characters"

    character_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    character_imdb_id = db.Column(db.String(200))
    character_name = db.Column(db.String(200))

    def __init__(self, character_id, character_imdb_id, character_name):
        self.character_id = character_id
        self.character_imdb_id = character_imdb_id
        self.character_name = character_name

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Character character_id={self.character_id} character_imdb_id={self.character_imdb_id} character_name={self.character_name}>"


class Movie(db.Model):
    """Movie information"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_imdb_id = db.Column(db.String(200))
    movie_title = db.Column(db.String(30))

    def __init__(self, movie_id, movie_imdb_id, movie_title):
        self.movie_id = movie_id
        self.movie_imdb_id = movie_imdb_id
        self.movie_title = movie_title

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Movie movie_id={self.movie_id} movie_imdb_id={self.movie_imdb_id} movie_title={self.movie_title}>"


class Quote(db.Model):
    """"Quote information."""

    __tablename__ = "quotes"

    quote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quote_imdb_id = db.Column(db.String(200))
    quote_text = db.Column(db.Text)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.character_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))

    def __init__(self, quote_id, quote_imdb_id, quote_text, character_id, movie_id):
        self.quote_id = quote_id
        self.quote_imdb_id = quote_imdb_id
        self.quote_text = quote_text
        self.character_id = character_id
        self.movie_id = movie_id

    character = db.relationship("Character", backref="quotes")
    movie = db.relationship("Movie", backref="quotes")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Quote quote_id={self.quote_id} quote_imdb_id={self.quote_imdb_id} quote_text={self.quote_text} character_id={self.character_id} movie_id={self.movie_id}>"
