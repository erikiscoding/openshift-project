from flask import Flask, render_template, url_for, request

application = Flask(__name__)


@application.route("/")
@application.route("/home")
def home():
    return render_template('layout.html')


@application.route("/",methods=['GET','POST'])
@application.route("/home",methods=['GET','POST'])
def conversion():
    result = ""
    usd_amount = request.form['usd']
    chosen_currency = request.form['currencies']

    try:
        val = float(usd_amount)
    except ValueError:
        result = "Invalid input -- please try again!"
        return render_template("layout.html", result=result)

    if chosen_currency == "EUR":
        converted_usd = to_euro(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    if chosen_currency == "JPY":
        converted_usd = to_yen(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    if chosen_currency == "GBP":
        converted_usd = to_gbp(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)  
    if chosen_currency == "AUD":
        converted_usd = to_aud(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    if chosen_currency == "CAD":
        converted_usd = to_cad(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    if chosen_currency == "CHF":
        converted_usd = to_chf(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    if chosen_currency == "CNH":
        converted_usd = to_cnh(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    if chosen_currency == "SEK":
        converted_usd = to_sek(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    if chosen_currency == "NZD":
        converted_usd = to_nzd(usd_amount)
        result = usd_amount + " USD is equal to " + str(converted_usd) + " " + str(chosen_currency)
        return render_template("layout.html", result=result)
    


"""
Euro (EUR)
Japanese yen (JPY)
Pound sterling (GBP)
Australian dollar (AUD)
Canadian dollar (CAD)
Swiss franc (CHF)
Chinese renminbi (CNH)
Swedish krona (SEK)
New Zealand dollar (NZD)1
"""

def to_euro(usd):
    usd = float(usd)
    usd = usd * 0.83
    usd = round(usd,2)
    return usd


def to_yen(usd):
    usd = float(usd)
    usd = usd * 104.01
    usd = round(usd,2)
    return usd


def to_gbp(usd):
    usd = float(usd)
    usd = usd * 0.76
    usd = round(usd,2)
    return usd


def to_aud(usd):
    usd = float(usd)
    usd = usd * 1.33
    usd = round(usd,2)
    return usd


def to_cad(usd):
    usd = float(usd)
    usd = usd * 1.28
    usd = round(usd,2)
    return usd


def to_chf(usd):
    usd = float(usd)
    usd = usd * 0.89
    usd = round(usd,2)
    return usd


def to_cnh(usd):
    usd = float(usd)
    usd = usd * 6.55
    usd = round(usd,2)
    return usd


def to_sek(usd):
    usd = float(usd)
    usd = usd * 8.46
    usd = round(usd,2)
    return usd


def to_nzd(usd):
    usd = float(usd)
    usd = usd * 1.41
    usd = round(usd,2)
    return usd


if __name__ == "__main__":
    application.run()
