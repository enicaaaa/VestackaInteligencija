import numpy as np
from numpy.lib.function_base import append
from string import Template

initial = {
    "heightOfTable": 0,
    "widthOfTable": 0,
    "numberOfWallsX": 0,
    "numberOfWallsO": 0,
    "initialPositionOfPlayerX" : [],
    "initialPositionOfPlayerO" : [],
    "currentPositionOfPlayerX-pesak1": [],
    "currentPositionOfPlayerX-pesak2": [],
    "currentPositionOfPlayerO-pesak1": [],
    "currentPositionOfPlayerO-pesak2": [],
    "horisontalWalls": [],
    "verticalWalls": [],
    "currentPlayer": "X",
    "currentPawn":0,
}
def setInitialValues():

    initial["widthOfTable"] = input("Please enter width of table: ")
    initial["heightOfTable"] = input("Please enter height of table: ")
    initial["numberOfWallsX"] = input("Please enter number of walls : ")
    initial["numberOfWallsO"] = initial["numberOfWallsX"] 
    initial["initialPositionOfPlayerX"].insert(
        0, [input("Please enter coordinate 1 of first pawn X: "), input("Please enter coordinate 2 of first pawn X: ")])
    initial["initialPositionOfPlayerX"].insert(
        1, [input("Please enter coordinate 1 of second pawn X: "), input("Please enter coordinate 2 of second pawn X:")])
    initial["initialPositionOfPlayerO"].insert(
        0, [input("Please enter coordinate 1 of first pawn Y: "), input("Please enter coordinate 2 of first pawn Y: ")])
    initial["initialPositionOfPlayerO"].insert(
        1, [input("Please enter coordinate 1 of second pawn Y: "), input("Please enter coordinate 2 of second pawn Y: ")])

    initial['currentPositionOfPlayerX-pesak1'] = initial['initialPositionOfPlayerX'][0]
    initial['currentPositionOfPlayerX-pesak2'] = initial['initialPositionOfPlayerX'][1]
    initial['currentPositionOfPlayerO-pesak1'] = initial['initialPositionOfPlayerO'][0]
    initial['currentPositionOfPlayerO-pesak2'] = initial['initialPositionOfPlayerO'][1]
    

def setInitialState():  

    #region SIRINA iscrtavanje 

    positions = ['     ','1   ','2   ','3   ','4   ','5   ','6   ','7   ','8   ','9   ','A   ','B   ','C   ','D   ','E   ','F   ',
                '10  ','11  ','12  ','13  ','14  ','15  ','16  ', '17  ','18  ','19  ' ,'1A  ','1B  ','1C  ']
    positions = positions[:int(initial["widthOfTable"]) + 1]

    walls = ['    ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ',]

    walls = walls[:int(initial["widthOfTable"]) + 1]

    #endregion SIRINA iscrtavanje 


    #region VISINA iscrtavanje
    positionColumn = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',
                      '10','12','13','14','15','16', '17','18','19','1A','1B','1C',]
    numPyArray = [positions, walls]
    positionsEnd = ['    ','1   ','2   ','3   ','4   ','5   ','6   ','7   ','8   ','9   ','A   ','B   ','C   ','D   ','E   ','F   ',
                '10  ','11  ','12  ','13  ','14  ','15  ','16  ', '17  ','18  ','19  ' ,'1A  ','1B  ','1C  ']
    positionsEnd = positionsEnd[:int(initial["widthOfTable"]) + 1]
    for i in range(1,int(initial['heightOfTable'])+1):
        end = i
        
        if i < 16:
            row = ['',positionColumn[i-1],'║','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','║', '1']
            row = row[:int((int((int(initial["widthOfTable"]))+1)*2))]
            row.append(row[2])
            row.append(row[1])
        else:
            row = [positionColumn[i-1],'║','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','║', '1']
            row = row[:int((int((int(initial["widthOfTable"]))+1)*2))]
            row.pop()
            row.append(row[1])
            row.append(row[0])
        tableWalls = ['    ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ','──  ']
        tableWalls = tableWalls[:int(initial["widthOfTable"]) + 1]
        numPyArray.append(row)
        
        if end != int(initial['heightOfTable']):
         numPyArray.append(tableWalls)
        else:
         numPyArray.append(walls)
         numPyArray.append(positionsEnd)
    # a = np.array([positions, walls, row,tableWalls])
    global a
    a = np.array(numPyArray)


    #endregion VISINA iscrtavanje

    #region PESACI 
    koordinatePesak1X = initial['currentPositionOfPlayerX-pesak1']
    koordinatePesak2X = initial['currentPositionOfPlayerX-pesak2']
    koordinatePesak1O = initial['currentPositionOfPlayerO-pesak1']
    koordinatePesak2O = initial['currentPositionOfPlayerO-pesak2']


    a[int(koordinatePesak1X[0])*2][int(koordinatePesak1X[1])*2+1] = '🟡'

    a[int(koordinatePesak2X[0])*2][int(koordinatePesak2X[1])*2+1] = '🟡'

    a[int(koordinatePesak1O[0])*2][int(koordinatePesak1O[1])*2+1] = '🟠'

    a[int(koordinatePesak2O[0])*2][int(koordinatePesak2O[1])*2+1] = '🟠'

    #endregion PESACI 

    #region ZIDOVI
    
    


    global table 
    table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')
    print(table)
    

