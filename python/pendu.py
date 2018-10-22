#jeu de pendu avec récupération d'un mot aléatoire sur internet
#https://www.palabrasaleatorias.com/mots-aleatoires.php
#pas d'api donc lecture et parsing du code html retourné

#import graphics a besoin de tkinter pour python (sudo apt install python3-tk)
#et pip3 install graphics.py
#et pip3 install requests

import graphics
##import http.client
import requests
from random import choice
import time
import string

__DEBUG__ = False

def log(text: str):
    if __DEBUG__:
        print(text)

def draw (win, graphList, step, draw=True):
    if step < 8:
        if draw:
            graphList[step -1].draw(win)
        else:
            graphList[step -1].undraw()
    elif step == 8:
        if draw:
            graphList[7].draw(win)
            graphList[8].draw(win)
        else:
            graphList[7].undraw()
            graphList[8].undraw()       
    elif step == 9:
        if draw:
            graphList[9].draw(win)
            graphList[10].draw(win)
        else:
            graphList[9].undraw()
            graphList[10].undraw() 

def find_mot() -> str:
    
    url = 'www.palabrasaleatorias.com'
    try:
        connection = http.client.HTTPSConnection('10.225.92.1',80)
        connection.set_tunnel(url)
        connection.request("GET", "/mots-aleatoires.php?fs=7&fs2=0&Submit=Nouveau+mot")
        response = connection.getresponse()

        if (response.status == 200):
            data=response.read()
            u=data.decode('utf8')
            lines=u.split('\n')
            liste=[]

            for i in range(len(lines)):
                if "color:#6200C5;" in lines[i]:
                    liste.append(lines[i+1].split("<")[0])
        
        connection.close()

    except:
        liste=[]    

    if liste == []:
        liste=["Abracadabrantesque","Simple","Canard","Croquette","Excellent","Tricheur","Python","Football"]

    return choice(liste)

def lettre_in_mot(lettre:str, clair:str, hidden:[]) -> bool:

    found = False
    L = lettre.upper()
    #handling a little more than just french alphabet
    if L == 'A':
        L = 'AÂÀÄÁ'
    elif L == 'C':
        L = 'CÇ'
    elif L == 'E':
        L = 'EÈÉÊË'
    elif L == 'I':
        L = 'IÎÏÍÌ'
    elif L == 'N':
        L = 'NÑ'
    elif L == 'O':
        L ='OÖÒÓÔ'
    elif L== 'U':
        L = 'UÜÛÚÙ'

    for i in range(len(clair)):
        if clair[i] in L:
            hidden[i]=clair[i]
            found = True

    log(hidden)
    return found, hidden

def init_game():
    clair = find_mot().upper()
    cache = []

    #il peut y avoir des mots avec des espaces ou des tirets
    for i in range(len(clair)):
        if clair[i] in (' ','-'):
            cache.append(clair[i])
        else:
            cache.append('*')

    log(cache)
    return clair, cache

def init_graphlist():
    graphList = []

    barre1 = graphics.Line(graphics.Point(550,350), graphics.Point(700,350))
    barre1.setWidth(5)
    graphList.append(barre1)

    barre2 = graphics.Line(graphics.Point(625,350), graphics.Point(625,100))
    barre2.setWidth(5)
    graphList.append(barre2)

    barre3 = graphics.Line(graphics.Point(625,100), graphics.Point(800,100))
    barre3.setWidth(5)
    graphList.append(barre3)

    barre4 = graphics.Line(graphics.Point(625,200), graphics.Point(700,100))
    barre4.setWidth(5)
    graphList.append(barre4)

    barre5 = graphics.Line(graphics.Point(800,100), graphics.Point(800,150))
    barre5.setWidth(5)
    graphList.append(barre5)

    tete = graphics.Circle(graphics.Point(800,175), 25)
    tete.setWidth(5)
    graphList.append(tete)

    corps = graphics.Line(graphics.Point(800,200), graphics.Point(800,300))
    corps.setWidth(5)
    graphList.append(corps)

    bras1 = graphics.Line(graphics.Point(800,230), graphics.Point(770,250))
    bras1.setWidth(5)
    graphList.append(bras1)

    bras2 = graphics.Line(graphics.Point(800,230), graphics.Point(830,250))
    bras2.setWidth(5)
    graphList.append(bras2)
      

    jambe1 = graphics.Line(graphics.Point(800,300), graphics.Point(770,320))
    jambe1.setWidth(5)
    graphList.append(jambe1)

    jambe2 = graphics.Line(graphics.Point(800,300), graphics.Point(830,320))
    jambe2.setWidth(5)
    graphList.append(jambe2)

    return graphList


