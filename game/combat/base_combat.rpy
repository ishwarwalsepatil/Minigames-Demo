screen battle_overlay():
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

    for player in mcside:
        if not player.dead:
            add player.img + "_idle"

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

    if eside != []:
        for enemy in eside:
            if not enemy.dead:
                add enemy.img + "_idle"


screen target_select():
    if eside != []:
        for i, enemy in enumerate(eside):
            vbox:
                xalign 0.5
                if players_turn and enemy.curhp > 0:
                    if no_of_target == 1:
                        imagebutton auto enemy.img + "_%s" hover_sound "audio/battle/hover.wav" action Return(i) focus_mask True
                    elif no_of_target == 2:
                        imagebutton:
                            focus_mask True
                            idle enemy.img + "_hover"
                            hover enemy.img + "_hover"
                            hover_sound "audio/battle/hover.wav"
                            action Return(None)
                    elif no_of_target == 0:
                        timer 0.01 action Return(None)

screen atk_choose():
    vbox at atk_screen_trans:
        xalign 0.7
        yalign 0.5
        spacing -15
        imagebutton auto "attack_%s" hover_sound "audio/battle/hover.wav" action Return("attack"), SetVariable("message", "who_attack"), SetVariable("no_of_target", 1)
        imagebutton auto "skills_%s" hover_sound "audio/battle/hover.wav" action Return("skills"), SetVariable("message", "who_attack") xoffset 20
        imagebutton auto "defend_%s" hover_sound "audio/battle/hover.wav" action Return("defend") xoffset 20
        if 6 <= battle_no <= 8:
            imagebutton idle "flee_disabled" action NullAction()
        else:
            imagebutton auto "flee_%s" hover_sound "audio/battle/hover.wav" action Return("flee")


screen skills_choose():
    vbox at atk_screen_trans:
        xalign 0.8
        yalign 0.4
        spacing -10
        if len(current_player.skills) > 0:
            if current_player.skill_left == 0:
                for skills in current_player.skills:
                    imagebutton idle skills[0] + "_disabled" action NullAction()
                imagebutton auto "back_%s" hover_sound "audio/battle/hover.wav" action Return(0)
            else:
                for skills in current_player.skills:
                    imagebutton auto skills[0] + "_%s" action Return(skills[0]), SetVariable("no_of_target", skills[1])
                imagebutton auto "back_%s" hover_sound "audio/battle/hover.wav" action Return(0)
        else:
            imagebutton auto "back_%s" hover_sound "audio/battle/hover.wav" action Return(0)

label group_battle:
    $ players_turn = False
    show screen battle_overlay
    show screen battle_message

    python:
        players_alive = mcside.copy()
        enemy_alive = eside.copy()

    window hide

    label battle_loop:
    if checkParty(mcside) == "lost":
        jump battle_lose

    $ playersChk()
    $ startNewTurn()

    $ party_index = 0

    while party_index < len(mcside):
        $ current_player = mcside[party_index]
        if current_player.curhp > 0:
            if checkParty(eside) == "lost":
                jump battle_win

            $ players_turn = True

            label atk_choose_label:
            $ message = "player_turn"
            call screen atk_choose

            $ action_type = _return

            if action_type == "attack":
                call screen target_select
                $ actor = _return
                play sound sword
                with vpunch
                $ player_damage = renpy.random.randint(0,2)
                if player_damage == 2:
                    $ player_damage = renpy.random.randint(current_player.atk-10, current_player.atk)
                elif True:
                    if current_player.atk <= eside[actor].dfn:
                        $ player_damage = renpy.random.randint(10, 25)
                    elif True:
                        $ player_damage = renpy.random.randint(current_player.atk-10, current_player.atk) - eside[actor].dfn
                $ eside[actor].curhp -= player_damage
                $ message = "p_attack"
                $ playersChk()
                pause

            elif action_type == "skills":
                if len(current_player.skills) == 0:
                    $ message = "no_skills"
                elif current_player.skill_left == 0:
                    $ message = "no_skill"
                call screen skills_choose
                $ skill_used = _return
                while skill_used == 0:
                    jump atk_choose_label
                call screen target_select
                $ actor = _return
                call skills_label from _call_skills_label
                $ playersChk()

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
                    jump flee
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

    if checkParty(eside) == "lost":
        jump battle_win

    $ enemy_index = 0
    while enemy_index < len(eside):

        $ current_enemy = eside[enemy_index]

        if current_enemy.curhp > 0:
            if checkParty(mcside) == "lost":
                jump battle_lose

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
    jump battle_loop


label skills_label:
    if skill_used == "royal_focus":
        play channel1 sword
        play channel2 focus
        $ player_damage = current_player.atk * 2
        $ eside[actor].curhp -= player_damage
        $ current_player.skill_left -= 1
        $ message = "p_skill"
        $ playersChk()
        pause
    return

label battle_win:
    hide screen battle_overlay
    hide screen battle_message
    if battle_no == 1:
        jump after_battle1_w
    elif battle_no == 2:
        jump after_battle2_w
    elif battle_no == 3:
        jump after_battle3_w
    elif battle_no == 4:
        jump after_battle4_w
    elif battle_no == 5:
        jump after_battle5_w
    elif battle_no == 6:
        jump after_battle6_w
    elif battle_no == 7:
        jump after_battle7_w
    elif battle_no == 8:
        jump after_battle8_w


label battle_lose:
    hide screen battle_overlay
    hide screen battle_message
    play sound flee
    scene black with dissolve
    centered "{size=+50}GAME OVER{/size}"
    return

label flee:
    hide screen battle_overlay
    hide screen battle_message
    if battle_no == 1:
        jump after_battle1_f
    elif battle_no == 2:
        jump after_battle2_f
    elif battle_no == 3:
        jump after_battle3_f
    elif battle_no == 4:
        jump after_battle4_w



screen battle_message():
    frame:
        xalign 1.0
        yalign 1.0
        background "battle_log2"
        xminimum 424
        yminimum 116
        has hbox:
            xalign 0.5
            yalign 0.5

        if message == "player_turn":
            text "[current_player.name], it's your turn now." style "battle_text"
        elif message == "p_attack":
            text "Damage dealt - [player_damage]hp" style "battle_text"
        elif message == "p_skill":
            text "Damage dealt - [player_damage]hp" style "battle_text"
        elif message == "p_defend":
            text "Defenses are up" style "battle_text"
        elif message == "flee_fail":
            text "Where do you think you are going argh!!" style "battle_text"
        elif message == "flee_success":
            text "That was... waste of my time" style "battle_text"
        elif message == "no_skill":
            text "You have used up your all skills for this battle" style "battle_text"
        elif message == "e_attack":
            text "Rrr! {i}*[current_enemy.name] attacks*{/i} (damage dealt - [enemy_damage]hp)" style "battle_text"
        elif message == "defend_success":
            text "Attack succesfully blocked " style "battle_text"
        elif message == "who_attack":
            text "Who do you want to attack?" style "battle_text"
        elif message == "no_skills":
            text "huh seems like this character doesn't have any skills yet" style "battle_text"
        elif message == "player_dead":
            text "You fought bravely rip" style "battle_text"
        elif message == "none":
            text ""
