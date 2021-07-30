
from flask_debugtoolbar import DebugToolbarExtension
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    flash,
    session,
    url_for,
    jsonify,
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_paginate import Pagination, get_page_args
from jinja2 import StrictUndefined
from sqlalchemy import func, asc, desc

from model import *

app = Flask(__name__)
CORS(app)

app.jinja_env.undefined = StrictUndefined

@app.route("/", methods=["POST", "GET"])
def index():
    """Homepage"""

    return render_template("index.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.autoreload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5432, host="0.0.0.0")
