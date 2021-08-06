import requests, os
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

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

loadDB(lst)
