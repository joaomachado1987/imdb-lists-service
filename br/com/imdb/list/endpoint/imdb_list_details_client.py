from flask import (
    Flask,
    render_template
)

from br.com.imdb.list.service.imdb_service import retrive_movie_details_by_title

import json

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/movie/title/<title>/year/<year>')
def home(title, year):
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """

    return retrive_movie_details_by_title(title, year);

if __name__ == '__main__':
    app.run(debug=True)