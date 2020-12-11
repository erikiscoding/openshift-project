from flask import Flask, render_template, url_for
application = Flask(__name__)


@application.route("/")
@application.route("/home")
def home():
    return render_template('layout.html')


if __name__ == "__main__":
    application.run()
