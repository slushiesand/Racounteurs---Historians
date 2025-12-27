# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character

init python:
    import random
    daysLeft = 3
    itemsFound = 0

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
    
    Queen and I have been doing this kind of thing for a long time. We’re a two-man theatre, gathering special stories from all around the world for those who wish to hear our gallant tales. I do most of the writing and information gathering, while Queen composes music and choreographs. It's a wonderful life. I wouldn't have it any other way!
    
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
    show king think frown
    "Nevertheless, there's probably something interesting out there, so I continue on."
    

    scene bg forest2
    show king neutral frown
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

    show king neutral happy
    """
    But in the distance, I see a saving grace: a cabin! 

    It is unlit, but well maintained. Perhaps the owner isn't home?

    I briskly walk to the cabin and knock on the door.
    """

    scene bg window
    """
        …
    Nothing. I guess I'll have to do this the hard way, then. 
    Lockpick the door, or break through the window? 
    """

    return
