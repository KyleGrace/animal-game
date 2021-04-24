####################
# PROMPTS FOR GAME #
####################
import random

starterPrompts = {                             # Yes: Effect on Animals, Humans; No: Effect on Animals, Humans
            """The population is growing! To expand
                your kingdom and provide resources to
                feed everyone, your advisor has suggested
                to clear out a forest to make land for
                agriculture. Accept?""":                         [(-3, 2), (1, -4),'/static/cruelty.jpg'],
            """Medical technology is expanding. A representative
                from the science society, Darles Charwin, has
                asked for your permission to begin the testing
                and development of a new research project. Grant
                permission?""":                                  [(-1, 5), (0, -5),'/static/cruelty.jpg'],
            """You've been visited by the evil twin of the
                artist Catherine Chalmer, who detests
                all insects and wants to use ddt pesticide
                to remove pests so that farmers
                will be happier. Allow ddt pesticide?""":        [(-5, 3), (0, -3),'/static/cruelty.jpg'],
            """Space-travel technology is being developed,
                and to test out your kingdom's newest
                rocket, your advisors have suggested to
                send a single chimp into space! It'll
                be good for the press! Do you accept?""":        [(-1, 5), (0, -1),'/static/cruelty.jpg'],
            """The neighboring kingdom's shaman, Carcus
                Moates, visits you and asks you to take a trip
                with him into the Underworld. You're curious
                about the animal spirits that live there,
                but you're also concerned about your public
                image and looking like an idiot. Take a trip
                into the Underworld?""":                         [(2, -1), (0, 0),'/static/cruelty.jpg'],
            """Your pet elephant has died naturally of old
                age. Now there's a dead elephant in your room,
                and artist Hamien Dirst wants to keep it for
                an art project. Allow Dirst to keep the
                elephant?""":                                    [(random.randint(0,5), random.randint(-5,5)), (0, 0),'/static/cruelty.jpg'],
            """You're visited by a mysterious creature named
                Helena, who offers you a blender with a live
                goldfish in it. Turn on the blender?""":         [(0, -1), (0, 0),'/static/cruelty.jpg'],
            """Your foreign embassador has informed you of the
                new "life release" trend that's viral across
                Japan! He's super excited to release
                animals, and has asked for your support.
                Allow your kingdom to practice
                life-releasing?""":                              [(-3, 2), (0, -1),'/static/cruelty.jpg'],
            """There's a elephant artist that has been gaining
                popularity. Would you like to recognize their
                work by admitting them to the national
                art collection?""":                              [(2, 0), (-1, 1),'/static/cruelty.jpg'],
            """You biggest energy company, PB, accidentally
                spilled oil into the ocean. Your coastal
                advisor Bacqueline Jishop suggests a
                million dollar initiative to clean up
                the oil spill. Would you like to
                raise the taxes for this intiative?""":          [(1, -6), (-5, 0),'/static/cruelty.jpg'],
            """One of your advisors, Udge Ferica, wants to
                start a nutrition program to encourage vegan
                meals in schools. Many parents are against this,
                but Udge believes its a good idea. Would you
                like to provide funding for Udge's program?""":  [(6, -3), (-1, 1),'/static/cruelty.jpg'],
            """The Earl of Claremont, Ill Banthes, has proposed
                animal studies as a new primary school subject. 
                Will you implement this new subject?""":          [(3,0),(-1,0),'/static/cruelty.jpg'],
            """You have been visited by Hilliam Wogarth. He has
                recently published a paper arguing that violence
                towards animals, conditions humans towards
                violence. He argues that you make animal
                cruelty punishable by life in prison. Will you
                do so?""":                                        [(5,2),(-2,-1),'/static/cruelty.jpg'],
            """A small cat has snuck into your chamber, will you
                let them stay?""":                                [(0,0),(0,0),'/static/izzyround.jpg'],
            """Izzy, representative of the feline district, has
                come asking for support in providing more tuna
                to their community. Will you provide the tuna?""":[(3,-1),(-2,0),'/static/standizzy.jpeg'],
}