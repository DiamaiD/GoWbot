Settings.MoveMouseDelay = 0.0
Settings.MinSimilarity = 0.80
Settings.WaitScanRate = 10
Settings.ObserveScanRate = 5
running=True
retreattrigger = False
waitformetofinish = False

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
Rend = Region(707,413,467,307)
Rskip = Region(893,968,131,70)
Rskip2 = Region(687,821,541,256)
Rsettings = Region(1821,11,87,86)
Rretreat = Region(852,724,221,97)
Ryes = Region(1104,663,116,62)
Rtribut = Region(847,884,215,191)
tribut = Pattern("tribut.png").similar(0.80)
Rcontinu = Region(343,817,1205,253)
continu = Pattern("continu.png").similar(0.80)
startIndicator = Pattern("turnicon.png").exact()
bomb = Pattern("bomb.png").similar(0.95)
sunbird = Pattern("sunbird.png").similar(0.90)
sunbirdready = Pattern("sunbirdready.png").similar(0.90)
sunbirdready2 = "sunbirdready2.png"
sunbirdreadyent = "sunbirdreadyent.png"
sunbirdreadyweb = "sunbirdreadyweb.png"
sunbirdreadymark = Pattern("sunbirdreadymark.png").similar(0.75)
sunbirdreadydeath = Pattern("sunbirdreadydeath.png").similar(0.75)
endofbattle = Pattern("endofbattle.png").similar(0.60)
Rplayagain = Region(1222,972,248,70)
Rmap =Region(5,305,94,82)
Rmiddle = Region(955,534,3,3)
Rsunbird = Region(158,62,315,245)
Rsunbird2 = Region(157,205,85,37)
Rerror = Region(808,631,306,125)
Rneunuhr = Region(225,321,358,283)
Rxzeichen = Region(1322,0,458,339)
Rlevelup = Region(793,886,319,156)
Rmastery = Region(1519,316,266,508)
Rlevelup2 = Region(1159,559,6,5)
Renemy = Region(1390,28,150,1052)
Rsilence = Region(151,54,80,72)
silence = Pattern("silence.png").similar(0.92)
mastery = "mastery.png"
levelup = Pattern("levelup.png").similar(0.85)
gloryzeichen = Pattern("gloryzeichen.png").similar(0.85)
playagain = "playagain.png"
skip = "skip.png"
settings = "settings.png"
retreat = "retreat.png"
yes = "yes.png"
cast = "cast.png"
mapsymbol = "mapsymbol.png"
tobattle = "tobattle.png"
retry = "retry.png"
xzeichen = Pattern("xzeichen.png").similar(0.86)
gnomebag = Pattern("gnomebag.png").similar(0.90)

#def gnomefunktion(event):
#    gnomezahl +=1
#    event.repeat()

#Renemydeck.onAppear(gnomebag, gnomefunktion)
#Renemydeck.observe(FOREVER, background = True)

leveluptrigger = False
def levelupfunktion(event):                
    Rlevelup.click(levelup)
    Rmastery.wait(mastery, FOREVER)        
    Rlevelup2.click()  
    wait(1)
    if not Rbattlestart.exists(tobattle):
        Rlevelup2.click()
    event.repeat()
    
#Rlevelup.onAppear(levelup, levelupfunktion)
#Rlevelup.observe(FOREVER, background = True)

def neuertag(event):
    Rerror.click()
    wait(5)
    Rxzeichen.click(xzeichen)
    wait(5)
    Rxzeichen.click(xzeichen)
    wait(5)
    event.repeat()

errormeldung = False
def errormeldungfunktion(event):
    Rerror.click(retry)
    event.repeat()
#Rerror.onAppear(retry, errormeldungfunktion)
#Rerror.observe(FOREVER, background = True)

silenced = False
def silencefunktion(event):
    global silenced
    silenced = True
    event.repeat()
#Rsilence.onAppear(silence, silencefunktion)
#Rsilence.observe(FOREVER, background = True)

castsunbird = False
def sunbirdfunktion(event):
#    global sunbirdtemp
#    sunbirdtemp = sunbirdready
    global castsunbird
    castsunbird = True    
    wait(3)
    if not Rsunbird2.exists(sunbirdready2):
        castsunbird = False
    event.repeat()

def sunbirdwebfunktion(event):
    global sunbirdtemp
    sunbirdtemp = sunbirdreadyweb
    global castsunbird
    if Rsunbird.exists(sunbirdreadyweb):    
        castsunbird = True
    else:
        castsunbird = False
    event.repeat()

