'''
Greetings My Fellow Travaller If you came this far you are welcome to join me in my journey to make a fully working polish TV for free here!

My aim is to simply make this website for people that want to watch Polish TV when they are abroad or simply dont want to pay for TV.

If you want to join go to my GitHub Repo @ https://github.com/JakubThe1st/PolishTV
'''

from flask import Flask
from flask import render_template
import webbrowser
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route("/TVP2")
def TVP2():
    return render_template("TVP2.html")

@app.route("/Polsat")
def Polsat():
    return render_template("Polsat.html")

@app.route("/TVT")
def TVT():
    return render_template("tvt.html")


app.run(host='0.0.0.0', port=8080)