def checkEndOfGame():
    if initial["currentPositionOfPlayerX-pesak1"] or initial["currentPositionOfPlayerX-pesak2"] == initial["initialPositionOfPlayerO-pesak1"] or initial["initialPositionOfPlayerO-pesak2"]:
        print("Game is over! The winner of the game is the player X")
    if initial["currentPositionOfPlayerO-pesak1"] or initial["currentPositionOfPlayerO-pesak2"] == initial["initialPositionOfPlayerX-pesak1"] or initial["initialPositionOfPlayerX-pesak2"]:
        print("Game is over! The winner of the game is the player O")
    

def State(vrstaZida):

    if initial["currentPlayer"] == "X": 
        if vrstaZida == 'U':
            duzinaliste = len(initial["verticalWalls"]) - 1
            lista = initial["verticalWalls"][duzinaliste]
            x = lista[0]
            y = lista[1]
            print('Uspravni zid: ║ ')
            if initial["currentPawn"] == 1:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerX-pesak1"]}  [ Z  {x} {y} ] ')
            elif initial["currentPawn"] == 2:
                print(initial['currentPositionOfPlayerX-pesak2'])
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerX-pesak2"]}  [ Z  {x} {y} ] ')
        else: 
            print('Polozeni zid:  ══')
            duzinaliste = len(initial["horisontalWalls"]) - 1
            lista = initial["horisontalWalls"][duzinaliste]
            x = lista[0]
            y = lista[1]
            if initial["currentPawn"] == 1:
                 print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerX-pesak1"]}   [ P  {x} {y} ] ')
            elif initial['currentPawn'] == 2:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerX-pesak2"]}     [ P  {x} {y} ] ')
    
    
    if initial["currentPlayer"] == "O": 
        if vrstaZida == 'U':
            duzinaliste = len(initial["verticalWalls"]) - 1
            lista = initial["verticalWalls"][duzinaliste]
            x = lista[0]
            y = lista[1]
            print('Uspravni zid: ║ ')
            if initial["currentPawn"] == 1:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerO-pesak1"]}  [ Z  {x} {y} ] ]')
            elif initial['currentPawn'] == 2:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerO-pesak2"]}  [ Z  {x} {y} ] ]')
        else: 
            print('Polozeni zid:  ══')
            duzinaliste = len(initial["horisontalWalls"]) - 1
            lista = initial["horisontalWalls"][duzinaliste]
            x = lista[0]
            y = lista[1]
            if initial["currentPawn"] == 1:
                 print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerO-pesak1"]}   [ P  {x} {y} ] ]')
            elif initial['currentPawn'] == 2:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]   {initial["currentPositionOfPlayerO-pesak2"]}   [ P  {x} {y} ] ]') 

