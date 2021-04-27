from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_session import Session
from flask_cors import CORS, cross_origin
import random,secrets
import json
from user import *

app = Flask(__name__,static_url_path='/static')

app.secret_key = secrets.token_bytes(32)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
CORS(app)
# app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

@app.route("/")
@cross_origin(supports_credentials=True)
def index():
    resp = render_template('landing.html')
    return resp

@app.route("/game")
@cross_origin(supports_credentials=True)
def game():
    #initializes session
    initializeSession()

    resp = render_template("game.html")
    return resp

@app.route("/lostanimal")
@cross_origin(supports_credentials=True)
def loser_animal():
    resp = render_template("lostAnimal.html")
    return resp

@app.route("/losthuman")
@cross_origin(supports_credentials=True)
def loser_human():
    resp = render_template("lostHuman.html")
    return resp

@app.route("/win")
@cross_origin(supports_credentials=True)
def winner():
    resp = render_template("win.html")
    return resp

@app.route("/yes", methods=["POST"])
@cross_origin(supports_credentials=True)
def optionyes():
    yesSession()

    if hasLostAnimal():
        return redirect(url_for('loser_animal'))
    elif hasLostHuman():
        return redirect(url_for('loser_human'))
    elif isEmpty():
        return redirect(url_for('winner'))

    response_string = (str(session['animal_metric']) + "#" 
                    + str(session['human_metric']) + "#" 
                    + session['game_prompt'] + "#" 
                    + session['image'])
    return response_string

@app.route("/no", methods=["POST"])
@cross_origin(supports_credentials=True)
def optionno():
    noSession()

    if hasLostAnimal():
        return redirect(url_for('loser_animal'))
    elif hasLostHuman():
        return redirect(url_for('loser_human'))
    elif isEmpty():
        return redirect(url_for('winner'))

    response_string = (str(session['animal_metric']) + "#" 
                    + str(session['human_metric']) + "#" 
                    + session['game_prompt'] + "#" 
                    + session['image'])
    return response_string
    

# # Used to test locally
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)