def sunbirdentfunktion(event):
    global sunbirdtemp
    sunbirdtemp = sunbirdreadyent
    global castsunbird
    if Rsunbird.exists(sunbirdreadyent):    
        castsunbird = True
    else:
        castsunbird = False
    event.repeat()

def sunbirddeathfunktion(event):
    global sunbirdtemp
    sunbirdtemp = sunbirdreadydeath
    global castsunbird
    if Rsunbird.exists(sunbirdreadydeath):    
        castsunbird = True
    else:
        castsunbird = False
    event.repeat()

def sunbirdmarkfunktion(event):
    global sunbirdtemp
    sunbirdtemp = sunbirdreadymark
    global castsunbird
    if Rsunbird.exists(sunbirdreadymark):    
        castsunbird = True
    else:
        castsunbird = False
    event.repeat()

Rsunbird2.onAppear(sunbirdready2, sunbirdfunktion)
#Rsunbird.onAppear(sunbirdreadymark, sunbirdmarkfunktion)
#Rsunbird.onAppear(sunbirdreadydeath, sunbirddeathfunktion)
#Rsunbird.onAppear(sunbirdreadyweb, sunbirdwebfunktion)
#Rsunbird.onAppear(sunbirdreadyent, sunbirdentfunktion)
Rsunbird2.observe(FOREVER, background = True)

#def failsafeonefunktion(event):
#    wait(10)
#    if Rbattlestart.exists(tobattle):
#        Rbattlestart.click()
#    event.repeat()

#Rbattlestart.onAppear(tobattle, failsafeonefunktion)
#Rbattlestart.observe(FOREVER, background = True)

Rmiddle.click()
wait(0.3)
Rkingdom.click()
wait(0.3)
while(running):
    Rbattlestart.wait(tobattle, FOREVER)
    Rbattlestart.click()
    if errormeldung:
        Rerror.click(retry)
    Rfirstbomb.wait(bomb, FOREVER)
    wait(0.9)
    Rfirstbomb.click()
    if not Rcast.exists(cast):
        Rfirstbomb.click()
    Rcast.click()
    bombzahler = 2
    while not Rend.exists(endofbattle):
        if Rmyturn.exists(startIndicator): 
            if (castsunbird and not silenced):
                try:
                    Rsunbird.click(sunbirdready2)
                    if not Rcast.exists(cast):
                        try:
                            Rsunbird.click(sunbirdready2)
                        except FindFailed:
                            continue
                    Rcast.click()
                    castsunbird = False
                    continue
                except FindFailed:
                    castsunbird = False
                    continue
            if bombzahler < 4:
                try:
                    Rmydeck.click(bomb)
                    if not Rcast.exists(cast):
                        Rmydeck.click(bomb)
                    Rcast.click()
                    bombzahler += 1
                    continue
                except FindFailed:
                    bombzahler +=1
                    continue
            if Rsettings.exists(settings):
                Rsettings.click(settings)
            else:
                break
            if not Rretreat.exists(retreat):
                    Rsettings.click(settings)
            Rretreat.click(retreat)
            if not Ryes.exists(yes):
                    Rretreat.click(retreat)
            wait(0.2)
            Ryes.click(yes)
            if not Rmap.exists(mapsymbol):
                try:
                    Ryes.click(yes)
                except FindFailed:
                    retreattrigger = True
                    break
            retreattrigger = True
            break
    if retreattrigger: 
        Rmap.wait(mapsymbol, FOREVER)
        while True:
            wait(0.1)
            if not Rend.exists(endofbattle):
                break
        if Rtribut.exists(tribut):
            contbutton = False
            Rtribut.click(tribut)
            try:
                Rskip2.wait(skip, 10)
                Rskip2.click(skip)
                skipped = True
            except FindFailed:
                Rtribut.click(tribut)
                wait(10)
                contbutton = True
            if skipped:
                Rcontinu.click(continu)
            if contbutton:
                Rcontinu.click(continu)
        wait(0.2)
        Rmiddle.click()
        if not Rxzeichen.exists(xzeichen):
            Rmiddle.click()
        wait(0.3)
        Rkingdom.click()                
        wait(0.3)
        retreattrigger = False
        continue
    Rskip.wait(skip, FOREVER)
    Rskip.click()
    Rplayagain.wait(playagain, FOREVER)
    Rplayagain.click()
    Rbattlestart.wait(tobattle, 10)
    silenced = False
