# The script of the game goes in this file.

default persistent.pizzaFlag = 0
define menuFlag = 0

# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg classroom with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show turandot at left with dissolve

    turandot "Hi! My name is Turandot"

    

    # These display lines of dialogue.

    show dj with moveinright

    dj "You've created a new Ren'Py game.  crunch wrap supreme 😿"

    dj "Once you add a story, pictures, and music, you can release it to the world!"

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
        $ persistent.pizzaFlag += 1
        jump pizza_choice

label pizza_choice:


label after_menu:



     


    # This ends the game.

    return
