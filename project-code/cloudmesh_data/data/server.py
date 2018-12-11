"""
Main module of the server file
"""

# 3rd party modules



# Create the application instance
import connexion as connexion
from flask import render_template

# Creating application instance
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
app.add_api("../etc/file.yml")
#app.add_api("../etc/user.yml")


# create a URL route in our application for "/"
@app.route("/file")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    app.run(debug=True)
