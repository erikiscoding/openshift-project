from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    your_word = str(input("Enter what word you really really like and enjoy greatly: "))

    your_word = your_word.upper()

    print("Here is your word but even better: " + your_word)
    print("bye bye now")

if __name__ == "__main__":
    application.debug = True
    application.run()
