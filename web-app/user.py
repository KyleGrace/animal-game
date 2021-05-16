import random
from flask import session
from prompts import *

import time

def initializeSession():
    session.clear()
    # must be ~<20 or the cookies grow too large,
    # requires rework of prompts storage in cookies to grow bigger than 20
    numdays = 10 # Update this to determine how many prompts they must pass to win
    session['animal_metric'] = 10
    session['human_metric'] = 10

    prompts = starterPrompts

    # Shortening it to 11 prompts to help the cookies stay small
    smallerPrompts = random.sample(list(prompts),(numdays+1))
    newprompts = {}
    for prompt in smallerPrompts:
        newprompts[prompt] = starterPrompts[prompt]

    prompts=newprompts

    keys = prompts.keys()
    game_prompt = random.choice(list(keys))
    image = prompts[game_prompt][2]
    session['game_prompt'] = game_prompt
    session['prompts'] = prompts
    session['image'] = image
    session['remain'] = numdays

    return session



def yesSession():
    game_prompt = session['game_prompt']
    prompts = session['prompts']

    yesChange = prompts[game_prompt][0]
    image = prompts[game_prompt][2]
    animal_change, human_change = yesChange

    session['animal_metric'] += animal_change
    session['human_metric'] += human_change
    session['remain'] = session['remain'] - 1

    prompts.pop(game_prompt)

    if not prompts:
        return 

    keys = prompts.keys()
    newprompt = random.choice(list(keys))
    image = prompts[newprompt][2]
    
    session['image'] = image
    session['game_prompt'] = newprompt
    session['prompts'] = prompts

    session.modified = True

def noSession():
    game_prompt = session['game_prompt']
    prompts = session['prompts']

    noChange = prompts[game_prompt][1]
    animal_change, human_change = noChange

    session['animal_metric'] += animal_change
    session['human_metric'] += human_change
    session['remain'] = session['remain'] - 1

    prompts.pop(game_prompt)

    if not prompts:
        return 

    keys = prompts.keys()
    newprompt = random.choice(list(keys))
    image = prompts[newprompt][2]

    session['image'] = image
    session['game_prompt'] = newprompt
    session['prompts'] = prompts

    session.modified = True


def hasLostAnimal():
    return int(session['animal_metric'])<=0

def hasLostHuman():
    return int(session['human_metric'])<=0

def isEmpty():
    return (session['remain']==0) or (not session['prompts'])

