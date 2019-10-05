# Version 0.58

import copy
Settings.MoveMouseDelay = 0.08
Settings.MinSimilarity = 0.80
Settings.WaitScanRate = 10
Settings.ObserveScanRate = 10
running = True
retreattrigger = False

def runHotkey(event):
        global running
        running = False

Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

Rkingdom = Region(1250,414,5,3)
Rbattlestart = Region(854,987,212,62)
Rfirstbomb = Region(155,319,333,251)
Rcast = Region(894,918,134,68)
Rmyturn = Region(286,0,62,107)
Rmydeck = Region(164,53,312,1021)
Rendold = Region(945,525,30,32)
Rend = Region(831,776,49,31)
Rskip = Region(893,968,131,70)
Rskip2 = Region(687,821,541,256)
Rsettings = Region(1821,11,87,86)
Rretreat = Region(873,1002,173,56)
Ryes = Region(1110,668,98,53)
Rtribut = Region(847,884,215,191)
tribut = Pattern("tribut.png").similar(0.80)
Rcontinu = Region(343,817,1205,253)
continu = Pattern("continu.png").similar(0.80)
Roffer = Region(824,29,271,93)
offer = "offer.png"
startIndicator = Pattern("turnicon.png").exact()
startIndicator2 = Pattern("turnicon2.png").exact()
startIndicator3 = Pattern("turnicon3.png").exact()
bomb = "bomb.png"
bomb2 = Pattern("bomb.png").similar(0.95)
bomb3 = Pattern("bomb2.png").similar(0.95)
bomb4 = Pattern("bomb3.png").similar(0.95)
sunbird = Pattern("sunbird.png").similar(0.90)
sunbirdready = Pattern("sunbirdready.png").similar(0.90)
sunbirdready2 = Pattern("sunbirdready2.png").similar(0.95)
sunbirdready3 = Pattern("sunbirdready3.png").similar(0.93)
sunbirdready4 = Pattern("sunbirdready4.png").similar(0.95)
sunbirdreadyent = "sunbirdreadyent.png"
sunbirdreadyweb = "sunbirdreadyweb.png"
sunbirdreadymark = Pattern("sunbirdreadymark.png").similar(0.75)
sunbirdreadydeath = Pattern("sunbirdreadydeath.png").similar(0.75)
endofbattleold = Pattern("endofbattle.png").similar(0.95)
endofbattle = "endofbattle.png"
winbiatch = "winbiatch.png"
Rwinbiatch = Region(818,820,70,80)
Rplayagain = Region(1222,972,248,70)
Rmap =Region(5,305,94,82)
Rmiddle = Region(955,534,3,3)
Rsunbird = Region(158,62,315,245)
Rsunbird2 = Region(202,212,22,23)
Rsunbird3 = Region(426,219,33,26)
Rsunbird4 = Region(404,77,62,54)
Rerror = Region(808,631,306,125)
Rneunuhr = Region(225,321,358,283)
Rxzeichen = Region(1322,0,458,339)
Rlevelup = Region(1023,963,23,28)
Rmastery = Region(1519,316,266,508)
Rlevelup2 = Region(1159,559,6,5)
Renemy = Region(1426,25,336,1050)
Rsilence = Region(151,54,80,72)
Rsilencebomb = Region(150,288,79,609)
Rsilenceweapon = Region(135,801,105,101)
Rdismiss = Region(1052,683,187,62)
Renemyturn = Region(1576,0,50,112)
Rweapon = Region(166,840,305,222)
Rnervnicht = Region(167,15,4,3)
weaponready = Pattern("weaponready.png").similar(0.94)
weaponready2 = Pattern("weaponready2.png").similar(0.93)
weaponready3 = Pattern("weaponready3.png").similar(0.93)
silence = Pattern("silence.png").similar(0.92)
mastery = "mastery.png"
dismiss = "dismiss.png"
levelup = Pattern("levelup.png").similar(0.85)
gloryzeichen = Pattern("gloryzeichen.png").similar(0.85)
playagain = "playagain.png"
skip = "skip.png"
settings = "settings.png"
retreat = Pattern("retreat.png").similar(0.85)
yes = Pattern("yes.png").similar(0.82)
cast = Pattern("cast.png").similar(0.85)
greycast = Pattern("greycast.png").similar(0.86)
mapsymbol = "mapsymbol.png"
tobattle = "tobattle.png"
retry = "retry.png"
xzeichen = Pattern("xzeichen.png").similar(0.86)
gnomebag = Pattern("gnomebag.png").similar(0.92)
gnome = Pattern("gnome.png").similar(0.91)
soulgnome = Pattern("soulgnome.png").similar(0.90)
eventgnome = Pattern("eventnome.png").similar(0.89)
Rfeld = Region(480,80,960,960)
rot = "rot.png"
lila = "lila.png"
gruen = "gruen.png"
blau = "blau.png"

