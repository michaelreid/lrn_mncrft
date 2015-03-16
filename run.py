#
# Learn Minecraft: Landing Page
#
# using Flask app
#
# March 2015
#


# import from Flask and setup the app
from flask import Flask, render_template
app = Flask(__name__)


# @app.template_filter()
# def datetimefilter(value, format='%Y/%m/%d %H:%M'):
#     """Convert a datetime to a different format."""
#     return value.strftime(format)

# setup up root view
@app.route("/")
def landing():
    return render_template('index.html')

# setup up root view
@app.route("/about")
def about():
    return render_template('about.html')

# define __main__ function so can call from command line
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8085)
