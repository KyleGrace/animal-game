import random
from flask import session

def initializeSession():
    session['animal_metric'] = 15
    session['human_metric'] = 15

    prompts = {
            "kill all animals": (-10, -9),
            "kill half of the animals": (-5, -4),
            "kill all humans": (5, -10),
            "require everyone to be vegan": (5, -5),
        }

    keys = prompts.keys()
    game_prompt = random.choice(list(keys))
    session['game_prompt'] = game_prompt
    session['prompts'] = prompts

    return session

def yesSession():
    game_prompt=session['game_prompt']
    prompts = session['prompts']
    human_change, animal_change = prompts[game_prompt]

    session['animal_metric'] += animal_change
    session['human_metric'] += human_change

    prompts.pop(game_prompt)

    keys = prompts.keys()
    newprompt = random.choice(list(keys))
    session['game_prompt'] = newprompt

    session['prompts'] = prompts

def noSession():
    game_prompt=session['game_prompt']
    prompts = session['prompts']
    human_change, animal_change = prompts[game_prompt]

    session['animal_metric'] += 0
    session['human_metric'] += 0

    prompts.pop(game_prompt)

    keys = prompts.keys()
    newprompt = random.choice(list(keys))
    session['game_prompt'] = newprompt

    session['prompts'] = prompts

def hasLost():
    return ((int(session['animal_metric'])<=0) or (int(session['human_metric'])<=0))