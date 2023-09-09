default name = ""
default no_of_target = 3
default message = ""
default players_alive = []
default enemy_alive = []
default battle_no = 0
default player_turn = False


default battle_1_win = False
default battle_2_win = False
default battle_3_win = False
default battle_4_win = False
default battle_5_win = False
default battle_6_win = False
default battle_7_win = False
default battle_8_win = False

transform atk_screen_trans:
    zoom 0.2
    xalign 0.75
    easein_quart 1 zoom 1

style battle_text:
    font "MavenPro-Regular.ttf"
    size 23
    color "#000000"
    xmaximum 400

style battlename is button:
    background Frame("battlescreen_name")
    xminimum 340
    yminimum 26

style battlename_text is text:
    font "MavenPro-Regular.ttf"
    size 27
    color "#3e372c"
    xalign 0.5
    yalign 0.7

style battle_info:
    font "seguiemj.ttf"
    size 22
    color "#3e372c"

init python:
    style.bar_hp = Style(style.default)
    style.bar_hp.left_bar = Frame("images/CustomUI/Combat/hp_bar_full.png")
    style.bar_hp.right_bar = Frame("images/CustomUI/Combat/hp_bar_empty.png")
    style.bar_hp.xmaximum = 340
    style.bar_hp.ymaximum = 11


default mcb = Characters("Prince", 50, 35, 150, exp = 0, img = "b1_mc", weapon_type = "steel sword", skill_left = 1, skills=[])

default orb = Characters("Olivia", 100, 100, 300, img = "b1_or", weapon_type = "steel sword", skills=[])

default battle1_opp = Characters("Orcs", 50, 20, 200, img = "b1_op", weapon_type = "steel axe")

default battle2_opp = Characters("Orcs", 75, 30, 300, img = "b2_op", weapon_type = "steel axe")

default battle3_opp = Characters("Orcs", 100, 40, 400, img = "b3_op", weapon_type = "steel axe")

default battle4_boss = Characters("Ogre", 100, 40, 800, img = "", weapon_type = "steel axe")

default battle5_boss = Characters("Female Orc", 40, 30, 200, img = "", weapon_type = "steel axe")

default battle6_opp = Characters("Orcs", 60, 30, 240, img = "b6_op", weapon_type = "steel axe")

default battle7_opp = Characters("Orcs", 60, 30, 240, img = "b7_op", weapon_type = "steel axe")

default battle7_boss = Characters("Orcs", 50, 30, 200, img = "b7_boss", weapon_type = "steel axe")

default battle8_opp = Characters("Orcs", 80, 40, 320, img = "b8_op", weapon_type = "steel axe")

default battle8_boss = Characters("Orcs", 40, 20, 140, img = "b8_boss", weapon_type = "steel axe")
