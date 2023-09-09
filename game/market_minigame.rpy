default market_picked_items = []
default market_required_items = []
default market_happy_customer = False

default money = 0

screen market_pick_items:
    add "market_empty"
    if "detergent" not in market_picked_items:
        imagebutton:
            pos (847,818)
            hover_sound "audio/hover.wav"
            auto "detergent_%s"
            action AddToSet(market_picked_items, "detergent") mouse "hand_cursor"

    if "icecream" not in market_picked_items:
        imagebutton:
            pos (872,178)
            hover_sound "audio/hover.wav"
            auto "icecream_%s"
            action AddToSet(market_picked_items, "icecream") mouse "hand_cursor"

    if "dishwasher" not in market_picked_items:
        imagebutton:
            pos (1108, 562)
            hover_sound "audio/hover.wav"
            auto "dishwasher_%s"
            action AddToSet(market_picked_items, "dishwasher") mouse "hand_cursor"

    if "slurpee" not in market_picked_items:
        imagebutton:
            pos (603, 332)
            hover_sound "audio/hover.wav"
            auto "slurpee_%s"
            action AddToSet(market_picked_items, "slurpee") mouse "hand_cursor"

    if "matcha" not in market_picked_items:
        imagebutton:
            pos (447, 573)
            hover_sound "audio/hover.wav"
            auto "matcha_%s"
            action AddToSet(market_picked_items, "matcha") mouse "hand_cursor"

    if "umbrella" not in market_picked_items:
        imagebutton:
            pos (400, 210)
            hover_sound "audio/hover.wav"
            auto "umbrella_%s"
            action AddToSet(market_picked_items, "umbrella") mouse "hand_cursor"

    if len(market_picked_items) == 0:
        imagebutton:
            pos (0,705)
            hover_sound "audio/hover.wav"
            auto "trolley_%s"
            action NullAction() mouse "cross_cursor"
    else:
        imagebutton:
            pos (0,705)
            hover_sound "audio/hover.wav"
            auto "trolley_%s"
            action Return() mouse "hand_cursor"







    on "show" action SetVariable("market_picked_items", [])

screen market_money:
    add "images/minigame/money1.png" pos (0,0)
    text "[money]" size 70 pos (150,0)

label market_minigame1:

    scene d2_grocershop1
    show screen market_money

    cust "I want something that is green in the outside, white in the inside, bubbly when it is mixed with water."
    $ market_required_items = ["detergent"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items


    cust "Weather is hot out here, grab me something that is icy cool."
    $ market_required_items = ["icecream"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_1

    scene d2_grocershop1
    cust "Get me something that is green, regardless inside or outside."
    $ market_required_items = ["dishwasher"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_2

    scene d2_grocershop1
    cust "Mom, I want a green, brain freezing stuff."
    $ market_required_items = ["slurpee"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_3

    scene d2_grocershop1
    cust "I am a huge fan of Matcha, can you get me something?"
    $ market_required_items = ["matcha"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_4

    scene d2_grocershop1
    cust "Jeez it’s hot out there."
    $ market_required_items = ["umbrella"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_5

    scene d2_grocershop1
    cust "One green drink."
    $ market_required_items = ["slurpee"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_6

    scene d2_grocershop1
    cust "Listen carefully, I am not repeating my words again. One liquid for household uses, one liquid for dirty clothes and one for me."
    $ market_required_items = ["detergent", "dishwasher", "slurpee"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_7

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Second Day{/size}"

label market_minigame2:

    scene d2_grocershop1
    show screen market_money

    scene d2_grocershop1
    cust "Get me something that is green, regardless inside or outside."
    $ market_required_items = ["dishwasher"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_8

    scene d2_grocershop1
    cust "Ice cream please."
    $ market_required_items = ["icecream"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_9

    scene d2_grocershop1
    cust "One green drink."
    $ market_required_items = ["slurpee"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_10


    scene d2_grocershop1
    cust "One dishwasher, one ice cream and one umbrella."
    $ market_required_items = ["icecream", "dishwasher", "umbrella"]
    call screen market_pick_items
    call market_check_picked_items from _call_market_check_picked_items_11

    return


label market_check_picked_items:

    $ market_happy_customer = True

    if len(market_picked_items) == len(market_required_items):
        python:
            for i in market_required_items:
                if i not in market_picked_items:
                    market_happy_customer = False
    elif True:
        $ market_happy_customer = False

    if market_happy_customer:
        play sound cash_register
        $ money += 200 * len(market_picked_items)
        cust "Thank you"
    elif True:
        cust "This is not what I want!"

    return
