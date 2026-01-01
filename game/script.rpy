
init python:
    import random

    itemsFound = 0
    manuscript = 1

    time = ["morning", "afternoon", "evening", "night"]
    timeCounter = 0
    daysLeft = 3

    location = ["Hallway", "Study", "Kitchen", "Bedroom", "Storage", "Living Room", "Dining Room", "Laundry Room", "Guest Bedroom", "Computer Room", "Bathroom", "Library"]
    unavailable = []

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
#image darkener = Frame(Solid("#000"))


# lowkey forgot everything we are relying on the documentation 100%



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    $ combo = random.randint(1000, 9999)

    #show top_text "This text is shown at the center-top of the screen"
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
    show bg dining
    with dissolve
    "There's an avalanche of snow coming through the window!"
    show bg forest4
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
    "this runs when time runs out."
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
            "true ending"
        else:
            $ wrongAns = 0
            $ question = 0
            "yap yap"

            while wrongAns < 3 and question < 5:
                menu:
                    "D-do you even know enough about me for this?!"
                
                    "wrong":
                        ka "Wrong."
                        $ wrongAns += 1
                
                    "right":
                        ka "... Sure."
                #menu end
                $ question += 1

            if wrongAns == 3:
                ka "You know not nearly enough about me to write anything true to life. I was hoping someone of your caliber would know a little more."
                ka "Disappointing, to say the least."
            else: 
                ka "... Fine. I suppose you know enough to write something decent."
                ka "But… my life until now…"
                ka "Are you sure I’ve done enough for a proper conclusion? Is writing obscure papers REALLY the ending you want for my mess of a story?"

        "this runs when the corresponding segment is over"
        return
    
    label hall:
        "1"
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
        $ third = c

        "At the end of the journal, there is a strange code: 3 - [third]"
        #i think that's how you do this i forgot
        
        jump loop
    
    label storage:
        scene bg storage
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
        """
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
        "I am the only one who deserves to have met you."

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

        $ fourth = 

        jump loop

    label living:
        "6"
        jump loop

    label dining:
        "7"
        jump loop

    label laundry:
        "8"
        jump loop

    label guest:
        "9"
        jump loop

    label computer:
        "10"
        jump loop

    label bath:
        "11"
        jump loop

    label library:
        "12"
        jump loop
    
    "IF YOU'RE SEEING THIS in game SOMETHING WENT WRONG PLEASE REPORT THANKS - slushie"
    return