def main():

    graphList = init_graphlist()

    finished = False
    win = graphics.GraphWin('Le jeu de Pendu', 1000, 600) # give title and dimensions 

    posMessage = graphics.Point(win.getWidth()/2, win.getHeight() -20)
    posCache = graphics.Point(win.getWidth()/2 - 200, 100)
    posLettres = graphics.Point(win.getWidth()/2 - 50, win.getHeight() - 150)
    posTriche = graphics.Point(400, 200)


     
    try:

        while not finished:
            step = 1
            lettres=''

            message = graphics.Text(posMessage, 'Choisis une lettre')
            message.draw(win)

            mot_clair, mot_cache = init_game()

            msgCache = graphics.Text(posCache, ''.join(mot_cache))
            msgCache.setSize(30)
            msgCache.draw(win)

            msgLettres = graphics.Text(posLettres, lettres)
            msgLettres.setSize(30)
            msgLettres.draw(win)

            msgTriche = graphics.Text(posTriche, mot_clair)
            msgTriche.setSize(10)
            if __DEBUG__ :
                msgTriche.draw(win)

            while True:
                tentative = win.getKey()

                if tentative == 'Escape':
                    win.close()
                    break
                
                if tentative.upper() in string.ascii_uppercase:

                    if tentative in lettres:
                        message.undraw()
                        message = graphics.Text(posMessage, "T'es bourré(e) ou quoi ?")
                        message.draw(win)
                        time.sleep(2)
                        message.undraw()
                        message = graphics.Text(posMessage, "Choisis une lettre")
                        message.draw(win)     
                    else:
                        lettres=lettres+tentative
                        msgLettres.undraw()
                        msgLettres = graphics.Text(posLettres, lettres)
                        msgLettres.draw(win)
                        found, mot_cache = lettre_in_mot(tentative, mot_clair, mot_cache)
                        log(mot_cache)
                        if not found:
                            draw(win, graphList, step)
                            if step == 9:
                                message.undraw()
                                message = graphics.Text(posMessage, 'PERDU!')
                                message.setSize(30)
                                message.setTextColor('red')
                                message.draw(win)
                                msgCache.undraw()
                                msgCache = graphics.Text(posCache, mot_clair)
                                msgCache.setSize(30)
                                msgCache.draw(win)
                                break
                            else:
                                step+=1
                        else:
                            msgCache.undraw()
                            msgCache = graphics.Text(posCache, ''.join(mot_cache))
                            msgCache.setSize(30)
                            msgCache.draw(win)

                            if ''.join(mot_cache) == mot_clair:
                                message.undraw()
                                message = graphics.Text(posMessage, 'GAGNÉ!')
                                message.setSize(30)
                                message.setTextColor('red')
                                message.draw(win)
                                break

            time.sleep(2)
            message.undraw()
            message = graphics.Text(posMessage, 'Une autre ?')
            message.setSize(10)
            message.setTextColor('black')
            message.draw(win)
            if win.getKey().upper() not in 'YO':
                finished = True
                win.close()
            else:
                message.undraw()
                msgLettres.undraw()
                msgCache.undraw()
                if __DEBUG__ :
                    msgTriche.undraw()
                for i in range(step,0,-1):
                    draw(win, graphList, i, False)
                

    except graphics.GraphicsError:
        pass

if __name__ == '__main__':
    main()