def befuellearray(bild,farbe):
    try:
        Rfeld.findAll(bild)
    except FindFailed:
        return
    mm = Rfeld.getLastMatches()
    while mm.hasNext():
        cord = mm.next().getTarget()
        a[(cord.y-80)/120][(cord.x-480)/120]=farbe

def teste2(b):
    for y in range(n):
        for x in range(n):
            if b[y][x] == 1 and x < 6:
                if b[y][x+1] == 1:
                    if b[y][x+2] == 1:
                        return 1
            if b[y][x] == 1 and y < 6:
                if b[y+1][x] == 1:
                    if b[y+2][x] == 1:
                        return 1
            if b[y][x] == 1 and y > 1:
                if b[y-1][x] == 1:
                    if b[y-2][x] == 1:
                        return 1
            if b[y][x] == 1 and x > 1:
                if b[y][x-1] == 1:
                    if b[y][x-2] == 1:
                        return 1

def teste(x,y):
    if runter(x,y) == 1:
        return "runter"
    if hoch(x,y) == 1:
        return "hoch"
    if rechts(x,y) == 1:
        return "rechts"
    if links(x,y) == 1:
        return "links"

def runter(x,y):
    b = copy.deepcopy(a)
    if y<7:
        b[y][x]=0
        temp = b[y+1][x]
        b[y+1][x]=1
        if teste2(b) == 1:
            return 1
#        b[y][x]=1
#        b[y+1][x]=temp

def hoch(x,y):
    b = copy.deepcopy(a)
    if y<0:
        b[y][x]=0
        b[y-1][x]=1
        if teste2(b) == 1:
            return 1


def rechts(x,y):
    b = copy.deepcopy(a)
    if x<7:
        b[y][x]=0
        b[y][x+1]=1
        if teste2(b) == 1:
            return 1

def links(x,y):
    b = copy.deepcopy(a)
    if x>0:
        b[y][x]=0
        b[y][x-1]=1
        if teste2(b) == 1:
            return 1

def matchrot():
    global gemacht
    gemacht = 0
    for y in range(n):
        for x in range(n):
            if a[y][x] == 1:
                verschiebe = teste(x,y)
                if verschiebe == "runter":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location(x*120+510,(y+1)*120+90))
                    gemacht = 1
                    return
                elif verschiebe == "hoch":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location(x*120+510,(y-1)*120+90))
                    gemacht = 1
                    return
                elif verschiebe == "rechts":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location((x+1)*120+510,y*120+90))
                    gemacht = 1
                    return
                elif verschiebe == "links":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location((x-1)*120+510,y*120+90))
                    gemacht = 1
                    return

leveluptrigger = False
def levelupfunktion():
    Rlevelup.wait(levelup, FOREVER)
    Rlevelup.click()
    Rmastery.wait(mastery, FOREVER)        
    Rlevelup2.click()  
    wait(1)
    if not Rbattlestart.exists(tobattle):
        Rlevelup2.click()


machweiter = True
def endfunktion(event):
    global machweiter
    machweiter = False
    wait(7)
    event.repeat()

#Rend.onAppear(endofbattle, endfunktion)
#Rend.observeInBackground(FOREVER)

def petfunktion():
    Rdismiss.wait(dismiss, FOREVER)
    Rdismiss.click(dismiss)
    wait(1)
    
def sanitycheck():
    global machweiter
    if Rcast.exists(cast,0) or Rcast.exists(greycast,0):
        wait(0.1)
        Rnervnicht.click()
        return
    if Renemyturn.exists(startIndicator,0):
        Renemyturn.waitVanish(startIndicator,10)
    if Rsettings.exists(settings,0):
        try:
            Rsettings.click(settings)
            if not Rretreat.exists(retreat,1):       
                machweiter = False
            else:
                Rnervnicht.click()
        except FindFailed: 
            machweiter = False 
    else:
        machweiter = False
    
