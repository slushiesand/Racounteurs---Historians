
init python:
    import random

    itemsFound = 0
    manuscript = 0

    time = ["morning", "afternoon", "evening", "night"]
    timeCounter = 0
    daysLeft = 3

    location = ["Hallway", "Study", "Kitchen", "Bedroom", "Storage", "Living Room", "Dining Room", "Laundry Room", "Guest Bedroom", "Computer Room", "Bathroom", "Library"]

    def locationDetermine(location):

        
        if location == "Hallway":
            renpy.jump("hall")
        elif location == "Study":
            renpy.jump("study")
        elif location == "Kitchen":
            renpy.jump("kitchen")
        elif location == "Bedroom":
            renpy.jump("bedroom")
        elif location == "Storage":
            renpy.jump("storage")
        elif location == "Living Room":
            renpy.jump("living")
        elif location == "Dining Room":
            renpy.jump("dining")
        elif location == "Laundry Room":
            renpy.jump("laundry")
        elif location == "Guest Bedroom":
            renpy.jump("guest")
        elif location == "Computer Room":
            renpy.jump("computer")
        elif location == "Bathroom":
            renpy.jump("bath")
        elif location == "Library":
            renpy.jump("library")
        

        #yandev ahh code. this is what happens when you havent coded in python for like 2 years
        

define ki = Character("King", color = "#FDCA62")
define ka = Character("Kazan", color="#A6E1FE")

define qu = Character("Queen", color="#5077CA")
define fu = Character("???", color="#FFF")
define s = Character("Sister", color="#FFF")
define m = Character("Mother", color="#FFF")

image black = "#000"

# The game starts here.

