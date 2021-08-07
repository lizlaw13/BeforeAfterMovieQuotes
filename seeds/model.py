"""Models for database."""
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import Seeder
import requests, os
from movielist import movies



db = SQLAlchemy()

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

class DemoSeeder(Seeder):
    movielist = movies
    def run(self, movielist):
        url = "https://imdb8.p.rapidapi.com/title/get-quotes"

        KEY = os.getenv("RAPIDAPI_KEY")
        HOST = os.getenv("RAPIDAPT_HOST")

        headers = {
            "x-rapidapi-key": KEY,
            "x-rapidapi-host": HOST
            }

        # for movie in movielist:
        movie_id = movielist[0]["id"][7:16]
        querystring = {"tconst": movie_id}

        response = requests.request("GET", url, headers=headers, params=querystring).json()

        # querying response
        c_id = response["quotes"][0]["lines"][0]["characters"][0]["characterId"][-10:-1]
        c_name = response["quotes"][0]["lines"][0]["characters"][0]["character"]
        m_id = movie_id
        m_title = response["base"]["title"]
        q_id = response["quotes"][0]["id"][-9:]


        
        # adding response to database
        new_character = Character(character_id=c_id, character_name=c_name)

        self.db.session.add(new_character)