def ValidMovePawn(x,y):
    if x < 0 or x > int(initial["heightOfTable"]):
        print("Inputed coordinates are not valid.")
        
    if y < 0 or y > int(initial["widthOfTable"]):
        print("Inputed coordinates are not valid.")

def potez(): 
    pesak = input("Unesi broj pesaka kojim zelis da odigras potez, 1 ili 2: ")
    initial['currentPawn'] = int(pesak)
    pesakX = input("Unesi X koordinatu pesaka:")
    pesakY = input("Unesi Y koordinatu pesaka:")

    #pozivanje funkcije koja validira unete koordinate i ceo POTEZ!!!
    #ako je ok onda zapamtimo koordinate u current

    if initial["currentPlayer"] ==  "X":
        if initial['currentPawn'] == 1: 
            a[int(initial['currentPositionOfPlayerX-pesak1'][0])*2][int(initial['currentPositionOfPlayerX-pesak1'][1])*2+1]='••'

            initial["currentPositionOfPlayerX-pesak1"][0] = pesakX
            initial["currentPositionOfPlayerX-pesak1"][1] = pesakY
            
            a[int(pesakX)*2][int(pesakY)*2+1] = '🟡'
            table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')

        elif initial["currentPawn"] == 2:
            a[int(initial['currentPositionOfPlayerX-pesak2'][0])*2][int(initial['currentPositionOfPlayerX-pesak2'][1])*2+1]='••'

            initial["currentPositionOfPlayerX-pesak2"] = pesakX
            initial["currentPositionOfPlayerX-pesak2"] = pesakY

            a[int(pesakX)*2][int(pesakY)*2+1] = '🟡'
            table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')
    else:
        if initial['currentPawn'] == 1: 
            a[int(initial['currentPositionOfPlayerO-pesak1'][0])*2][int(initial['currentPositionOfPlayerO-pesak1'][1])*2+1]='••'

            initial['currentPositionOfPlayerO-pesak1'] = pesakX
            initial['currentPositionOfPlayerO-pesak1'] = pesakY

            a[int(pesakX)*2][int(pesakY)*2+1] = '🟠'
            table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')

        elif initial["currentPawn"] == 2:
            a[int(initial['currentPositionOfPlayerO-pesak2'][0])*2][int(initial['currentPositionOfPlayerO-pesak2'][1])*2+1]='••'

            initial['currentPositionOfPlayerO-pesak2'] = pesakX
            initial['currentPositionOfPlayerO-pesak2'] = pesakY

            a[int(pesakX)*2][int(pesakY)*2+1] = '🟠'
            table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')

    vrsta = input("Izaberi zid, U za uspravni ili P za polozeni zid: ")
    zid = [input("Unesi koordinatu X zida:"),input("Unesi koordinatu Y zida:")]
    
    #poziv fje koja validira stavljanje zida na te koordinate 
    #ako moze, pamtimo zid u sledecem koraku 

    #region setovanje zidova i stavljanje na tablu 
    if vrsta == "U":
        initial['verticalWalls'].append(zid)
        a[(int(zid[0])*2)][int(zid[1])+3] = '║'
        a[(int(zid[0])*2)+2][int(zid[1])+3] = '║'
        table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')


    else:
        initial['horisontalWalls'].append(zid)
        a[(int(zid[0])*2)+1][int(zid[1])] = '══  '
        a[(int(zid[0])*2)+1][int(zid[1])+1] = '══  '
        table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')

    State(vrsta)
    #end region setovanje zidova i stavljanje na tablu 
    

    print(table)

        


    
    

setInitialValues()    
setInitialState()
#checkEndOfGame()
potez()

