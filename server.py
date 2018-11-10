from flask import Flask, redirect, request, render_template, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

@app.route("/")
def homepage():
    """homepage of the site"""
    if session.get("name", 0) == 0:
        return render_template("homepage.html")
    else:
        return redirect("/top-melons")

@app.route("/get-name")
def get_name():
    form_name = request.args.get("name")
    session["name"] = form_name.title()
    return redirect("/top-melons")
"""forgot that I have to return a redirect method thing"""

""" Had to look up how to write beginning of route.
I wrote '@route ("/top-melons"):' originally
"""
@app.route("/top-melons")
def show_top_melons():
    """ shows most loved melons to user displaying name """
    melons = MOST_LOVED_MELONS
    if session.get("name", 0) == 0:
        return redirect("/")
    else:
        return render_template("top-melons.html",
                            melons=melons)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
