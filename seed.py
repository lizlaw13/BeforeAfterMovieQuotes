from flask.json import jsonify
import requests, os
from model import *
from app import *
from movielist import movies
from dotenv import load_dotenv

load_dotenv()

lst = movies

def loadDB(movielist):

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
    c_id = response["quotes"][0]["lines"][0]["characters"][0]["characterId"][-10:-1]
    c_name = response["quotes"][0]["lines"][0]["characters"][0]["character"]
    m_id = movie_id
    m_title = response["base"]["title"]
    q_id = response["quotes"][0]["id"][-9:]
    

loadDB(lst)
    # new_quote = Quote(quote_id=movie_quotes["quotes"][0]["id"][-9:], character_id=movie_quotes["quotes"][0]["lines"][0]["characters"][0], movie_id=data['movies.movie_id'])
    # db.session.add(new_quote)
    # db.session.commit()

