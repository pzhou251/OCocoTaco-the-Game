# The script of the game goes in this file.

#flags
default persistent.pizza_flag = 0
default persistent.menu_flag = 0
default persistent.game_started = 0
default persistent.game_restart = 0

#character positions
transform quarter_left:
    xalign .25 yalign 1.0
transform quarter_right:
    xalign .75 yalign 1.0
transform center_center:
    xalign .5 yalign .5
transform bounce:
    yoffset 0
    linear 0.2 yoffset -30
    linear 0.2 yoffset 0

# The game starts here.


label start:
    $ _game_menu_screen = 'preferences'

    show screen exit_button
    play music normal volume 0.5 fadein 0.5
    define config.window = None

    #debug
    $ persistent.pizza_flag = 3
    $ persistent.menu_flag = 2
    $ persistent.game_started = 1

    if (persistent.pizza_flag > 0) and (persistent.game_started > 0) and (persistent.menu_flag == 2):
        jump pizza_start

    # figure out how to deal with persistents when the user quits manually
    $ persistent.menu_flag = 0
    $ persistent.game_started = 1

    scene bg obby with pixellate

    play sound boing
    play sound oof

    wist "Dang it, I quit >:c"

    wist "{i}Failed this obby again.{/i}"

    wist "{i}Maybe I should play a new game.{/i}"

    wist "hmm?"
    play sound click

    scene bg games with pixellate
    $ result = "loop"

    play sound click
    wist "huh? caca o taco"

    call screen roblox_menu
    

    
    play sound click

    scene bg outside with pixellate
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
    
    wist "crunchywrapy supremy…"

    if(persistent.game_restart == 1):
        scene bg outsidecoco4 with pixellate
    else:
        scene bg outsidecoco3 with pixellate
    play sound tacochime
    
    narrator "Yeah we know fast food chains dont usually have door chimes when you enter its just to establish the setting ,,, gosh"
    
    show turan confused
    turandot "Why so sassy they probably weren't even thinking about that."

    wist "who are you talking to?? Whos they??0 ___0' "

    show turan neutral
    turandot "Don’t worry this game is , like , 5 min long so we dont have time delve into that."
    show turan happy
    turandot  "Let's go order."

    scene bg insidecoco with pixellate
    play sound tacobeep

    show turan happy at center with dissolve
    turandot "hiiiii :3"
    show turan sad at quarter_left with move

    show dj neutral at quarter_right

    dj " *sigh* "

    wist "hello!"

    dj "No animals allowed."

    wist "?????? >:O"

    show turan mad at quarter_left
    turandot "They're not an animal they're a player !"

    wist "*sweating* yeah…"

    hide turan mad with moveoutleft
    show dj mad at center with move

label food_menu:
    
    dj "Whatever, what do u want"

    if(persistent.pizza_flag >= 3):
        if(persistent.game_restart == 1):
            show cocomenu ugly with moveintop
            play sound shake
            pause 1.50
            show cocomenu ugly
            hide cocomenu ugly with moveouttop
            play sound boing
            show cocomenu soldout with moveinbottom
        else:
            show cocomenu soldout
        call screen food_menu_outtapizza
        $ result = _return
        hide cocomenu soldout
    else:
        if(persistent.game_restart == 1):
            show cocomenu ugly with moveintop
            play sound shake
            pause 1.5
            hide cocomenu ugly with moveouttop
            play sound boing
            show cocomenu with moveinbottom

        else:
            show cocomenu 
        call screen food_menu
        $ result = _return
        hide cocomenu
    if(result == "crunchy"):
        $ persistent.menu_flag = 1
        show turan happy at quarter_left
        show dj mad at quarter_right
        turandot "yum i love crunchwrapy supremy"
        jump after_menu
    elif(result == "cheesy"):
        $ persistent.menu_flag = 1
        turandot "can you not spit on it this time"
        dj "hmmm ill think about it"
        wist "wait you spit on it??"
        wist "i wanna speak to your manager"
        #karen hair sprite
        dj "Allegedly... its just jokes."
        jump after_menu
    elif(result == "pizza"):
        $ persistent.menu_flag = 2
        jump pizza_choice