def retreattriggerfunktion():
    global machweiter
    if Rsettings.exists(settings,0):
        try:        
            Rsettings.click(settings) 
            if not Rretreat.exists(retreat,1): 
                wait(0.3)
                Rsettings.click(settings) 
            wait(0.3)
            if Rretreat.exists(retreat,1):
                wait(0.3)
                Rretreat.click(retreat)
            if not Ryes.exists(yes,1): 
                wait(0.3)
                Rretreat.click(retreat)        
            wait(0.5)
            if Ryes.exists(yes,1):
                Ryes.click(yes)
            if not Rmap.exists(mapsymbol,1) and Ryes.exists(yes,0):
                try:
                    Ryes.click(yes)
                except FindFailed:
                    pass
            global retreattrigger
            retreattrigger = True
        except FindFailed:
            machweiter = False

retreatet = False
def retreatfunktion():
    global retreattrigger
    global retreatet
    global schongestartet
    global tributabholen
    if retreattrigger:
        Rmap.exists(mapsymbol, 5)
        if not Rmap.exists(mapsymbol, 0):        
            type(Key.ESC)
            Rmap.exists(mapsymbol, 5)
            while True:
                if not Rmap.exists(mapsymbol, 0):        
                    type(Key.ESC)
                    wait(3)
                    continue
                break
        if not Rmap.exists(mapsymbol, 0) and Rxzeichen.exists(xzeichen,0):
            Rxzeichen.click(xzeichen)    
        wait(0.2)
        while True:
            if Rxzeichen.exists(xzeichen,0):
                Rxzeichen.click(xzeichen)
            if not Rend.exists(endofbattle,0) and not Rxzeichen.exists(xzeichen,0):
                break
            wait(0.2)
        if Rtribut.exists(tribut,1):
            Rtribut.click()
            if Rskip2.exists(skip,10):
                Rskip.click()
                wait(0.4)
                if Rskip2.exists(skip,0):
                    Rskip.click() 
            if Rcontinu.exists(continu,10):
                Rcontinu.click()
                wait(0.4)
                if Rcontinu.exists(continu,0):
                    Rcontinu.click()
        if Rxzeichen.exists(xzeichen,0):
                Rxzeichen.click(xzeichen)
        Rmiddle.click()
        if not Rxzeichen.exists(xzeichen,0):
            Rmiddle.click()
        wait(0.3)
        Rkingdom.click()
        if Rxzeichen.exists(xzeichen,0):
            Rkingdom.click()
            wait(0.3)
            Rkingdom.click()
        wait(0.3)
        tributabholen = 0
        retreattrigger = False
        schongestartet = False
        retreatet = True


Rmiddle.click()
wait(0.8)
Rkingdom.click()
wait(0.3)
schongestartet = False
tributabholen = 0
while(running):
    tributabholen += 1
    retreatet = False
    machweiter = True
    if not schongestartet:
        Rbattlestart.wait(tobattle, FOREVER)
        Rplayagain.click()
    try:
        Rfirstbomb.wait(bomb, 10)
