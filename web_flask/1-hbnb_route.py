#!/usr/bin/python3
"""Hello Flask!"""
from flask import Flask


web_app = Flask(__name__)


# strict_slashes=False for ignoring / when accessing route
@web_app.route("/", strict_slashes=False)
def home_page():
    "define home page"
    return ("Hello HBNB!")


@web_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """define hbnb page"""
    return ("HBNB")


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000, debug=True)