label pizza_choice:
menu:
    dj "are you sure about this? ( this action will have consequences) "
    "Yes":
        stop music
        play sound horror
        scene bg cocoscary 
        $ persistent.pizza_flag += 1
        dj "you have chosen pizza [persistent.pizza_flag] time(s)"

        show turan scared
        turandot "hey wait-"
    
        #Game closes 
        $ renpy.quit()

    "No":
        jump food_menu
        #Goes back to menu
        #music restarts

label pizza_start:
    # The game reload , bgm play
    play music normalwrong fadein 0.5
    if(persistent.pizza_flag == 3):
        jump outta_pizza
    show turan thinking at center with dissolve
    turandot "phewww thank goshness you dindt have to see that" 
    wist "??? why did my screen just black out just now?" 
    turandot "ooo yeah i didn't want you to see what that Brazilian pizza would do to me" 
    wist "wait you did that? you logged me out of the game???"  
    turandot "oh it wasn't me it was my code writers"
    wist "excuse me o_O what kind of vn is this" 

    scene bg coco bathroom with pixellate
    show turan neutral at center with dissolve
    turandot "yeah they probably wanted to protect you from what that pizza was going to do to me"
    wist "… o_e"
    if(persistent.pizza_flag == 1):
        turandot "ufff I hope you don’t get the pizza again"
        wist "again?"
    elif(persistent.pizza_flag == 2):
        show turan scared at center with dissolve
        turandot "seriously. IM STUFFED"
        pause 2.20
    hide turan neutral with moveoutright
    $ persistent.menu_flag = 0
    stop music

    play music normal volume 0.5 fadein 0.5
    narrator "The cycle repeats"
    
    jump game_end




label after_menu:
    scene bg insidecoco with pixellate
    play sound tacochime
    show turan happy at center with dissolve

    turandot "time to eattt"
    wist "ok I’ll try a bite"
    play sound nom

    wist "this doesn’t taste like anything. i dunno why i thought it would"
    show turan neutral
    turandot "do u like it : 3"
    wist "uhhh do u like it"

    show turan thinking
    turandot "hmm i like the wingstart more"
    wist "what's with all the parody names? "
    show turan thinking at center, bounce

    turandot "so we dont get sued duhhh "
    wist "Who’s we?? Actually who even are you really?"
    
    show turan neutral 
    turandot "oh and me uhh Turandot the T at the end isnt pronounced 🙂"
    show turan confused
    turandot "we is you know… we"
    wist "{i}There’s something… off about this place. And this guy. {/i}"
    wist "{i}I think she's funny and I don’t want to leave her here all alone… what should I do?? {/i}"
    menu:
        "Who cares! Get the heck out of here":
            wist "sorry but i got to gooo"
            show turan shocked
            turandot "no wait-"
    menu:
        narrator "do you want to log out?"
        "yes":
            stop music
            play sound horror
            scene bg cocoscary
            jump game_end
        "No":
            wist "{i} i must keep eating... this food... {/i}"
            show turan shocked
            turandot "phewww thank goddess u didnt decide to leave, its gets really lonely here"
            wist "Well its kind of fun being with you , lets play another game !"
            show turan happy at center, bounce
            narrator "The cycle repeats"
            scene bg main menu with fade
            $ persistent.game_restart = 1
            jump game_end


    label outta_pizza:
        show weouttapizza at center_center
        play sound horror
        # play sound horror_hit
        # play sound metal_pipe
        # play sound bang
        play music normalwrong fadein 0.5
        
        $ persistent.menu_flag = 0
        pause
        

    label game_end:
    # This ends the game
    $ persistent.game_started = 0 # game ended
    return
