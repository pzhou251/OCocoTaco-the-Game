# The script of the game goes in this file.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show zeil delighted at left with dissolve

    zeil "Hi! My name is Zeil"

    

    # These display lines of dialogue.

    show eileen happy with moveinright

    eileen "You've created a new Ren'Py game. virtual crunch wrap supreme 😿"

    eileen "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
