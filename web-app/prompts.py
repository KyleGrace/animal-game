####################
# PROMPTS FOR GAME #
####################
import random

starterPrompts = {                             # Yes: Effect on Animals, Humans; No: Effect on Animals, Humans
            """The population is growing! To expand
                your kingdom and provide resources to
                feed everyone, your advisor has suggested
                to clear out a forest to make land for
                agriculture. Accept?""":                         [(-3, 2), (1, -4),'/static/reeds.png'],
            """Medical technology is expanding. A representative
                from the science society, Darles Charwin, has
                asked for your permission to begin the testing
                and development of a new research project. Grant
                permission?""":                                  [(-1, 5), (0, -5),'/static/darwin.jpg'],
            """You've been visited by the evil twin of the
                artist Catherine Chalmer, who detests
                all insects and wants to use ddt pesticide
                to remove pests so that farmers
                will be happier. Allow ddt pesticide?""":        [(-5, 3), (0, -3),'/static/ants.jpeg'],
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
                into the Underworld?""":                         [(2, -1), (0, 0),'/static/coates.png'],
            """Your pet elephant has died naturally of old
                age. Now there's a dead elephant in your room,
                and artist Hamien Dirst wants to keep it for
                an art project. Allow Dirst to keep the
                elephant?""":                                    [(random.randint(0,5), random.randint(-5,5)), (0, 0),'/static/hirst.jpg'],
            """You're visited by a mysterious creature named
                Helena, who offers you a blender with a live
                goldfish in it. Turn on the blender?""":         [(0, -1), (0, 0),'/static/helena.jpg'],
            """Your foreign embassador has informed you of the
                new "life release" trend that's viral across
                Japan! He's super excited to release
                animals, and has asked for your support.
                Allow your kingdom to practice
                life-releasing?""":                              [(-3, 2), (0, -1),'/static/release.png'],
            """There's a elephant artist that has been gaining
                popularity. Would you like to recognize their
                work by admitting them to the national
                art collection?""":                              [(2, 0), (-1, 1),'/static/suda.jpg'],
            """You biggest energy company, PB, accidentally
                spilled oil into the ocean. Your coastal
                advisor Bacqueline Jishop suggests a
                million dollar initiative to clean up
                the oil spill. Would you like to
                raise the taxes for this intiative?""":          [(1, -6), (-5, 0),'/static/bishop.jpg'],
            """One of your advisors, Udge Ferica, wants to
                start a nutrition program to encourage vegan
                meals in schools. Many parents are against this,
                but Udge believes its a good idea. Would you
                like to provide funding for Udge's program?""":  [(6, -3), (-1, 1),'/static/cruelty.jpg'],
            """The Earl of Claremont, Ill Banthes, has proposed
                animal studies as a new primary school subject. 
                Will you implement this new subject?""":          [(3,0),(-1,0),'/static/bill.png'],
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
            """Your space agency has plans to build a large 
               telescope in the center of the national forest.
               The telescope will be used to search for aliens.
               Ned Chiang has approached you in opposition of 
               this project. He believes it will destroy animal
               habitats and widen the divide between species.
               Will you cancel the project.""":                   [(4,-2),(-4,3),'/static/telescope.jpg'],
            """Bnæbjörnsdóttir and Milson have approached you 
               as representatives of the Old York Animal
               Advocacy Board. They propose new legislation
               requiring all house pets to have their own 
               dedicated space within a home. Will you pass
               this legislation?""":                              [(4,-3),(-1,0),'/static/worlding.png'],
            """You meet with your friend from secondary 
               school, Bron Roglio, for coffee. In passing he 
               mentions that you should bring on an animal 
               advisor. Will you do so?""":                       [(3,-1),(-3,0),'/static/broglio.png'],
            """Renowned artist Batherine Chell has asked to
               perform at the royal ball next month. She says
               she will need 100 squids for the performance. 
               Will you schedule her to perform?""":              [(3,-5),(0,1),'/static/bell.png'],
            """Logistics advisor, Kucy Limbell, enters your 
               chamber with a box of rats. She introduces them
               as REA, the Rat Empowered Assistant. She suggests
               you allow REA to help you with all kinds of
               things, from creating palace artwork to 
               designing the streets of new cities. Will you 
               employ the rats?""":                               [(2,-5),(-1,3),'/static/rats.png'],
            """While hunting rabbits, a royal hunter has brought
               a painting they found in a patch of tall grass.
               You cannot make out the inscription on the back
               other than G__rg_ _tub_s. You like it. Will you
               hang it in your palace?""":                        [(1,1),(-1,-1),'/static/lionhorse.jpg'],
            """The Reverend of Nano Bio Info Cogno has come to 
               you demanding that their religion become officially
               recognized by the state. Will you make a public
               announcement of your support?""":                  [(-3,-2),(2,2),'/static/bio.png']             
}