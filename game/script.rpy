
init python:
    import random
    daysLeft = 3
    itemsFound = 0
    time = ["morning", "afternoon", "evening", "night"]
    timeCounter = 0
    manuscript = 1
    location = ["Hallway", "Study", "Kitchen", "Bedroom", "Storage", "Living Room", "Dining Room", "Laundry Room", "Guest Bedroom", "Computer Room", "Bathroom", "Library"]

    def locationDetermine(location):

        """renpy
        if location == "Hallway":
            jump hall
        elif location == "Study":
            jump study
        elif location == "Kitchen":
            jump kitchen
        elif location == "Bedroom":
            jump bedroom
        elif location == "Storage":
            jump storage
        elif location == "Living Room":
            jump living
        elif location == "Dining Room":
            jump dining
        elif location = "Laundry Room":
            jump laundry
        elif location = "Guest Bedroom":
            jump guest
        elif location = "Computer Room":
            jump computer
        elif location = "Bathroom":
            jump bath
        elif location = "Library":
            jump library
        """

        #yandev ahh code. this is what happens when you havent coded in python for like 2 years


define ki = Character("King", color = "#FDCA62")
define ka = Character("Kazan", color="#A6E1FE")

define qu = Character("Queen", color="#5077CA")
define fu = Character("???", color="#F")
define s = Character("Sister", color="#F")
define m = Character("Mother", color="#F")

image top_text = ParameterizedText(xalign=0.5, yalign=0.0)
image black = "#000"

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

    # This ends the game.

    scene cg inn tired
    with Fade(1.0, 0, 1.0)

    ki "... Ugh! I have no inspiration!"
    qu "It's alright, King. We had a good session today. The people seemed to especially enjoy our telling of the Ouroboros Angel."
    ki "Of course, of course. I'm glad! That one’s really underrated! But everyone in the world has probably heard it already.\nWe need… something NEW!"
    qu "Hmm. No need to be hasty. I think you're getting restless again.\nPerhaps you ought to take a walk in the forest. Nature is always an inspiring sight. And if not, at least you'll clear your mind."
    
    "Queen… always trying to comfort me, even if he doesn't smile much himself… and always more patient about life than I."
    
    show cg inn happy
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

    """
    I reach the forest on the edge of town. Queen and I had walked through it when we first came, but the road on which we walked is no longer visible.
    
    In fact, everything seems to be flattened to one single surface of pure snow, with trees serving as the only points of interest on this coordinate plane.
    """
    show king think frown at right
    "Nevertheless, there's probably something interesting out there, so I continue on."
    

    scene bg forest2
    show king neutral frown at right
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

    show king neutral sad

    ki "Oof..."

    """
    Still, I should be fine.

    More importantly, no alarm systems go off. I might not die for trespassing!
    """

    show king neutral happy

    """
    I leave some money on the table as a gesture of good will, and scuttle to find somewhere to hide for the night. 

    If there is someone in the house, I should find somewhere secluded to sleep so they don't find me. A blanket closet may be a good candidate.
    """

    #ideally walking sound goes here
    show king neutral
    ki "... Ah-hah."
    "Just what I wanted."
    ki "Alright, get comfy, me. It's going to be a long night."
    hide king
    with fade

    pause 3.0
    #music here?
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
    show king neutral ecstatic
    with vpunch
    ki "A writer trapped in an empty cabin for who-knows-how-long? That's just SCREAMING for a good story to be found!"
    show king neutral happy
    ki "O’ thank you, chaotic particles that have collided in such a way to grant this luck to me!"
    show king neutral
    ki "Let me write something to Queen to let him know that I’m okay, then I can begin my expedition."

    label loop:
        while daysLeft > 0:
            scene bg kitchen
            show king neutral
            with wipeleft

            if timeCounter == 0:
                if daysLeft == 3:
                    ki "I suppose I should eat something. Let's see what's in my bag…"
                    ki "Some granola bars and a bottle of water. Surprised this didn't freeze over. Sure, that'll do for today. Let's not rob the fridge just yet!"
                elif daysLeft == 2:
                    ki "I said I wasn't gonna rob the fridge yesterday, but that doesn't account for today. Hopefully, none of this is expired…"
                    ki "Huh. The fridge seems to be working. Did a backup generator go off? I should still go with something with a long shelf-life to be safe, though."
                    show king neutral happy
                    ki "Let’s see… a jar of preserved fruit jelly. I saw some bread on the counter, as well. Hehe, a good breakfast for me today!"
                else: 
                    ki "The fridge served me well last time. Let's see…"
                    ki "... Some pancakes seem to have appeared overnight. They’re a bit charred at the edges, but charming enough."
                    menu:
                        "Should I eat them?"
                    
                        "Yes!!!!!!!!!!!!!":
                            $ pass
                        "No.":
                            $ pass
                
                    ki "Luckily, I still have some jam from yesterday."
                    show king neutral annoy
                    ki "Now that I think about it… I should probably pay for this too…"
            elif timeCounter == 4:
                $ daysLeft -= 1
                $ timeCounter = 0
                jump loop
            
                    
            python:
                #ok this is going to be incredibly inefficient but i dont feel like devoting brainpower to making this efficient
                loc1 = random.choice(location)
                

            menu:
                "It looks like the snow will melt in [daysLeft] days. It's currently [time[timeCounter]]. Where should I go?"
            
                "[ loc1 ]":
                    $ timeCounter += 1
                    $ locationDetermine(loc1)

                "Basement":
                    $ timeCounter += 1
                    jump basement
    
        
            
    #loop end here
    "this runs when time runs out."
    return
        
    label basement:
            "test"
            jump loop
    
    label hall:
        "1"


        jump loop

    label study:
        "2"
        jump loop

    label kitchen:
        "3"
        jump loop

    label bedroom:
        "4"
        jump loop
    
    label storage:
        "5"
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
    
    "just in case something goes wrong"
    return

