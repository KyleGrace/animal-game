import time
import sys
import random

#########################
#     Helper Functions  #
#########################


def delay_print(s,delay):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def addMetrics(currTup, choiceTup):
    return (currTup[0]+choiceTup[0],
            currTup[1]+choiceTup[1],
            currTup[2]+choiceTup[2],
            currTup[3]+choiceTup[3])

def win():
    delay_print("\nYou have won...",0.3)

def lose():
    delay_print("\nYou have lost...",0.3)

# Structured as
# OPTION : (Animal, Wealth, Peace, Humans)
prompts = {
    "Kill all dogs?"                    : (-10,2,-1,-1),
    "Kill all cats?"                    : (-10,2,-1,-1),
    "Give subsidy for owning pets?"     : (5,-2,0,1),
}

metrics = (10,10,10,10)
maxMetrics = (20,20,20,20)

playing = True
days = 0
while(playing):
    days += 1
    print(f'|------------------ day {days} ---------------------|')
    print(f'Current Levels:\nAnimals {metrics[0]}   Wealth {metrics[1]}   Peace {metrics[2]}   Humans {metrics[3]}\n')

    if not prompts:
        win()
        playing = False
        break
    keys = prompts.keys()
    currKey = random.choice(list(keys))
    delay_print(currKey,0.1)
    
    choice = input("Yes or No? ")

    if (choice[0].lower()) == 'y':
        metrics = addMetrics(metrics,prompts[currKey])

        for met in metrics:
            if met <= 0:
                delay_print(f'\nLevels:\nAnimals {metrics[0]}   Wealth {metrics[1]}   Peace {metrics[2]}   Humans {metrics[3]}\n',0.05)
                lose()
                playing=False
    
    del prompts[currKey]
