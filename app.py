from flask import Flask, request
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from seeds.model import *
from dotenv import load_dotenv
import requests, os

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

seeder = FlaskSeeder()
seeder.init_app(app, db)


# lst = movies

# @app.route("/quotes", methods=['POST'])
# def loadDB(movielist):

#     if request.method == "POST":
#         if request.is_json:

#         url = "https://imdb8.p.rapidapi.com/title/get-quotes"

#         KEY = os.getenv("RAPIDAPI_KEY")
#         HOST = os.getenv("RAPIDAPT_HOST")

#         headers = {
#             "x-rapidapi-key": KEY,
#             "x-rapidapi-host": HOST
#             }

#         # for movie in movielist:
#         movie_id = movielist[0]["id"][7:16]
#         querystring = {"tconst": movie_id}

#         response = requests.request("GET", url, headers=headers, params=querystring).json()

#         # querying response
#         c_id = response["quotes"][0]["lines"][0]["characters"][0]["characterId"][-10:-1]
#         c_name = response["quotes"][0]["lines"][0]["characters"][0]["character"]
#         m_id = movie_id
#         m_title = response["base"]["title"]
#         q_id = response["quotes"][0]["id"][-9:]

#         # adding response to database
#         new_character = Character(character_id=c_id, character_name=c_name)
#         new_movie = Movie(movie_id=m_id, movie_title=m_title)
#         # new_quote = Quote(quote_id=movie_quotes["quotes"][0]["id"][-9:], character_id=movie_quotes["quotes"][0]["lines"][0]["characters"][0], movie_id=data['movies.movie_id'])
#         db.session.add(new_character)
#         db.session.commit()

#         db.session.add(new_movie)
#         db.session.commit()

# loadDB(lst)


@app.route("/")
def hello():
    """Homepage"""

    return {"hello": "world"}

if __name__ == "__main__":

    app.run(debug=True)
