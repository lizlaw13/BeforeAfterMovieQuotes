"""Models for database."""
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import Seeder
import requests, os

db = SQLAlchemy()

# Tables for database
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


# For FlaskSeeder to load database
class DemoSeeder(Seeder):

    def run(self):

        # Request to RapidAPI to retrieve information for each movie
        url = "https://imdb8.p.rapidapi.com/title/get-quotes"

        KEY = os.getenv("RAPIDAPI_KEY")
        HOST = os.getenv("RAPIDAPT_HOST")

        headers = {
            "x-rapidapi-key": KEY,
            "x-rapidapi-host": HOST
            }

        movielist = [{
            "id": "/title/tt0111161/",
            "chartRating": 9.2
        },
        {
            "id": "/title/tt0068646/",
            "chartRating": 9.1
        }       
        ]

        for movie in movielist:
            m_id = movie["id"][7:16]

            querystring = {"tconst": m_id}

            response = requests.request("GET", url, headers=headers, params=querystring).json()        
            if self.db.session.query(Movie).filter_by(movie_id=m_id).first() is None:
                m_title = response["base"]["title"]

                new_movie = Movie(movie_id=m_id, movie_title=m_title)
                self.db.session.add(new_movie)
            else: 
                print('REJECTED HEHE')

    

            # for quote in response["quotes"]:

            #     c_id = quote["lines"][0]["characters"][0]["characterId"][-10:-1]
            #     c_name = quote["lines"][0]["characters"][0]["character"]

            #     if self.db.session.query(Character).filter_by(character_id=c_id).first() is None:
            #         new_character = Character(character_id=c_id, character_name=c_name)
            #         self.db.session.add(new_character)

            # m_title = response["base"]["title"]
            # q_id = response["quotes"][0]["id"][-9:]

                # adding response to database

                # new_movie = Movie(movie_id=m_id, movie_title=m_title)
                # new_quote = Quote(quote_id=movie_quotes["quotes"][0]["id"][-9:], character_id=movie_quotes["quotes"][0]["lines"][0]["characters"][0], movie_id=data['movies.movie_id'])
