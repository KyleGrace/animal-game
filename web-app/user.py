import random
from flask import session
from prompts import *

def initializeSession():
    session['animal_metric'] = 15
    session['human_metric'] = 15

    prompts = starterPrompts

    keys = prompts.keys()
    game_prompt = random.choice(list(keys))
    session['game_prompt'] = game_prompt
    session['prompts'] = prompts

    return session

def yesSession():
    game_prompt=session['game_prompt']
    prompts = session['prompts']
    animal_change,human_change = prompts[game_prompt]

    session['animal_metric'] += animal_change
    session['human_metric'] += human_change

    prompts.pop(game_prompt)

    if not prompts:
        return 

    keys = prompts.keys()
    newprompt = random.choice(list(keys))
    session['game_prompt'] = newprompt

    session['prompts'] = prompts

def noSession():
    game_prompt=session['game_prompt']
    prompts = session['prompts']
    animal_change,human_change = prompts[game_prompt]

    session['animal_metric'] += 0
    session['human_metric'] += 0

    prompts.pop(game_prompt)

    if not prompts:
        return 

    keys = prompts.keys()
    newprompt = random.choice(list(keys))
    session['game_prompt'] = newprompt

    session['prompts'] = prompts


def hasLost():
    return ((int(session['animal_metric'])<=0) or (int(session['human_metric'])<=0))

def isEmpty():
    return not session['prompts']