label start:

    scene black

    $ combo = random.randint(1000, 9999)
    $ unavailable = []

    #ok btw all the text is prolly gonna be copy and pasted from the google docs i am NOT writing for 8 hours again that was hell

    ki """
    Have you ever heard a folktale? 

    Hehe… in this world made of atoms, exploding at the end of the universe? Perhaps imagination is the only thing you can cling onto.

    I like stories, too. So that's why…
    """


    scene cg inn tired
    with Fade(1.0, 0, 1.0)
    play music "audio/Symphony no. 5 in Cm, Op. 67 - II. Andante con moto (For Recorder Ensemble - Papalin).mp3"

    ki "... Ugh! I have no inspiration!"
    qu "It's alright, King. We had a good session today. The people seemed to especially enjoy our telling of the Ouroboros Angel."
    ki "Of course, of course. I'm glad! That one’s really underrated! But everyone in the world has probably heard it already.\nWe need… something NEW!"
    qu "Hmm. No need to be hasty. I think you're getting restless again.\nPerhaps you ought to take a walk in the forest. Nature is always an inspiring sight. And if not, at least you'll clear your mind."
    
    "Queen… always trying to comfort me, even if he doesn't smile much himself… and always more patient about life than I."
    
    show cg inn idea
    with vpunch

    ki "YES! That's what I'll do! Thank you, my dear partner! I'll come back with results, surely!"
    qu "Haha… alright, alright. Make sure to wear your winter coat; It's cold outside."

    scene black
    with fade

    """
    I quickly gather the things I need for any inspiration adventure: A leather notebook, a belt of stationary, and a small empty bag for any goodies I find along the way, along with general survival supplies just in case I need it.
    
    Queen and I have been doing this kind of thing for a long time. We’re a two-man theatre, gathering special stories from all around the world for those who wish to hear our gallant tales. 
    
    I do most of the writing and information gathering, while Queen composes music and choreographs. It's a wonderful life. I wouldn't have it any other way!
    
    My partner says goodbye as I rush through the bed-and-breakfast door. The sun is threatening to set soon, so I should finish my walk quickly.
    """
    ki "Although, the moon has always treated me better."

    scene bg forest1
    show king neutral at right
    with fade
    stop music fadeout 1.0
    

    """
    I reach the forest on the edge of town. Queen and I had walked through it when we first came, but the road on which we walked is no longer visible.
    
    In fact, everything seems to be flattened to one single surface of pure snow, with trees serving as the only points of interest on this coordinate plane.
    """
    show king think at right
    "Nevertheless, there's probably something interesting out there, so I continue on."
    

    scene bg forest2
    show king neutral sad at right
    with wipeleft

    """
    … Perhaps I was wrong. There seems to only be snow and branchless trees out here, along with a never ending whirlwind of snow. Normally, artists covet blank canvases, but if you have nothing to illustrate, they serve no purpose. 
    
    Worse yet: it's getting late! I promised I would have something when I get back, but I have absolutely nothing on my mind! 
    
    … Hang on, which way IS back? I don't see my footprints anywhere. Did the snow fill in my footsteps? 
   
    That's… not great, but in a pinch, I suppose I could just teleport back. 
    
    Still, I must move forward. 

    """

    show bg forest3
    with fade

    
    "It gets darker still. My stamina wanes as the moon tickles the horizon. Once again, my greed has overtaken my instinct for safety."

    show king neutral happy at right
    """
    But in the distance, I see a saving grace: a cabin! 

    It is unlit, but well maintained. Perhaps the owner isn't home?

    I briskly walk to the cabin and knock on the door.
    """

    scene bg window
    with dissolve
    """
    …
    Nothing. I guess I'll have to do this the hard way, then. 
    """
    menu:
        "Lockpick through the door, or break through the window?"

        "Break through the window.":
            $ pass

        "Break through the window.":
            $ pass

    "Hehe, the answer is obvious! Break through the window!!"

    scene black
    with vpunch

    """
    I barrel my body through the window.

    My body rolls over a dining table as glass spills over the floor.

    Eventually, I land on the shadowy floor of a kitchen, glass scratching at the inner lining of my coat.

    """

    show king back sad

    ki "Oof..."

    """
    Still, I should be fine.

    More importantly, no alarm systems go off. I might not die for trespassing!
    """

    show king back happy

    """
    I leave some money on the table as a gesture of good will, and scuttle to find somewhere to hide for the night. 

    If there is someone in the house, I should find somewhere secluded to sleep so they don't find me. 
    
    A blanket closet may be a good candidate.
    """

    #ideally walking sound goes here
    show king think
    ki "... Ah-hah."
    "Just what I wanted."
    ki "Alright, get comfy, me. It's going to be a long night."
    hide king
    with fade

    pause 3.0
    """
    My eyes flutter open as the sun peeks through the ventilation gaps in the door. Not the worst sleep I've had, but definitely could have a little more leg room.

    I cautiously leave my closet and head downstairs to the kitchen.
    """

    scene bg kitchen
    with fade
    "It's hard to tell if the scene has been touched since last night, namely because..."
    show bg snow
    with dissolve
    "There's an avalanche of snow coming through the window!"
    show bg snow2
    with vpunch
    "Truthfully, the whole cabin is buried in snow!"
    show bg kitchen
    show king neutral happy
    with dissolve
    ki "Oh my! How unfortunate! Or rather… how fortunate!"
    show king shrug
    with vpunch
    ki "A writer trapped in an empty cabin for who-knows-how-long? That's just SCREAMING for a good story to be found!"
    show king neutral happy
    ki "O’ thank you, chaotic particles that have collided in such a way to grant this luck to me!"
    show king neutral
    ki "Let me write something to Queen to let him know that I’m okay, then I can begin my expedition."

    label loop:
        while daysLeft > 0:
            play music "audio/Grand Dark Waltz Allegretto.mp3" if_changed fadein 1.0
            scene bg kitchen
            show king neutral
            with wipeleft

            if timeCounter == 0:
                if daysLeft == 3:
                    show king think
                    ki "I suppose I should eat something. Let's see what's in my bag…"
                    show king neutral happy
                    ki "Some granola bars and a bottle of water. Surprised this didn't freeze over. Sure, that'll do for today. Let's not rob the fridge just yet!"
                elif daysLeft == 2:
                    ki "I said I wasn't gonna rob the fridge yesterday, but that doesn't account for today. Hopefully, none of this is expired…"
                    show king think
                    ki "Huh. The fridge seems to be working. Did a backup generator go off? I should still go with something with a long shelf-life to be safe, though."
                    show king neutral happy
                    ki "Let’s see… a jar of preserved fruit jelly. I saw some bread on the counter, as well. Hehe, a good breakfast for me today!"
                else: 
                    ki "The fridge served me well last time. Let's see…"
                    show king back sad
                    ki "... Some pancakes seem to have appeared overnight. They’re a bit charred at the edges, but charming enough."
                    menu:
                        "Should I eat them?"
                    
                        "Yes!!!!!!!!!!!!!":
                            $ pass
                        "No.":
                            $ pass
                
                    ki "Luckily, I still have some jam from yesterday."
                    show king back annoy
                    ki "Now that I think about it… I should probably pay for this too…"
            elif timeCounter == 4:
                $ daysLeft -= 1
                $ timeCounter = 0
                jump loop
            
                    
            python:
                #ok this is going to be incredibly inefficient but i dont feel like devoting brainpower to making this efficient
                alreadyChosen = []

                loc1 = random.choice(location)
                while loc1 in unavailable:
                    loc1 = random.choice(location)
                alreadyChosen.append(loc1)

                if len(unavailable) >= 11:
                    loc2 = "Unavailable"
                else:
                    loc2 = random.choice(location)
                    while loc2 in unavailable or loc2 in alreadyChosen:
                        loc2 = random.choice(location)
                    alreadyChosen.append(loc2)

                if len(unavailable) >= 10:
                    loc3 = "Unavailable"
                else: 
                    loc3 = random.choice(location)
                    while loc3 in unavailable or loc3 in alreadyChosen:
                        loc3 = random.choice(location)
                    alreadyChosen.append(loc3)

                if len(unavailable) >= 9:
                    loc4 = "Unavailable"
                else: 
                    loc4 = random.choice(location)
                    while loc4 in unavailable or loc4 in alreadyChosen:
                        loc4 = random.choice(location)
                    alreadyChosen.append(loc4)
                

            menu:
                "It looks like the snow will melt in [daysLeft] days. It's currently [time[timeCounter]]. Where should I go?"
            
                "[ loc1 ]":
                    $ timeCounter += 1
                    $ unavailable.append(loc1)
                    $ locationDetermine(loc1)
                "[ loc2 ]":
                    $ timeCounter += 1
                    $ unavailable.append(loc2)
                    $ locationDetermine(loc2)
                "[ loc3 ]":
                    $ timeCounter += 1
                    $ unavailable.append(loc3)
                    $ locationDetermine(loc3)
                "[ loc4 ]":
                    $ timeCounter += 1
                    $ unavailable.append(loc4)
                    $ locationDetermine(loc4)

                "Basement":
                    $ timeCounter += 1
                    jump basement
    
        
            
    #loop end here
    # dev menu: shirt + d; console: shift + o
    scene black:
            alpha 1.0
    with fade

    "In the end, I left the cabin after three days, no homeowner in sight. As for the story I made…"

    if itemsFound == 1:
        "I actually had to take lots of creative liberties. I didn't gather as much information as I thought. People didn't seem as engaged as I had hoped. Maybe it's a good filter story instead…"
    elif itemsFound == 2:
        "The story ended up quite imaginative. People seemed interested, but it didn't hit as hard as I would have liked. I suppose it was as truthful as any good fairytale."
    elif itemsFound == 3:
        "The story was a big hit, although I had to fill in some gaps here and there. I think I caught a few sniffling at the darkest pitfalls in the story, though no one outright cried."
    else: 
        "The story was a great hit! People seemed to find its more grounded and realistic nature an interesting and engaging departure from our regular material, and so listened even deeper than usual! "
    "I think this story is certainly a good runner for our staple catalog, except…"

    show bg forest3
    with fade
    """
    When I went back to that cabin with Queen some time later, it was totally abandoned. The power wasn't on, the food in the fridge had long expired, and the inside was ravaged from the wind flowing through the still-broken window.
    
    I found a door in the basement with an alphabetic lock. With some force, I successfully broke in, but that room, too, was abandoned.
    
    The only thing cluing to someone being there was a glass pocketwatch with a broken face.
    
    Ending: Back in Time. (3/4)
    """
    return
        
    label basement:
            scene bg basement
            with fade

            while True:
                menu:
                    "The basement is quite barren and boring, except for a door that requires an numeric password. Enter something?"

                    "Yes":
                        python:
                            userPass = renpy.input("What will you enter?", allow="1234567890", length=4, )
                            if int(userPass) == combo:
                                renpy.jump("ending")
                            else:
                                ki ("Hm… the door doesn't budge. Wrong answer, I suppose.")
                        
                    "No":
                        ki "Hm... I don't feel ready yet. I will come back later."
                        jump loop
    label ending:
        scene black
        with fade
        stop music fadeout 1.0
        "The door opens slowly, pouring light into the basement below, and on…"
                
        scene cg kazan
        with Fade(1.0, 0, 1.0)
                
        ka "..."
        ki "So you are here after all."
        ka "... Hi."        
                
        if itemsFound == 4 and manuscript == 3:
            ki "Greetings, I am King, a traveling storyteller! … But perhaps… "
            ki "... You'd know me better as Eilhart."

            scene bg basement inner
            show kazan down surprise at left 
            show king neutral at right
            with fade

            ka "Y-YOU’RE EILHART?!"
            show kazan up one
            ka "Holy gods… it… it all makes sense! Why you guys always talk about the plague, why your hands look the way they do…"
            ka "Is my theory right? Are all those praising God during disastrous times a part of the Proponents of Chaos?"

            show king neutral happy
            ki "Hahaha! Calm down, calm down my friend. We have infinite time to speak. I've lived quite a long time, as you must know!"

            show kazan hip annoy
            ka "Ahem. I'm sorry, sir. Please excuse me. I'm just a humble historian interested in your history."
            
            show king neutral
            ki "I am flattered. I, too, was just a humble boy. I think Aelred is much more interesting, but I suppose we are ‘soulbound,’ as you said."

            show kazan down surprise
            ka "Did you really read all of that? Geez."
            ka "I apologize, I haven't edited that yet. Excuse me if anything is incorrect."

            show king back sad 
            ki "I… couldn’t tell you, really. It's been a long time. I couldn't even tell you my father's face if I wanted to. Or what I looked like back then."
            show king back happy
            ki "… Have you ever heard of the Ship of Theseus?"

            show kazan neutral
            "Kazan nodded."

            show king neutral sad 
            ki """
            Perhaps that's the life I live now. Rebuilt out of primordial soup, a mouthpiece for a God that saved a boy whose body expired centuries ago. Hell, do I even have the same neurons anymore? 
            
            I am nothing like that boy that died of the plague. And yet I still harbor his memories. Maybe that's what growing up is like. I wouldn't know. We died young.
            """

            ka "..."

            show king neutral
            ki """
            I don't necessarily regret my choice. I think my life is fun. But that paper made me wonder… what would life be like if I continued staying in that town? If I stayed a cleric’s boy from the 1300s?
            
            Well, I guess I wouldn't have lived. So you could say it's a pointless question! Hehe.
            """

            show kazan hip annoy
            ka "In the end, even being chosen by God seems like a painful experience. You have to leave everyone behind."

            show king back annoy
            ki "Hm. But you seemed keen to leave everyone behind, too."

            show kazan down surprise
            ka "What?"

            show king back happy
            ki "I mean your sister. ‘It's better for your future if you forget about me,’ not to mention the rest of that letter. How depressing!"

            show kazan hip annoy
            ka "... You don't have to say it so condescendingly. I know what I am."
            show kazan up two
            ka """
            So what if I need to abandon them? You don't regret it either, right? It's for the greater good. 
            
            You – actually, I suppose you'd know if you read the letter –, but that woman… I'm not in her good graces. 
            
            Any association with me gets you on the bottom of society, too. And my sister deserves better.
            """

            show king neutral
            ki """
            You are a smart man. You have ambitions. You do good research. I wouldn't recommend running away. You have the potential to change the world.
            
            This wasn't my original plan when I came here, but seeing as we have a mutual understanding of each other, I have a very special proposal for you.
            """

            show king shrug
            ki "How would you like to join the Proponents of Chaos?"

            show kazan down surprise

            "Kazan is silent. Even more bewildered than I anticipated."

            ka "Wh… what?? Me? Proponent of Chaos?"

            show king neutral happy
            ki "Sure! We’ve needed someone to do the more formal paperwork for a long time. We've got serious members, but I think you've got enough sanity and experience to do it properly and not be bored out of your mind. Plus, I like you!"
            
            show kazan neutral
            ka "So… you're just hiring me to be an accountant?"

            show king neutral
            ki "You'll do fun stuff, too! I'm not THAT heartless! In fact, I've already got a fun expedition for you in mind, but only if you accept."
            show king shrug
            ki "So? How about it, my friend? Will you accept our invitation into chaos?"

            show kazan down surprise
            ka "I..."

            scene black:
                alpha 1.0
            with fade
            ka "... Accept."

            scene cg true one 
            with fade
            play music "audio/Trio for Piano Violin and Viola.mp3" fadein 1.0

            ki "Knock, knock. I've got a new member to introduce to you."
            ka "ohmygodohmygod HOW THE HELL AM I BREATHING?"
            qu "Sir, if you freak out more, I'm not sure how much longer you will continue breathing."
            ka "Uhm. Okay. Haha. This is fine, then--"

            show cg true two
            with vpunch

            fu """
            A new member? Hahaha~! I haven't heard of such a thing in a few years! 
            
            Pray tell, what’s going on with this one? Anomaly from a liminal space? Immortal by virtue of belief? 
            
            Or an underdog full of lunacy?
            """
            ka "!!!"

            show cg true three
            with dissolve
            fu """
            Oh, why hello! Are you in awe, or in fear? Both are equally reasonable and likely reactions. 
            
            Please, introduce yourself and the time period you're from. It's hard keeping track these days. The timeline keeps fragmenting more and more. It's really concerning!
            """

            show cg true four 
            with dissolve

            ka "Ahem... Greetings… God? I am Kazan Syed, from the year 20XX. As for classification, I believe I am... 'an underdog full of lunacy… ?'"
            fu """
            Oh, modern! How fun! We always need more modern people. I'm still getting the hang of technology, and these two fossils in front of me certainly can't help.
            
            Anyway, you CAN call me God, but considering that you're modern, maybe you'd be more familiar with the name ‘FUCA.’ I don't really care, whatever makes you comfortable.
            """
            ka "FUCA... like the... ?"
            fu """
            YES. Exactly. It makes sense, does it not? Some people don’t get it. I guess they just haven't taken a biology class! How shameful!
            
            HAHA, I digress. What I mean to say is, 
            """

            scene black
            with fade
            fu "Welcome... to the far side of the moon."
            "Ending: Proponents of Chaos (4/4. True Ending)"

        else:
            $ wrongAns = 0
            scene bg basement inner 
            show king neutral at right
            show kazan neutral at left 
            with fade

            ki "Greetings, I am King, a traveling storyteller! I’d like to thank you for letting me stay these past three days. I understand that I have not been the most polite houseguest."

            show kazan hip annoy
            ka """
            ‘Not the most polite?’
            
            For god’s sake, you broke into my house through my window, stole the food from my fridge, and rummaged through all of my belongings! What degree of politeness is that?!
            
            Ahem.

            Point is, I should have kicked you out the second you stepped foot into my house if I knew how much trouble you'd cause, but I unfortunately respected you too much to do that.
            """

            show king neutral happy
            ki "Hahaha. Truly, I am sorry. Anything you may need for compensation, I am willing to pay. And I humbly thank you for your devotion to our craft!"
            
            show kazan neutral
            ka "Whatever. I don't want to be responsible for freezing someone to death, anyway. Plus, I’m leaving soon."
            show kazan up one
            ka "But something I could get from a Proponent of Chaos… An invitation? Nay, too greedy."
            show kazan neutral
            ka "... A few good stories will do. Not your embellished ones, but the stories with all their mundanity attached. I have no interest in falsehoods."

            show king think
            ki """
            Yes, yes, these are all things I can do. I am honored you take an interest in what I have to say about the past, Mr. Kazan.
            
            But what would you say in having your own story written about you?
            """

            show kazan down surprise
            ka """
            M-me?! My mundane life?! 

            What moral could you get out of my life? ‘Don’t go into a dying profession?’ That's common sense!
            """

            menu:
                "D-do you even know enough about me for this?!"
            
                "You're highly technological and spend a lot of time online.":
                    ka "Wrong."
                    $ wrongAns += 1
            
                "You'd rather read books and academic papers.":
                    ka "... Sure."
            
            menu: 
                "D-do you even know enough about me for this?!"
                
                "Your family couldn't care less about you.":
                    ka "Wrong."
                    $ wrongAns += 1

                "You have a sister that you begrudingly love.":
                    ka "... Sure."
            
            menu: 
                "D-do you even know enough about me for this?!"
                
                "Science is your favorite subject.":
                    ka "Wrong."
                    $ wrongAns += 1

                "History is your favorite subject.":
                    ka "... Sure."
            
            menu: 
                "D-do you even know enough about me for this?!"
                
                "You're a well renowned academic author, really.":
                    ka "Wrong."
                    $ wrongAns += 1

                "You live your entire life in obscurity.":
                    ka "... Sure."
            
                    
                #menu end

            if wrongAns > 2:
                show kazan hip annoy
                ka "You know not nearly enough about me to write anything true to life. I was hoping someone of your caliber would know a little more."
                ka "Disappointing, to say the least."

                "How embarrassing! To think I've spent so much time in this cabin with nothing to show of it!"
                show king neutral sad 
                ki "My memory has gotten rusty, it seems… I sincerely apologize for the trouble! From the time I've spent here, you seem like a respectable and intelligent man."
                ki "You deserve none of the disrespect I have given you today."

                ka """
                No… it is very much deserved.
                
                You may not know it, but I have borne witness to the irreparable damage of the world. And I am powerless to it. 
                """
                show kazan up two
                ka "So I sit here in my cabin, writing warnings in the form of past histories to feebly spur someone to stop it."

                show king neutral
                ki """
                Well, perhaps there is still something you can do.
                
                Share me the stories you find. Surely, if I am spoonfed the information, I won't mess it up, right? 
                
                We will spread them for you, far and wide, and in return, you'll get some payment every once in a while. Perhaps my own personal stories, perhaps some material change. Deal?
                """

                show kazan up one
                ka "A personal way to spread history to the entire world? Outside obscure academic journals, but through THE King and Queen?! O-of course! I oblige! I accept!!"

                show king shrug
                ki "HAHAHA! THEN, it's a deal, my new partner in crime. Let us spread the stories of man, of chaos and order, of imagination and atoms!"

                scene black:
                    alpha 1.0
                with fade
                """
                In the end, I didn't get the exact story I was looking for. Instead, I got many obscure tales, tallied by a lonely man in a wooden cabin.
                
                Kazan… despite their dour personality, they are a good, honest man. Queen and I have become good friends with him. We like to have tea and pancakes together! They're actually quite a good cook, you know?
                
                I can tell they have bigger ambitions, but… I'm not sure if they're ready for them yet. I don't think they even believe in themselves. 
                
                Perhaps, if I could go back… I’d try to find out a little bit more about them. See if they're ready for the next step. 
                
                But I suppose that is something I can do.

                Ending: Failed Research. (1/4)
                """
            
            else: 
                ka "... Fine. I suppose you know enough to write something decent."
                ka "But… my life until now…"
                ka "Are you sure I’ve done enough for a proper conclusion? Is writing obscure papers REALLY the ending you want for my mess of a story?"

                show king neutral
                ki "Well, how would you want it to end?"

                show kazan neutral
                ka "Obviously, I’d fix all of my mistakes. Or at least, get someone to clean it up for me. Shoot that woman, maybe?"
                ka "Ha... but that didn't go well for me. Killed the spirits in everyone in my family. "
                show kazan hip annoy
                ka "So, I don't know. You're the creative one. Go figure."

                show king back happy
                ki """
                That's how we want all of our stories to end, isn't it? But it seems you have bigger ambitions. You have the capability to make a hopeful note, you just have to push through the doubt.
                
                No good story is without its conflict, after all.
                
                Tell you what; I'll make it an open, but happy ending, so it's up to interpretation. But I still need some real-life inspiration. So I have a deal!
                
                Share me the stories you find as a historian. And I'll share them with the bigger world.
                """

                show kazan up one
                ka "A personal way to spread history to the entire world? Outside obscure academic journals, but through THE King and Queen?! O-of course! I oblige! I accept!!"

                show king shrug
                ki "HAHAHA! THEN, it's a deal, my new partner in crime. Let us spread the stories of man, of chaos and order, of imagination and atoms!"

                scene black:
                    alpha 1.0
                with fade

                "In the end,"

                if itemsFound == 1:
                    "I actually had to take lots of creative liberties. I didn't gather as much information as I thought. I got a big mouthful from Kazan afterwards, who came to see our performance. Hehe."
                elif itemsFound == 2:
                    "The story ended up quite imaginative. I think Kazan, who came to see our performance, was a little disappointed, but he didn't fuss too much. I suppose it was as truthful as any good fairytale."
                elif itemsFound == 3:
                    "The story was a big hit, although I had to fill in some gaps here and there. Kazan, who came to see our performance, found it serviceable. Considering their hard expectations, I’d consider that a great success!"
                else: 
                    "The story was a great hit! People seemed to find its more grounded and realistic nature an interesting and engaging departure from our regular material, and so listened even deeper than usual! Hehe, and Kazan, who came to see our performance, seemed to like it, too."
                """
                I think this story will stay a staple in our library from now on. A very worthwhile expedition in the woods! 
                
                As for our titular protagonist, Queen and I have become quite good friends with them. They have a different demeanor these days, as if they've gained a little hope. Perhaps a friend or two was what they needed in that lonely cabin of theirs.
                
                In reading their works, sometimes I wonder about my own history. I have my own long story, too. Is there something I can bring to light, too?
                
                But I suppose… I could try and ask my friend to find out.

                Ending: Storytelling with a Friend. (2/4)
                """
        
    
        return
    
    label hall:
        scene bg hallway
        with fade
            
        """
        Hallways… the liminal space between one important moment and the next. But perhaps in its unimportance, something eye-opening will be left on the shelf. 

        … Of course, boring things can be left, too.
        """
        show king back annoy
        with dissolve
        ki "The Historical Journal? Historische Zeitschrift? My, my. How sophisticated." 
        """
        Not my favorite literature.
        
        There seems to be some academic journals on the wall, as well.
        """
        show king neutral
        ki "Charta Slavica? Hm... never heard of that one!"
        show king think
        ki """
        Er… I’m not the best at reading Russian, nevermind high-level language like this. But I think the title is… ‘The Effect of Old World Diseases on Modern History’ by Kazan Syed.
        
        There's also a note tucked behind here...
        """
            
        hide king
        show black:
            alpha .5
        show kazan up one
        with dissolve

        ka """
        I finally got something published. Not the so-called publishing of selling papers at your doorstep – No! This is a real paper, with real experts reading my paper!
        
        Hahahaha! I know, it's no Historian, but it proves my writing is not as worthless as everyone makes it out to be. Nay, it has to be valuable in some way.
        """
        show kazan hip annoy
        ka "Disease is a little overdone these days. Should I go nicher? Ahh, but to establish myself, I should probably do a follow up…"
        show kazan up two
        ka "No matter. One day… I will be all over the newspapers, and everyone will have to admit they were wrong. Wrong about me. Wrong about everything."
        show kazan down trauma
        ka "You’re All. The. SAME."

        hide kazan
        hide black
        with dissolve

        """
        A few more papers behind the framed pictures slip out. Fancy letters with wax seals and aged paper.
        
        Rejection. Rejection. Rejection. It seems he wasn't as lucky with these.
        
        Some of them even have scribbled pen on them. How vindictive.
        """

        show king back annoy
        with dissolve
        ki "You act like you're in the right, but it doesn't seem like you believe in yourself, either. Just who are you trying to prove yourself to?"
        $ one = (int)(combo / 1000)
        $ itemsFound += 1
        "Inside one letter is a strange code: 1 - [one]"

        jump loop

    label study:
        scene bg study
        with fade

        "For the working individual, a study is where the mundane yet important documents are stored. As a bonus, you can create the feeling of being an intellectual by decorating like you're a Victorian."
        "That seems to be the direction of this room, doused in earthy tones. Although, I suppose this is a cabin, so maybe that's the point. "
        "An elaborate writing desk sits on the right side of the room. A large lamp looms over stacks of research papers and stationary. I glance over the papers, but most seem unfinished with aggravated babbles detailing how terrible they are."
        show king neutral happy
        with dissolve
        ki "Still, the material itself is interesting. Can't say I've studied much about BCE India myself!"
        "I pick up some papers for my own use, but see an article whose title alarms me."
        "‘The Art of Time Travel’ by Serena ■■■■."
        show king back annoy
        ki "..."
        "I snatch that up, as well. I really thought we got rid of all of those."
        jump loop

    label kitchen:
        "I’m still kind of hungry, so I decide to look around the kitchen some more."
        show king think
        ki "Is there any fruit here... ?"
        "It's been a bit since I've had some fresh produce. It's winter, after all. But maybe there's still some sort of dried fruit."
        "Chips, stale chocolate… a big piece of sugarcane? Interesting, certainly, but I don't think I have the capacity to chew that."
        show king neutral sad
        "... What kind of diet is this?"
        "...There's a lot of coffee beans inside this cabinet. Light, dark, artisanal… oh, and some teas, too!"
        show king neutral happy
        "Eventually, I find some fruit-flavored biscuits. Hehe, these will do nicely! Thank you, my strange-appetite friend!"
        jump loop

    label bedroom:
        scene bg bedroom
        with fade

        "The master bedroom is surprisingly informal. A double bed is cushioned with thick pillows and a well-worn quilt, and a fluffy carpet sits below adorned with yet more pillows and blankets. I suppose even an intellectual needs to stay warm, too."
        "Beneath a conspicuous pile of pillows, I find a journal of some kind…"

        show black:
            alpha .5
        with dissolve
        show kazan neutral smile
        with dissolve

        ka "I enjoy reading philosophy a bit, but I've never tried writing anything introspective myself. The publishers always tell me I can get a bit off topic in my writing, so maybe trying some different genres will help me solidify my informational writing."
        show kazan hip annoy
        ka "Here goes:"
        hide kazan
        with dissolve
        ka """
        Sonder is an interesting concept. It is the feeling when you realize others have a life that is as complex as yours. 
        
        Your friends, your family, the strangers you see on the street. They, too, plan their next dinner while spacing out in the shower, put their colored and white clothes in the same wash cycle, and break friendships over an impulsive word. It happens to everyone, everywhere. 
        
        The people from the past had a life as full as the people now, and the people in the future. History is interesting in that way: how did the people in the future have so different resources, yet die as fulfilled – or even as empty – as the people of today? 
        
        However, media is finite. No amount of hieroglyphics, Latin, or Cyrillic can depict that infinite complexity. No one is going to write down the joy of smelling fresh clothes, or the dismay of getting mud on your freshly cleaned carpet. 
        
        Memory, too, is finite. People don't remember their childhoods, or even what they ate the day before.
        
        And yet, people strive to learn everything about the past, about each other, to create some sort of understanding. Some empathy within themselves. 
        
        We are alone. But we find ourselves in history.
        """
        show kazan hip smile
        with dissolve
        ka "... I think it turned out more like a manifesto. That's fine, I guess. I still kind of like it."

        hide kazan
        hide black
        $ third = (int)((combo % 100) / 10)
        $ itemsFound += 1

        "At the end of the journal, there is a strange code: 3 - [third]"
        #i think that's how you do this i forgot
        
        jump loop
    
    label storage:
        scene bg storage
        with fade
        "A storage room may be a good call for stores and such. All types of things can be housed here: important ones, forgotten ones; loved ones and hated ones. And yet, it must all hold some significance if it hasn't been thrown away yet."
        "Unfortunately, this room is even more messy than the rest of the house."
        show king back annoy
        ki "How do people live like this?"
        "Even I don't have time for this nonsense. Let's just pick the most obscure looking box and hope the atoms smile upon me."
        hide king
        with dissolve
        "I climb over a few boxes, careful not to knock anything over, and pick up a manilla envelope."
        "It's over ten years old. It reads: 'University Poetry Collection.'"

        show black:
            alpha .5
        show kazan neutral smile
        with dissolve
        ka """
        The one with the pearl and purple hair,
        
        O’ my friend,
        
        The maddening glare,

        As science ought to do with souls like ours.
        
        """

        show kazan hip annoy
        with fade
        ka """
        Logic and emotion dance,
        
        It is gunpowder that allows wars of power to be fought.
        
        Is love, too, a war?
        
        Of restraint and brilliance? 
        
        Atoms make up bodies
        
        Make up neurons to think
        
        ‘I hold you in the highest regard.'
        """
        hide kazan
        with dissolve

        "This last one... isn't much like a poem at all."
        show kazan down surprise
        with fade
        ka "Haven't you taken my research into account? The historical losses! The studies into how it affects people mentally!"
        ka "It's supposed to be a warning, not an example! Do you even care at all????"
        show kazan up two
        ka """
        No. You were never sympathetic in the first place. I should have known by the way your smile never reaches your eyes.

        You just wanted to see how far you could go. And this place just lets you. You both are…
        
        No wonder no one here has a reflection.
        """
        show kazan down trauma #do you like my naming....
        ka "I am the only one who deserves to have met you."

        hide kazan
        hide black
        show king think
        with dissolve

        ki "Is this saying... an entire university has no reflection?"
        show king shrug
        ki """
        Hahahha. How interesting.

        And this person they were once enamored with...

        Certainly a good find.
        """

        $ fourth = (int)((combo % 10))
        $ itemsFound += 1

        "On the back of the envelope is a strange code: 4 - [fourth]"

        jump loop

    label living:
        scene bg living
        with fade

        "The living room is cozy and classy: a leather loveseat is flanked by a recliner and a coffee table, and a fireplace houses a modest television. A good place to brainstorm your next story, or cuddle up with a loved one."
        
        show king back annoy
        with dissolve
        "I walk up to the fireplace and hover my hand over the ashes. There's still some residual heat. I should keep my guard up."
        show king neutral
        "Nevertheless, there is work to be done. I sit down on the couch and inspect the table."
        hide king
        with dissolve
        """
        Loose papers and an empty coffee mug surround a thick, black notebook simply labeled 'Myths.'
        
        The notebook seems to be a chronology of folktales told by yours truly, each with dates of origin and historical notes about their context and accuracy. Not a single page has a margin of space remaining.
        """
        show king neutral happy
        with dissolve
        ki "Oh my, is this the house of a fan? How flattering! I think I'm blushing!"
        "I wonder if the owner of this house was at our last performance?"

        jump loop

    label dining:
        scene bg dining
        with fade

        """
        I pick up a broom and dust pan and clean up the glass. Although my boots are thick, I don't want to step on this stuff too much. Oh, and I suppose I should assure the homeowner doesn't get hurt, either. 
        
        Unfortunately, there's not much I can do about the water melting from the snow in the window. I guess I just have to be careful when stepping around here.
        
        While I sweep, I take a look around the dining room. Really, it's not much of an individual room at all. It's an open plan with the kitchen and living room. 
        
        Suddenly, I spot a paper underneath the table. It must have been knocked under there the first day…
        """
        jump manu

        jump loop

    label laundry:
        scene bg laundry
        with fade

        """
        Now that I think about it, I don't quite remember the last time I've done my laundry.
        
        Gross, I know, but I think I lost my ability to sweat a long time ago. Not sure about other odors, though.
        
        Still, it seems rude to use this person’s water bill. I’m fine with stealing food, but I draw the line at paying taxes.
        
        Speaking of, there seems to be some taxes on top of the laundry machine.
        
        … Seems like one of these is a little late. No good, my friend.
        
        Hold on. This one isn't a tax document at all… 
        """
        jump manu

        jump loop

    label guest:
        scene bg guest
        with fade

        "I open the door to an eerily blank guest bedroom."
        show king think
        with dissolve

        """
        Unlike the rest of the house, this room is devoid of any personality. There's not even any clutter; it's like this room has never been stepped into at all. 
        
        It's quiet. 
        
        I open the wardrobe for any clue of belongings. Nothing at all.
        
        Nothing… except a single pearl earring.
        """
        jump loop

    label computer:
        scene bg computer
        with fade

        """
        I have to admit, I am not very tech savvy. I'm just more magic-inclined than technology-inclined. 
        
        It seems this person is the same way, judging by their machinery: A chunky computer chugging with a similarly archaic keyboard. 
        
        I try to log in, but the computer is password protected. No notepads nearby give me any clue of a login, either; only endless research notes about plagues, churches, and… German translation?
        """
        ki "I'm quite fond of Germany, myself!"
        "But there is a manuscript..."
        jump manu

        jump loop

    label bath:
        scene bg bathroom
        with fade

        """
        I’m not expecting to find much in the bathroom. At best, I'm seeing if the plumbing still works in this freezing weather.
        
        But I find something much more interesting than that.
        """
        show king think
        ki "A blocked off mirror, hm?"
        """
        
        If you find an obscured mirror in a home, they say, it indicates that the homeowner has interpersonal issues they don't want to face.
        
        A reflection isn't just simple science, you see; It's another version of you whose job is to peer into you and keep you sane.
        
        If you don't have a reflection, well...
        """
        show king shrug
        ki "You're just too vile a person to change."

        jump loop

    label library:
        scene bg library
        with fade

        "Bookshelves overflow with annotated novels and broken spines and line the walls like a dust jacket. You can almost hear the silverfish just looking at the scene."
        "Clearly, whoever lives here isn't faking their affinity for books."
        show king back annoy
        with dissolve
        """
        I comb through some of the titles on the shelves: Crime and Punishment, No Longer Human, The Plague. Thought-provoking classics.
        
        There are lots of nonfiction titles, as well, mostly consisting of textbooks and secondhand histories. 
        
        Atop one pile of books sit a few letters with annotations.
        """

        hide king
        show black:
            alpha .5
        with dissolve

        s """
        Dear Kazan,
       
        I heard the cabin got finished, so I decided to send this letter to test your address out! If you got it, congrats! If this is someone else, give this letter back to my brother!
        
        I hope you don't use this as an excuse to hole yourself into your studies even more. I don't really get it; why would you graduate, THEN go back to school?
        
        But I guess if I lived in basically-a-library, I’d read a bunch of books, too. Fiction, obviously! You should at least read outside, though. Get a porch or something, nerd.
        
        Love, Sister.
        """

        show kazan hip annoy
        with dissolve
        ka "Ugh, so annoying. I'll read whatever I want. Who told this brat my address?"
        hide kazan
        with dissolve

        m """
        Dear Kazan,

        We found a few manuscripts in your old room, so we've sent it along with this letter. We've also sent some new laboratory internships. 
        
        We haven't told the university your new address, so they're still being sent here.
        
        We all know you're good at writing, so writing some reports for this lab would do some great work for the world. 
        
        Your girlfriend has told us your historical work is great for background knowledge, but I think you have the interests for science, too! 
        
        Of course, we're happy with whatever you do. 

        With love, Mom.
        """

        show kazan neutral
        with dissolve
        ka "You say that, but continue send me internships for work outside my field."
        show kazan down surprise
        ka "... Why is my girlfriend talking to my parents behind my back anyway?"
        hide kazan
        with dissolve

        s """
        Dear Kazan,
        
        The situation at the university got out to the family. I'm sorry. 
        
        I tell you to believe in others a lot, but… I think this is my fault this time.
        
        Maybe you should stay at the cabin until this calms down. I guess you still got this letter, so I'm not sure how safe you'll be from the authorities.
        
        Still, I'll come visit. It's the least I can do.

        Hope you're well, Sister.
        """

        show kazan down trauma
        with dissolve
        ka "I'm doing terrible?--"
        show kazan up two
        ka "I'm doing fine. Thank you for your concern."
        show kazan down surprise
        ka "Forget about her, okay? She's bad news. Don't trust anything about her. And tell mom and dad to stop contacting me--"
        ka "I don't know. It's not their fault. It's all her fault. and, and……"
        show kazan hip annoy
        ka "Ugh. Screw this letter. Screw all of this."
        show kazan down trauma
        ka "Don't trust the university. Don't trust her. Don't trust anyone."
        ka "Are you after me to o????"
        ka "..."
        show kazan hip annoy
        ka "I'm sorry I'm this way."
        ka "Don't blame yourself. But it's better for your future if you forget about me, too."

        hide kazan
        hide black 
        with dissolve

        ki "Underneath escapism, there lies the root of problems."
        $ second = (int)((combo % 1000) / 100)
        $ itemsFound += 1
        "On the back of the letter is a strange code: 2 - [second]"


        jump loop

    label manu:  
        play music "audio/Trio for Piano Violin and Viola.mp3" fadein 1.0
        if manuscript == 0:
            show black:
                alpha .5
            show kazan neutral
            with dissolve

            ka """
            Although the historical recountings of King and Queen are very well executed and relatively accurate, they are much more embellished than realistic. 
            
            One portion of history they like to retell are the three plague pandemics, so I have taken it upon myself to investigate the truth of these eras.
            """
            hide kazan
            with dissolve
            ka """
            The three plague pandemics refer to three separate outbreaks of the bubonic plague (Yersinia pestis) where major chunks of the affected populations died. 
            
            These pandemics are categorized as "disaster times" by historians, meaning there is a higher occurrence of individuals who claim to have met God (or at least, a god).
            """
            show kazan neutral smile
            with dissolve
            ka """
            Of course, these individuals may be acting in hysteria due to the severity of their situations, but more well documented accounts leads me to believe that these individuals may have been recruited to the Proponents of Chaos.
            
            A particular well documented story from the time follows two children who appeared to be resurrected after their deaths from the plague...
            """
            hide kazan
            hide black
            show king neutral
            with dissolve

            "This page of the manuscript ends here."

            ki """
            ... I suppose we do talk about the plague a lot. But you can't fault me for not including the mundane parts. 
            
            You've ended this boring manuscript with a cliffhanger for the most exciting part!  
            
            This page is from a few weeks ago. I wonder if there are other pages lying around.
            """

        elif manuscript == 1:
            show black:
                alpha .5
            show kazan neutral
            with dissolve

            ka """
            These documents originates from a small Catholic Church in modern day Germany and details the lives of Aelred A■■■■ and Eilhart T■■■■■, the sons of the local nobility and church respectively. 
            
            Despite their class gap, they were very good friends. It is unknown when exactly they met, but it is reported that Eilhart was often seen watching the knightly training of Aelred outside. Perhaps this is why many witnessed them pretend to be opposing warriors of a  medieval war, spinning stories of how such a conflict came to be. 
            
            Although the local nobility and church were glad to have formed a bond through their two heirs, they worried that this “friendship” may mix up their family duties. Nobles, after all, have no need to answer the calls of the people, and clergies have no need to fight with sharpened steel. 
            
            Thus, the two were advised to keep themselves occupied with their official traditions, much to their discontent.
            """
            show kazan hip annoy
            ka """
            However, the line between 'Higher' and 'Lower' disappeared with the onset of the plague. 
            
            Eventually, both the noble and common sick were laid on the floor in rows like a mass burial in progress. 
            
            Aelred and Eilhart ended up being treated next to each other – perhaps as a gesture of good faith to the two soul bounds – but it wasn't enough to save them from the black death.
            """

            hide black
            hide kazan
            show king neutral sad
            with dissolve

            "This page of the manuscript ends here."
            ki """
            Aelred and Eilhart… it's been a long time since I've heard those names

            Yes, this is a tale very familiar to me. And yet, almost forgotten.

            This is from a week ago. There may be one more page.
            """

        else:
            show black:
                alpha .5
            show kazan neutral
            with dissolve

            ka """
            The next day, the A■■■■ family arrived at the church, having gained late-stage plague symptoms overnight. They all died a few days later. 
            
            A day after their deaths, Aelred and Eilhart were seen frolicking in the square. Despite their liveliness, their bodies still sported the markings of a corpse: pale skin, discolored eyes, and most importantly, black fingertips. 
            
            This was a frightening sight for the townsfolk: Were they possessed by demons? A warning from God about the nature of the plague?
            
            The head priest, Eilhart’s father, was the only one brave enough to directly talk to the two children. 
            
            They claimed that they were 'resurrected by a white angel because of their faithfulness to courage and chaos and chosen to spread God’s story.'
             
            It was hard to argue. How else would the dead of God's plague come back to life?
            
            The children then asked for a blessing before heading out on their endless journey, eyes sparking and smiles gleaming in innocent earnest. 
            
            The priest complied, bittersweetly giving his son a goodbye to a world unknown.
            
            Before they left, he stated, 'I suppose I was wrong to separate you two, if you have been approved by God. I pray you never come apart again.' 
            
            Eilhart replied, 'You are a good man, father. You listen and help the people, both rich and poor. Be true to the fairness of God, and you shall surely lead this town through the plague.'
            """

            show kazan neutral smile
            ka """
            After the death of the local nobility, the church took control of the town. They had little clue how to lead a town outside of a religious setting, but they managed to stay afloat using the old nobility’s funds. 
            
            A small religious holiday was established, turnout to the church doubled, and many young men and women started studying scripture to decipher what the existence of their new prophets meant. 
            
            Although the town was happy, it was not prosperous, so they eventually accepted the movement of a new nobility into town to stir business. 
            
            Still, the people were happy with fading into obscurity, knowing that their little insignificant town would live on through the tale of two blesséd boys.
            """
            
            show black:
                alpha 1.0
            hide kazan
            with dissolve

            ki "..."
            """
            The wind quietly patters on the window, muffled by the mountain of snow.
            
            It never snowed like this where we lived, did it? I can hardly remember now.
            
            I know the true nature of this world now. It is much larger, methodical, and chaotic than the book you immersed yourself in. 
            
            I still follow that white angel, but I imagine they're different than what you believed them to be. 
            """
            ki "Are you still proud of me, Father?"
            """
            It's a pointless question. Your soul must be far away from me by now, passed through countless individuals.
            
            And yet, my soul remains the same little boy.
            
            Haha. Although, I suppose it's normal for a son to outlive his father. 
            """
            ki "... All I can do, and continue to do, is carry on your vow to fairness."
            "I'm glad we were remembered."
        
        $ manuscript += 1

        jump loop
    
    "IF YOU'RE SEEING THIS in game SOMETHING WENT WRONG PLEASE REPORT THANKS - slushie"
    return