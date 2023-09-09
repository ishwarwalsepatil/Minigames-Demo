init:
    define fade = Fade(0.5, 0.2, 0.5)
    define dissolve = Dissolve(0.5)
    define slowdissolve = Dissolve(1.5)
    define flash = Fade(0.1, 0.0, 0.5, color="#fff")
    define config.default_music_volume = 0.2
    define config.default_sfx_volume = 0.2


init python:
    renpy.music.register_channel("channel1", mixer="sfx", loop= False)
init python:
    renpy.music.register_channel("channel2", mixer="sfx",loop= False)
init python:
    renpy.music.register_channel("music2", mixer="music")


define o = Character("Olivia", color="590059")
define p = Character("Prince", color="ffd792")

define cust = Character("Customer", color="ffd792")

label start:

    menu:
        "Market Minigame":
            jump market_minigame1

        "RPG Style Battle":
            jump rpg_battle




label rpg_battle:
    scene black with fade
    scene black with dissolve
    centered "{size=+30}First Battle{/size}"

    $ quick_menu  = False
    $ mcside = [mcb, orb]
    $ eside = [battle1_opp]
    $ battle_no = 1
    jump group_battle

label after_battle1_w:
    $ battle_1_win = True
    scene black
    with fade
    $ mcside[0].exp += 25
    $ renpy.notify("EXP +25")
    jump after_battle1_continue

label after_battle1_f:
    $ battle_1_win
    play sound flee
    pause 1

label after_battle1_continue:

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Second Battle{/size}"


    $ mcside[0].img = "b2_mc"
    $ mcside[1].img = "b2_or"
    $ eside = [battle2_opp]
    $ startNewBattle()
    $ battle_no = 2
    jump group_battle

label after_battle2_w:
    $ battle_2_win = True
    scene black with fade
    $ mcside[0].exp += 25
    $ renpy.notify("EXP +25")

label after_battle2_f:

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Third Battle{/size}"

    $ mcside[0].img = "b3_mc"
    $ mcside[1].img = "b3_or"
    $ eside = [battle3_opp]
    $ startNewBattle()
    $ battle_no = 3
    jump group_battle


label after_battle3_w:
    $ battle_3_win = True
    scene fr027
    with fade
    $ mcside[0].exp += 25
    $ renpy.notify("EXP +25")

    o "Don't allow it to gain momentum!"

    o "Attack it from the side as I stop it from charging!"

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Cut Scene{/size}"



label after_battle3_f:

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Fourth Battle{/size}"

    $ eside = [battle4_boss]
    $ current_enemy = eside[0]
    $ startNewBattle()
    $ battle_no = 4
    jump group_battle2




    label after_battle4_w:
    $ battle_4_win = True

    $ mcside[0].exp += 50
    $ renpy.notify("EXP +50")

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Fifth Battle{/size}"

    $ eside = [battle5_boss]
    $ current_enemy = eside[0]
    $ startNewBattle()
    $ battle_no = 5
    jump group_battle2



    label after_battle5_w:
    $ battle_5_win = True

    $ mcside[0].exp += 25
    $ renpy.notify("EXP +25")

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Sixth Battle{/size}"

    $ mcside[0].img = "b6_mc"
    $ mcside[1].img = "b6_or"
    $ eside = [battle6_opp]
    $ startNewBattle()
    $ battle_no = 6
    jump group_battle


    label after_battle6_w:
    $ battle_6_win = True

    $ mcside[0].exp += 25
    $ renpy.notify("EXP +25")

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Boss Battle{/size}"

    $ mcside[0].img = "b7_mc"
    $ mcside[1].img = "b7_or"
    $ eside = [battle7_boss, battle7_opp]
    $ startNewBattle()
    $ battle_no = 7
    jump group_battle


    label after_battle7_w:
    $ battle_7_win = True

    $ mcside[0].exp += 100
    $ renpy.notify("EXP +100")

    scene black with fade
    scene black with dissolve
    centered "{size=+30}Boss Battle 2{/size}"

    $ mcside[0].img = "b8_mc"
    $ mcside[1].img = "b8_or"
    $ eside = [battle8_boss, battle8_opp]
    $ startNewBattle()
    $ battle_no = 8
    jump group_battle


    label after_battle8_w:
    $ battle_8_win = True
    scene black
    with fade
    $ mcside[0].exp += 100
    $ renpy.notify("EXP +100")
    stop music fadeout 2.0
    play music "audio/Medieval.wav" fadein 2.0

    return
