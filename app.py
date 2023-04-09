'''

Comment jouer ?

- Utilisation du clavier numérique
- Touche espace pour réinitialiser

'''

##############################################################
# Importations #

import pyxel

##############################################################
# Chargement #

pyxel.init(39,33,title="Morpion")
pyxel.load("res.pyxres")

##############################################################
# Début du programme #

def update():
    affichage()
    tableau()

def draw():
    global j, m
    if pyxel.btnp(pyxel.KEY_KP_SPACE) or pyxel.btnp(pyxel.KEY_SPACE):
        j = 1
        m = [[0,5,10],
            [15,20,25],
            [30,35,40]]

    if j == 1:
        pyxel.blt(3,27,0,0,0,5,3)
        if pyxel.btnp(pyxel.KEY_KP_1) or pyxel.btnp(pyxel.KEY_1):
            if m[0][0] != 46 and m[0][0] != 53:
                m[0][0] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_2) or pyxel.btnp(pyxel.KEY_2):
            if m[0][1] != 46 and m[0][1] != 53:
                m[0][1] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_3) or pyxel.btnp(pyxel.KEY_3):
            if m[0][2] != 46 and m[0][2] != 53:
                m[0][2] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_4) or pyxel.btnp(pyxel.KEY_4):
            if m[1][0] != 46 and m[1][0] != 53:
                m[1][0] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_5) or pyxel.btnp(pyxel.KEY_5):
            if m[1][1] != 46 and m[1][1] != 53:
                m[1][1] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_6) or pyxel.btnp(pyxel.KEY_6):
            if m[1][2] != 46 and m[1][2] != 53:
                m[1][2] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_7) or pyxel.btnp(pyxel.KEY_7):
            if m[2][0] != 46 and m[2][0] != 53:
                m[2][0] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_8) or pyxel.btnp(pyxel.KEY_8):
            if m[2][1] != 46 and m[2][1] != 53:
                m[2][1] = 46
                j = 2
        elif pyxel.btnp(pyxel.KEY_KP_9) or pyxel.btnp(pyxel.KEY_9):
            if m[2][2] != 46 and m[2][2] != 53:
                m[2][2] = 46
                j = 2

    elif j == 2:
        pyxel.blt(31,27,0,0,0,5,3)
        if pyxel.btnp(pyxel.KEY_KP_1) or pyxel.btnp(pyxel.KEY_1):
            if m[0][0] != 46 and m[0][0] != 53:
                m[0][0] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_2) or pyxel.btnp(pyxel.KEY_2):
            if m[0][1] != 46 and m[0][1] != 53:
                m[0][1] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_3) or pyxel.btnp(pyxel.KEY_3):
            if m[0][2] != 46 and m[0][2] != 53:
                m[0][2] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_4) or pyxel.btnp(pyxel.KEY_4):
            if m[1][0] != 46 and m[1][0] != 53:
                m[1][0] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_5) or pyxel.btnp(pyxel.KEY_5):
            if m[1][1] != 46 and m[1][1] != 53:
                m[1][1] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_6) or pyxel.btnp(pyxel.KEY_6):
            if m[1][2] != 46 and m[1][2] != 53:
                m[1][2] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_7) or pyxel.btnp(pyxel.KEY_7):
            if m[2][0] != 46 and m[2][0] != 53:
                m[2][0] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_8) or pyxel.btnp(pyxel.KEY_8):
            if m[2][1] != 46 and m[2][1] != 53:
                m[2][1] = 53
                j = 1
        elif pyxel.btnp(pyxel.KEY_KP_9) or pyxel.btnp(pyxel.KEY_9):
            if m[2][2] != 46 and m[2][2] != 53:
                m[2][2] = 53
                j = 1

    if win1():
        j = 3

    elif win2():
        j = 4

    elif win3():
        j = 5

    if j == 3:
        pyxel.rectb(2,8,7,19,11)
        pyxel.text(4,28,"J1 a win",8)

    elif j == 4:
        pyxel.rectb(30,8,7,19,11)
        pyxel.text(4,28,"J2 a win",8)

    elif j == 5:
        pyxel.rectb(2,8,7,19,13)
        pyxel.rectb(30,8,7,19,13)
        pyxel.text(3,28,"Match nul",8)

def affichage():
    pyxel.cls(0)
    pyxel.blt(1,1,0,0,16,37,5)
    pyxel.blt(3,9,0,0,24,5,11)
    pyxel.blt(31,9,0,6,24,5,11)
    pyxel.blt(3,21,0,46,8,5,5)
    pyxel.blt(31,21,0,53,8,5,5)
    x = 10
    for i in range(4):
        pyxel.line(x,8,x,26,7)
        x += 6
    y = 8
    for i in range(4):
        pyxel.line(10,y,28,y,7)
        y += 6

def tableau():
    pyxel.blt(11,9,0,m[0][0],8,5,5)
    pyxel.blt(17,9,0,m[0][1],8,5,5)
    pyxel.blt(23,9,0,m[0][2],8,5,5)
    pyxel.blt(11,15,0,m[1][0],8,5,5)
    pyxel.blt(17,15,0,m[1][1],8,5,5)
    pyxel.blt(23,15,0,m[1][2],8,5,5)
    pyxel.blt(11,21,0,m[2][0],8,5,5)
    pyxel.blt(17,21,0,m[2][1],8,5,5)
    pyxel.blt(23,21,0,m[2][2],8,5,5)

def win1():
    n = len(m)
    p = 46
    win = None

    for i in range(n):
        win = True
        for j in range(n):
            if m[i][j] != p:
                win = False
        if win:
            return win


    for i in range(n):
        win = True
        for j in range(n):
            if m[j][i] != p:
                win = False
        if win:
            return win

    win = True
    for i in range(n):
        if m[i][i] != p:
            win = False
    if win:
        return win

    win = True
    for i in range(n):
        if m[i][n - 1 - i] != p:
            win = False
    if win:
        return win
    return False

def win2():
    n = len(m)
    p = 53
    win = None

    for i in range(n):
        win = True
        for j in range(n):
            if m[i][j] != p:
                win = False
        if win:
            return win


    for i in range(n):
        win = True
        for j in range(n):
            if m[j][i] != p:
                win = False
        if win:
            return win

    win = True
    for i in range(n):
        if m[i][i] != p:
            win = False
    if win:
        return win

    win = True
    for i in range(n):
        if m[i][n - 1 - i] != p:
            win = False
    if win:
        return win
    return False

def win3():
    n = len(m)
    p1 = 46
    p2 = 53
    draw = True

    for i in range(n):
        for j in range(n):
            if m[i][j] != p1 and m[i][j] != p2:
                draw = False
    if draw:
        return draw
    return False

j = 1
m = [[0,5,10],
    [15,20,25],
    [30,35,40]]

##############################################################
# Fin du programme #

pyxel.run(update, draw)

##############################################################