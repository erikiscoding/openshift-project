from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Will I ever figure out how to develop and deploy an OpenShift application?"

if __name__ == "__main__":
    application.run()
