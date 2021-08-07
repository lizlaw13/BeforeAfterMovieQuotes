from flask.json import jsonify
from flask_seeder import Seeder, Faker, generator
import requests, os
from seeds.model import *
from app import *
from movielist import movies
from dotenv import load_dotenv


load_dotenv()

lst = movies

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
        # new_movie = Movie(movie_id=m_id, movie_title=m_title)
        # # new_quote = Quote(quote_id=movie_quotes["quotes"][0]["id"][-9:], character_id=movie_quotes["quotes"][0]["lines"][0]["characters"][0], movie_id=data['movies.movie_id'])
        # db.session.add(new_character)
        # db.session.commit()

        # db.session.add(new_movie)
        # db.session.commit()

    # def loadDB(movielist):

    #     url = "https://imdb8.p.rapidapi.com/title/get-quotes"

    #     KEY = os.getenv("RAPIDAPI_KEY")
    #     HOST = os.getenv("RAPIDAPT_HOST")

    #     headers = {
    #         "x-rapidapi-key": KEY,
    #         "x-rapidapi-host": HOST
    #         }

    #     # for movie in movielist:
    #     movie_id = movielist[0]["id"][7:16]
    #     querystring = {"tconst": movie_id}

    #     response = requests.request("GET", url, headers=headers, params=querystring).json()

    #     # querying response
    #     c_id = response["quotes"][0]["lines"][0]["characters"][0]["characterId"][-10:-1]
    #     c_name = response["quotes"][0]["lines"][0]["characters"][0]["character"]
    #     m_id = movie_id
    #     m_title = response["base"]["title"]
    #     q_id = response["quotes"][0]["id"][-9:]
        


    #     # adding response to database
    #     new_character = Character(character_id=c_id, character_name=c_name)
    #     new_movie = Movie(movie_id=m_id, movie_title=m_title)
    #     # new_quote = Quote(quote_id=movie_quotes["quotes"][0]["id"][-9:], character_id=movie_quotes["quotes"][0]["lines"][0]["characters"][0], movie_id=data['movies.movie_id'])
    #     db.session.add(new_character)
    #     db.session.commit()

    #     db.session.add(new_movie)
    #     db.session.commit()



