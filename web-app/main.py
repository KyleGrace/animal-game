from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

votes = 0

animal_metric = 15
human_metric = 15

prompts = {
    "kill all animals": (-10, -9),
    "kill half of the animals": (-5, -4),
    "kill all humans": (5, -10),
    "require everyone to be vegan": (5, -5),
}

keys = prompts.keys()
game_prompt = random.choice(list(keys))
animal_change, human_change = prompts[game_prompt]
del prompts[game_prompt]

@app.route("/")
def index():
    return render_template("index.html", animal_metric = animal_metric, human_metric = human_metric, game_prompt=game_prompt)

@app.route("/yes", methods=["POST"])
def optionyes():
    global animal_metric
    global human_metric
    global game_prompt
    global prompts
    global animal_change
    global human_change

    animal_metric += animal_change
    human_metric += human_change

    game_prompt = random.choice(list(keys))
    animal_change, human_change = prompts[game_prompt]
    del prompts[game_prompt]

    response_string = str(animal_metric) + "#" + str(human_metric) + "#" + game_prompt
    return response_string

@app.route("/no", methods=["POST"])
def optionno():
    global animal_metric
    global human_metric
    global game_prompt
    global prompts
    global animal_change
    global human_change

    animal_metric += 0
    human_metric += 0

    game_prompt = random.choice(list(keys))
    animal_change, human_change = prompts[game_prompt]
    del prompts[game_prompt]

    response_string = str(animal_metric) + "#" + str(human_metric) + "#" + game_prompt
    return response_string
    

# # Used to test locally
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)