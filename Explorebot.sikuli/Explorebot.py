# Version 0.46

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
Rcast = Region(903,919,116,59)
Rmyturn = Region(286,0,62,107)
Rmydeck = Region(164,53,312,1021)
Rend = Region(945,525,30,32)
Rskip = Region(893,968,131,70)
Rskip2 = Region(687,821,541,256)
Rsettings = Region(1821,11,87,86)
Rretreat = Region(730,752,451,118)
Ryes = Region(1104,663,116,62)
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
endofbattle = Pattern("endofbattle.png").similar(0.95)
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
Renemy = Region(1390,28,150,1052)
Rsilence = Region(151,54,80,72)
Rsilencebomb = Region(150,288,79,609)
Rdismiss = Region(1029,670,162,51)
Renemyturn = Region(1576,0,50,112)
Rweapon = Region(165,834,307,239)
Rnervnicht = Region(167,15,4,3)
weaponready2 = Pattern("weaponready2.png").similar(0.85)
weaponready3 = Pattern("weaponready3.png").similar(0.85)
silence = Pattern("silence.png").similar(0.92)
mastery = "mastery.png"
dismiss = "dismiss.png"
levelup = Pattern("levelup.png").similar(0.85)
gloryzeichen = Pattern("gloryzeichen.png").similar(0.85)
playagain = "playagain.png"
skip = "skip.png"
settings = "settings.png"
retreat = "retreat.png"
yes = "yes.png"
cast = Pattern("cast.png").exact()
greycast = Pattern("greycast.png").exact()
mapsymbol = "mapsymbol.png"
tobattle = "tobattle.png"
retry = "retry.png"
xzeichen = Pattern("xzeichen.png").similar(0.86)
gnomebag = Pattern("gnomebag.png").similar(0.90)
Rfeld = Region(480,80,960,960)
rot = "rot.png"

def befuellearray(bild,farbe):
    Rfeld.findAll(bild)
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
    for y in range(n):
        for x in range(n):
            if a[y][x] == 1:
                verschiebe = teste(x,y)
                if verschiebe == "runter":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location(x*120+510,(y+1)*120+90))
                    return
                if verschiebe == "hoch":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location(x*120+510,(y-1)*120+90))
                    return
                if verschiebe == "rechts":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location((x+1)*120+510,y*120+90))
                    return
                if verschiebe == "links":
                    click(Location(x*120+510,y*120+90))
                    wait(0.2)
                    click(Location((x-1)*120+510,y*120+90))
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

Rend.onAppear(endofbattle, endfunktion)
Rend.observeInBackground(FOREVER)

def petfunktion():
    Rdismiss.wait(dismiss, FOREVER)
    Rdismiss.click(dismiss)
    wait(1)

def retreattriggerfunktion():        
    if Rsettings.exists(settings,0):
        try:        
            Rsettings.click(settings)        
            if not Rretreat.exists(retreat,1):            
                Rsettings.click(settings)        
            if Rretreat.exists(retreat,1):
                Rretreat.click(retreat)        
            if not Ryes.exists(yes,1):            
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
            pass

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
            if not Rmap.exists(mapsymbol, 0):        
                type(Key.ESC)
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
        wait(0.3)
        tributabholen = 0
        retreattrigger = False
        schongestartet = False
        retreatet = True


Rmiddle.click()
wait(0.3)
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
    except FindFailed:
        while True:
            if Rerror.exists(retry,0):
                Rerror.click(retry)
            if Rfirstbomb.exists(bomb,0):
                break
    Renemyturn.waitVanish(startIndicator,5)
    Rfirstbomb.click()
    if not Rcast.exists(cast,1):
        Rfirstbomb.click()
    Rcast.click()
    wait(2.5)
    if Rsettings.exists(settings,0):
        machweiter = True
    silenced = False
    while machweiter:
        if Rmyturn.exists(startIndicator,0) and not Renemyturn.exists(startIndicator,0) and machweiter:
            if (Rsunbird2.exists(sunbirdready2,0) or Rsunbird3.exists(sunbirdready3,0) or Rsunbird4.exists(sunbirdready4,0)) and not Rsilence.exists(silence,0) and machweiter:
                if Rend.exists(endofbattle,0):
                    break
                Rsunbird3.click()                    
                if not Rcast.exists(cast,0.3):
                    if Rcast.exists(greycast,0):
                        Rnervnicht.click()
                        Rnervnicht.click()
                        wait(0.1)
                        continue
                    Rsunbird2.click()                        
                Rcast.click()
                wait(2.5)
                continue
            if Rmydeck.exists(bomb,0) and machweiter and not Rsilencebomb.exists(silence,0):
                if machweiter:
                    try:
                        Rmydeck.click(bomb)
                        if not Rcast.exists(cast,0.3):
                            if Rcast.exists(greycast,0):
                                Rnervnicht.click()
                                Rnervnicht.click()
                                wait(0.1)
                                continue
                            Rmydeck.click(bomb)
                        Rcast.click()
                        wait(2.5)
                        continue
                    except FindFailed:
                        continue
            if not machweiter:
                break
            if (Rsunbird2.exists(sunbirdready2,0) or Rsunbird3.exists(sunbirdready3,0) or Rsunbird4.exists(sunbirdready4,0)) and not Rsilence.exists(silence,0) and machweiter:
                Rsunbird2.click()                    
                if not Rcast.exists(cast,1):                                                   
                    Rsunbird2.click()                        
                Rcast.click()
                wait(2)
                continue
            if machweiter:
                n = 8
                a = [[0] * n for i in range(n)]
                befuellearray(rot,1)
                matchrot()
                wait(2)
                continue
#            if (Rweapon.exists(weaponready,0) or Rweapon.exists(weaponready2,0) or Rweapon.exists(weaponready3,0)) and machweiter:
#                Rweapon.click()                    
#                if not Rcast.exists(cast,1):                                                   
#                    Rweapon.click()                        
#                Rcast.click()
#                wait(2)
#                continue
            wait(1)
            if machweiter:
                retreattriggerfunktion()
            break
    while True:
        if not Rend.exists(endofbattle,0):
                break
        wait(0.2)
    retreatfunktion()
    if retreatet:
        continue
    if not running:
        break
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
    if tributabholen > 45:
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
    
