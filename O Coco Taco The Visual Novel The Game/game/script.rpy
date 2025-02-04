# The script of the game goes in this file.

#flags
#default persistent.pizzaFlag = 0
#define menuFlag = 0

#character positions
transform quarter_left:
    xalign .25 yalign 1.0
transform quarter_right:
    xalign .75 yalign 1.0

# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg classroom with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    show turan neutral with dissolve

    wist "What da heck I just wanted to buy a crunchwrap supreme , I didn't want to play a dating sim :c"

    play sound shake
    show turan shocked with hpunch
    turandot "WAITTT KITTY !!"
    show turan sad
    turandot "Don't go, lets eat tacos together 😭"

    wist "???"
    wist "how did you know I was a cat? :c hmm..."
    wist "Are you a player or an npc"

    show turan neutral
    turandot "Yeah."

    wist "???"
    wist "That doesnt answer my question"

    show turan neutral
    turandot "Oh, I'm just stuck here. My name's Turandot."

    wist "oh nice to meet you im wist : 3"
    wist "..."
    
    show turan happy
    turandot "..."

    wist "Wait :/ what do u mean ur stuck here"

    show turan thinking
    turandot "Hmm have u ever watched Saber Art Online."
    play sound bruh

    wist ">:/ i want to log out…."

    show turan shocked
    turandot "Nooooo wait lets get some food , Wist ! We can get a crunchy wrapy supremi™."
    
    wist "(╯✧ ∇ ✧)╯ crunchywrapy supremy…"

    #bmg transition
    play sound tacochime
    
    narrator "Yeah we know fast food chains dont usually have door chimes when you enter its just to establish the setting ,,, gosh"
    
    show turan confused
    turandot "Why so sassy they probably weren't even thinking about that."

    wist "who are you talking to?? Whos they??0 ___0' "

    show turan neutral
    turandot "Don’t worry this game is , like , 5 min long so we dont have time delve into that."
    show turan happy
    turandot  "Let's go order."

    scene bg outsidecoco with fade
    play sound tacobeep

    show turan happy at center
    turandot "hiiiii :3"
    show turan sad at left with move

    show dj neutral at right

    dj " *sigh* "

    dj "Once you add a story, pictures, and music, you can release it to the world!"

label food_menu:
menu:
    dj "Whatever, what do u want"

    "Crunchywrapy supremy":
        $ menuFlag = 0
        turandot "yum i love crunchwrapy supremy (placeholder text)"

    "Cheesy beans taquito":
        $ menuFlag = 1
        turandot "can you not spit on it this time"
        dj "hmmm ill think about it"
        wist "wait you spit on it??"
        wist "i wanna speak to your manager *karen hair sprite*"

    "Brazilian pizza":
        $ menuFlag = 2

        
        jump pizza_choice

label pizza_choice:
menu:
    dj "are you sure about this? ( this action will have consequences) "
    "Yes":
        #background and Turandot get darker / looks like night
        $ persistent.pizzaFlag += 1
        #split second turandot sprite change
        #Game closes 
        $ renpy.quit()

    "No":
        jump food_menu
        #Goes back to menu
        #music restarts

label after_menu:



     


    # This ends the game.

    return
