init python:
    class Characters():
        def __init__(self, name, atk, dfn, maxhp, exp = 0, img= None, skills=[], defending=False, weapon_type=[], skill_left = 0, dead = False):
            self.name = name
            self.atk = atk
            self.dfn = dfn
            self.img = img
            self.maxhp = maxhp
            self.curhp = maxhp
            self.exp = exp
            self.skills = skills
            self.defending = defending
            self.weapon_type = weapon_type
            self.skill_left = skill_left
            self.dead = dead


    def startNewTurn():
        for member in mcside:
            if member.defending:
                member.defending = False

    def checkParty(x):
        for member in x:
            if member.curhp > 0:
                return "ok"
        return "lost"

    def checkParty2(x):
        for member in x:
            if member.curhp < 30:
                return "lost"
        return "ok"

    def playersChk():
        for p in mcside:
            if p.curhp <= 0 and not p.dead:
                p.dead = True
                koplayer = p.name
                message = "player_dead"
                renpy.pause
                players_alive.remove(p)
            if p.curhp < 0:
                p.curhp = 0
        for e in eside:
            if e.curhp <= 0 and not e.dead:
                e.dead = True
                koplayer = e.name
                message = "player_ko"
                renpy.pause
                enemy_alive.remove(e)
            if e.curhp < 0:
                e.curhp = 0

    def startNewBattle():
        for c in mcside:
            c.curhp = c.maxhp
        for c in mcside:
            if c.dead == True:
                c.dead = False
                c.curhp = c.maxhp
        mcside[0].skill_left = 1