#        if Renemy.exists(gnomebag,0):
#            while True:
#                if Renemy.exists(eventgnome,0):
#                    break
#                if Renemy.exists(gnome,0) or Renemy.exists(soulgnome,0):
#                    retreattriggerfunktion()
#                    retreatfunktion()
#                    if retreatet:
#                        break
#                wait(0.2)
#            if retreatet:
#                continue
    except FindFailed:
        while True:
            if Rerror.exists(retry,0):
                Rerror.click(retry)
            if Rfirstbomb.exists(bomb,0):
                break
    Renemyturn.waitVanish(startIndicator,5)
    Rfirstbomb.click()
    wait(0.1)
    if not Rcast.exists(cast,1):
        Rfirstbomb.click()
    Rcast.click()
    wait(2.5)
    if Rsettings.exists(settings,0):
        machweiter = True
    silenced = False
    while machweiter:
        if Rcast.exists(greycast,0):
            Rnervnicht.click()
            wait(0.1)
            continue
        if Rcast.exists(cast,0):
            Rcast.click()
            wait(0.1)
            if Rcast.exists(cast,0):
                Rcast.click()
            wait(2.5) 
            continue
        if Rmyturn.exists(startIndicator,0) and not Renemyturn.exists(startIndicator,0):
            if (Rsunbird2.exists(sunbirdready2,0) or Rsunbird3.exists(sunbirdready3,0) or Rsunbird4.exists(sunbirdready4,0)) and not Rsilence.exists(silence,0) and machweiter:
                Rsunbird3.click()
                if not Rcast.exists(cast,0.2):
                    #wait(0.2)
                    if Rcast.exists(greycast,0.2):
                        wait(0.1)
                        Rnervnicht.click()
                        Rnervnicht.click()
                        wait(0.1)
                        continue
                    #wait(0.1)
                    Rsunbird2.click()
                Rcast.click()
                wait(0.1)
                if Rcast.exists(cast,0):
                    Rcast.click()
                wait(2.5)
                continue
            if Rmydeck.exists(bomb,0) and not Rsilencebomb.exists(silence,0) and machweiter:
                try:
                    Rmydeck.click(bomb)
                    if not Rcast.exists(cast,0.2):
                        #wait(0.2)
                        if Rcast.exists(greycast,0.2):
                            wait(0.1)
                            Rnervnicht.click()
                            Rnervnicht.click()
                            wait(0.1)
                            continue
                        else:
                            machweiter = False
                            break
                        Rmydeck.click(bomb)
                    Rcast.click()
                    wait(0.1)
                    if Rcast.exists(cast,0):
                        Rcast.click()
                    wait(2.5)
                    continue
                except FindFailed:
                    if Rcast.exists(greycast,0.1):
                        Rnervnicht.click()
                        Rnervnicht.click()
                        wait(0.1)
                        continue
                    continue
            if not Rsettings.exists(settings,0):
                break
            if (Rsunbird2.exists(sunbirdready2,0) or Rsunbird3.exists(sunbirdready3,0) or Rsunbird4.exists(sunbirdready4,0)) and not Rsilence.exists(silence,0) and machweiter:
                Rsunbird2.click()                    
                if not Rcast.exists(cast,1):                                                   
                    Rsunbird2.click()                        
                Rcast.click()
                wait(2)
                continue
            if not Rsettings.exists(settings,0):
                break
            if (Rweapon.exists(weaponready,0) or Rweapon.exists(weaponready2,0) or Rweapon.exists(weaponready3,0)) and not Rsilenceweapon.exists(silence,0) and machweiter:
                Rweapon.click()                    
                if not Rcast.exists(cast,1):                                                   
                    Rweapon.click()                        
                Rcast.click()
                wait(2)
                continue
            if not Rsettings.exists(settings,0):
                break
            sanitycheck()
            if machweiter:
                n = 8
                a = [[0] * n for i in range(n)]
                befuellearray(rot,1)
                matchrot()
                if gemacht == 1:    
                    wait(2)
                    continue
            if machweiter:
                n = 8
                a = [[0] * n for i in range(n)]
                befuellearray(lila,1)
                matchrot()
                if gemacht == 1:    
                    wait(2)
                    continue 
            wait(0.5)
            if machweiter:
                retreattriggerfunktion()
            break
        if Rsettings.exists(settings,0.4):
            continue
        else:
            break
#    wait(0.2)
    retreatfunktion()
    if retreatet:
        continue
    if not running:
        break
    if not Rplayagain.exists(playagain,0):
        try:
            Rskip.wait(skip, 5)
        except FindFailed:
            while True:
                if Rerror.exists(retry,0):
                    Rerror.click(retry)
                if Rskip.exists(skip,0):
                    break
                if Rplayagain.exists(playagain,0):
                    break
    if Rskip.exists(skip,0):
        Rskip.click()
        wait(0.1)
    retreattriggerfunktion()
    retreatfunktion()
    if retreatet:
        continue
    Rplayagain.wait(playagain, FOREVER)
    Rplayagain.click()
    if not Rbattlestart.exists(tobattle,2):
        if Rdismiss.exists(dismiss,0):
            petfunktion()
            if Rplayagain.exists(playagain,2):
                Rplayagain.click()
    schongestartet = False
    if tributabholen > 30:
        if Rbattlestart.exists(tobattle,1):
            type(Key.ESC)
            retreattrigger = True
            retreatfunktion()
    if Rbattlestart.exists(tobattle,1):
        Rbattlestart.click(tobattle)
        schongestartet = True
    elif Rlevelup.exists(levelup,0):
        levelupfunktion()
        Rbattlestart.wait(tobattle, 15)
        Rbattlestart.click()
        schongestartet = True
    
