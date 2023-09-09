screen battle_overlay2():
    add "battle_bg[battle_no]"
    vbox:
        xalign 0.01 yalign 0.03
        spacing 10
        for player in mcside:
            vbox:
                spacing 7
                textbutton "[player.name!u]" style "battlename"
                add "battlescreen_status_full"
                bar style "bar_hp" value AnimatedValue(value=player.curhp, range=player.maxhp, delay=0.25)
                hbox:
                    spacing -40
                    text "HP [player.curhp]/[player.maxhp]" xoffset 140 yoffset -80 style "battle_info"
                    text "[player.weapon_type!u]" style "battle_info" yoffset -55

    vbox:
        xpos 1570 yalign 0.03
        spacing 10
        if eside != []:
            for enemy in eside:
                vbox:
                    spacing 7
                    textbutton "[enemy.name!u]" style "battlename"
                    add "battlescreen_status_full"
                    bar style "bar_hp" value AnimatedValue(value=enemy.curhp, range=enemy.maxhp, delay=0.25)
                    hbox:
                        spacing -40
                        text "HP [enemy.curhp]/[enemy.maxhp]" xoffset 140 yoffset -80 style "battle_info"
                        text "[enemy.weapon_type!u]" style "battle_info" yoffset -55


screen atk_choose2():
    vbox at atk_screen_trans:
        xalign 0.7
        yalign 0.5
        spacing -15
        imagebutton auto "attack_%s" hover_sound "audio/battle/hover.wav" action Return("attack"), SetVariable("message", "who_attack")
        imagebutton auto "defend_%s" hover_sound "audio/battle/hover.wav" action Return("defend") xoffset 20
        imagebutton auto "flee_%s" hover_sound "audio/battle/hover.wav" action Return("flee")


label group_battle2:
    $ players_turn = False
    show screen battle_overlay2
    show screen battle_message

    python:
        players_alive = mcside.copy()
        enemy_alive = eside.copy()

    window hide

    label battle_loop2:
    if battle_no == 4:
        if checkParty2(mcside) == "lost":
            jump battle_lose2
    elif True:
        if checkParty(mcside) == "lost":
            jump battle_lose2

    $ playersChk()

    $ startNewTurn()

    $ party_index = 0

    while party_index < len(mcside):
        $ current_player = mcside[party_index]
        if current_player.curhp > 0:
            if battle_no == 4:
                if checkParty2(eside) == "lost":
                    jump battle_win2
            elif True:
                if checkParty(eside) == "lost":
                    jump battle_win2


            $ players_turn = True

            label atk_choose2_label:
            $ message = "player_turn"
            call screen atk_choose2

            $ action_type = _return

            if action_type == "attack":
                play sound sword
                with vpunch
                $ player_damage = renpy.random.randint(0,2)
                if player_damage == 2:
                    $ player_damage = current_player.atk
                elif True:
                    if current_player.atk <= current_enemy.dfn:
                        $ player_damage = renpy.random.randint(10, 25)
                    elif True:
                        $ player_damage = renpy.random.randint(current_player.atk-10, current_player.atk) - current_enemy.dfn
                $ current_enemy.curhp -= player_damage
                $ message = "p_attack"
                $ playersChk()
                pause

            elif action_type == "defend":
                play sound defend
                with vpunch
                $ current_player.defending = True
                $ message = "p_defend"
                pause

            elif action_type == "flee":
                $ flee_rand = renpy.random.randint(1, 4)
                if flee_rand == 1:
                    $ message = "flee_success"
                    pause
                    jump flee2

                elif True:
                    $ message = "flee_fail"
                    pause
                    $ current_enemy = eside[0]
                    $ player_to_attack = mcside[renpy.random.randint( 0, (len(mcside)-1) )]
                    if current_enemy.atk < player_to_attack.dfn:
                        $ enemy_damage = renpy.random.randint(1,10)
                    elif True:
                        $ enemy_damage = renpy.random.randint(current_enemy.atk-10, current_enemy.atk) - player_to_attack.dfn
                    play channel1 orc_attack
                    play channel2 sword
                    with vpunch
                    $ player_to_attack.curhp -= enemy_damage
                    $ message = "e_attack"
                    pause

        $ players_turn = False

        $ party_index += 1

    if battle_no == 4:
        if checkParty2(eside) == "lost":
            jump battle_win2
    elif True:
        if checkParty(eside) == "lost":
            jump battle_win2


    $ enemy_index = 0
    while enemy_index < len(eside):

        $ current_enemy = eside[enemy_index]

        if current_enemy.curhp > 0:
            if battle_no == 4:
                if checkParty2(mcside) == "lost":
                    jump battle_lose2
            elif True:
                if checkParty(mcside) == "lost":
                    jump battle_lose2


            $ player_to_attack = players_alive[renpy.random.randint( 0, (len(players_alive)-1))]

            if player_to_attack.defending:
                $ def_rand = renpy.random.randint(1, 3)
                if def_rand == 1:
                    play channel1 orc_attack
                    play channel2 sword
                    with vpunch
                    $ enemy_damage = (renpy.random.randint(current_enemy.atk - 10, current_enemy.atk))/2
                    $ player_to_attack.curhp -= enemy_damage
                    $ message = "e_attack"
                    $ playersChk()
                    pause
                elif True:
                    $ message = "defend_success"
                    pause
            elif True:
                $ player_to_attack = players_alive[renpy.random.randint( 0, (len(players_alive)-1))]
                $ enemy_damage = renpy.random.randint(0,2)
                if current_enemy.atk <= player_to_attack.dfn:
                    $ enemy_damage = renpy.random.randint(1,15)
                elif True:
                    if enemy_damage == 2:
                        if player_to_attack.name == "Prince":
                            $ enemy_damage = current_enemy.atk/2
                        elif True:
                            $ enemy_damage = current_enemy.atk
                    elif True:
                        $ enemy_damage = renpy.random.randint(current_enemy.atk-10, current_enemy.atk) - player_to_attack.dfn
                play channel1 orc_attack
                play channel2 sword
                with vpunch
                $ player_to_attack.curhp -= enemy_damage
                $ message = "e_attack"
                $ playersChk()

                pause

        $ enemy_index += 1
    jump battle_loop2

label battle_win2:
    hide screen battle_overlay2
    hide screen battle_message
    if battle_no == 4:
        jump after_battle4_w
    elif battle_no == 5:
        jump after_battle5_w


label battle_lose2:
    if battle_no == 4:
        hide screen battle_overlay2
        hide screen battle_message
        jump after_battle4_w
    elif True:
        hide screen battle_overlay2
        hide screen battle_message
        play sound flee
        scene black with dissolve
        centered "{size=+50}GAME OVER{/size}"
        return


label flee2:
    hide screen battle_overlay2
    hide screen battle_message
    if battle_no == 4:
        jump after_battle4_w
