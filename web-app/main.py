from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import random,secrets
import json
from user import *

app = Flask(__name__)

app.secret_key = secrets.token_bytes(32)

@app.route("/")
def index():
    #initializes session
    initializeSession()

    resp = render_template("index.html")
    return resp

@app.route("/lost")
def loser():
    return "You are a fucking loser."

@app.route("/yes", methods=["POST"])
def optionyes():
    yesSession()

    if hasLost():
        return redirect(url_for('loser'))

    response_string = str(session['animal_metric']) + "#" + str(session['human_metric']) + "#" + session['game_prompt']
    return response_string

@app.route("/no", methods=["POST"])
def optionno():
    noSession()

    if hasLost():
        return redirect(url_for('loser'))

    response_string = str(session['animal_metric']) + "#" + str(session['human_metric']) + "#" + session['game_prompt']
    return response_string
    

# # Used to test locally
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)