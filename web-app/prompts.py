####################
# PROMPTS FOR GAME #
####################
import random

starterPrompts = {                             # Yes: Effect on Animals, Humans; No: Effect on Animals, Humans
            """The population is growing! To expand
                your kingdom and provide resources to
                feed everyone, your advisor has suggested
                to clear out a forest to make land for
                agriculture.""":                                 [(-3, 2), (1, -4)],
            """Medical technology is expanding. A representative
                from the science society, Darles Charwin, has
                asked for your permission to begin the testing
                and development of a new research project.""":   [(-1, 5), (0, -5)],
            """You've been visited by the evil twin of the
                artist Catherine Chalmer, who detests
                all insects and wants to use ddt pesticide
                to remove pests so that farmers
                will be happier.""":                             [(-5, 3), (0, -3)],
            """Space-travel technology is being developed,
                and to test out your kingdom's newest
                rocket, your advisors have suggested to
                send a single chimp into space! It'll
                be good for the press!""":                       [(-1, 5), (0, -1)],
            """The neighboring kingdom's shaman, Carcus
                Moates, visits you and asks you to take a trip
                with him into the Underworld. You're curious
                about the animal spirits that live there,
                but you're also concerned about your public
                image and looking like an idiot.""":             [(2, -1), (0, 0)],
            """Your pet elephant has died naturally of old
                age. Now there's a dead elephant in your room,
                and artist Hamien Dirst wants to keep it for
                an art project.""":                              [(random.randint(0,5), random.randint(-5,5)), (0, 0)],
            """You're visited by a mysterious creature named
                Helena, who offers you a blender with a live
                goldfish in it. Turn on the blender?""":         [(0, -1), (0, 0)],
            """Your foreign embassador has informed you of the
                new "life release" trend that's viral across
                Japan! He's super excited to release
                animals, and has asked for your support.""":      [(-3, 2), (0, -1)],
}