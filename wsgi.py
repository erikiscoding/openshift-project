from flask import Flask, render_template, url_for, request

application = Flask(__name__)


@application.route("/")
@application.route("/home")
def home():
    return render_template('layout.html')


@application.route("/",methods=['GET','POST'])
@application.route("/home",methods=['GET','POST'])
def conversion():
    #submission = request.args.get('currencies')
    submission = request.form['currencies']
    return str(submission)





if __name__ == "__main__":
    application.run()
