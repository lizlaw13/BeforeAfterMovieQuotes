"""Models for database."""
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import Seeder
import requests, os
import sys
sys.path.append('../BeforeAfterMovieQuotes')
from model import *
from movielist import movies

db = SQLAlchemy()

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

        for movie in movies:

            try:
                m_id = movie["id"][7:16]
                querystring = {"tconst": m_id}

                response = requests.request("GET", url, headers=headers, params=querystring).json()

                if self.db.session.query(Movie).filter_by(movie_id=m_id).first() is None:
                    m_title = response["base"]["title"]
                    # Add movie to db
                    new_movie = Movie(movie_id=m_id, movie_title=m_title)
                    self.db.session.add(new_movie)

                for quote in response["quotes"]:

                    try:
                        c_id = quote["lines"][0]["characters"][0]["characterId"][-10:-1]
                        c_name = quote["lines"][0]["characters"][0]["character"]

                        if self.db.session.query(Character).filter_by(character_id=c_id).first() is None:
                            # Add character to db
                            new_character = Character(character_id=c_id, character_name=c_name)
                            self.db.session.add(new_character)

                    except:
                        pass

                    try:
                        q_id = quote["id"][-9:]
                        q_text = quote["lines"][0]["text"]

                        if self.db.session.query(Quote).filter_by(quote_id=q_id).first() is None:
                            # Add quote to db
                            new_quote = Quote(quote_id=q_id,quote_text=q_text,character_id=c_id, movie_id=m_id)
                            self.db.session.add(new_quote)

                    except:
                        pass

            except:
                pass
