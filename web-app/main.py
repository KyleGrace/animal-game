from flask import Flask, render_template
import random

app = Flask(__name__)

votes = 0

game_metric=[10,10]

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
    return render_template("index.html", votes=votes, game_metric=game_metric,game_prompt=game_prompt)

@app.route("/up", methods=["POST"])
def upvote():
    global votes
    votes = votes + 1
    return str(votes)

@app.route("/down", methods=["POST"])
def downvote():
    global votes
    if votes >= 1:
        votes = votes - 1
    return str(votes)



@app.route("/yes", methods=["POST"])
def optionyes():
    global game_metric
    # global animal_metric
    # global human_metric
    global game_prompt
    global prompts
    global animal_change
    global human_change

    # animal_change, human_change = prompts[game_prompt]
    game_metric[0] += animal_change
    game_metric[1] += human_change
    # animal_metric += animal_change
    # human_metric += human_change
    # del prompts[game_prompt]

    game_prompt = random.choice(list(keys))
    animal_change, human_change = prompts[game_prompt]
    del prompts[game_prompt]

    return str(game_metric)

# @app.route("/no", methods=["POST"])
# def optionno():
    

# # Used to test locally
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)