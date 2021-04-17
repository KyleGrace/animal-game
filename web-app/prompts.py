####################
# PROMPTS FOR GAME #
####################

starterPrompts = {                             # Yes: Effect on Animals, Humans; No: Effect on Animals, Humans
            "kill all animals":                                 [(-10, -9), (0, 0)],
            "kill half of the animals":                         [(-5, -4), (0, 0)],
            "kill all humans":                                  [(5, -10), (0, 0)],
            "require everyone to be vegan":                     [(5, -5), (0,0)],
            """Pass legislation to allow all housepets 
                to vote in elections.""" :                      [(3,0), (0, 0)],
            """The population is growing! To expand
                your kingdom and provide resources to
                feed everyone, your advisor has suggested
                to clear out a forest to make land for
                agriculture.""":                                 [(-3, 2),(1, -4)]
}