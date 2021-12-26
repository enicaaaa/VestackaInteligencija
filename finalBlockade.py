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
    "currentPositionOfPlayerX": [],
    "currentPositionOfPlayerO": [],
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
    a = np.array(numPyArray)


    #endregion VISINA iscrtavanje

    #region PESACI 
    koordinatePesak1X = initial["initialPositionOfPlayerX"][0]
    koordinatePesak2X = initial["initialPositionOfPlayerX"][1]
    koordinatePesak1O = initial["initialPositionOfPlayerO"][0]
    koordinatePesak2O = initial["initialPositionOfPlayerO"][1]
    
    a[int(koordinatePesak1X[0])*2][int(koordinatePesak1X[1])*2+1] = '🔴'

    a[int(koordinatePesak2X[0])*2][int(koordinatePesak2X[1])*2+1] = '🔴'

    a[int(koordinatePesak1O[0])*2][int(koordinatePesak1O[1])*2+1] = '🟠'

    a[int(koordinatePesak2O[0])*2][int(koordinatePesak2O[1])*2+1] = '🟠'

    #endregion PESACI 

    #region ZIDOVI
    
    


    global table 
    table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')
   

def checkEndOfGame():
    if initial["currentPositionOfPlayerX"][0] or initial["currentPositionOfPlayerX"][1] == initial["initialPositionOfPlayerO"][0] or initial["initialPositionOfPlayerO"][1]:
        print("Game is over! The winner of the game is the player X")
    if initial["currentPositionOfPlayerO"][0] or initial["currentPositionOfPlayerO"][1] == initial["initialPositionOfPlayerX"][0] or initial["initialPositionOfPlayerX"][1]:
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
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerX"][0]}  {initial["currentPositionOfPlayerX"][1]} [ Z  {x} {y} ] ]')
            elif initial['currentPawn'] == 2:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerX"][0]}  {initial["currentPositionOfPlayerX"][1]} [ Z  {x} {y} ] ]')
        else: 
            print('Polozeni zid:  ══')
            duzinaliste = len(initial["horisontalWalls"]) - 1
            lista = initial["horisontalWalls"][duzinaliste]
            x = lista[0]
            y = lista[1]
            if initial["currentPawn"] == 1:
                 print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerX"][0]}  {initial["currentPositionOfPlayerX"][1]} [ P  {x} {y} ] ]')
            elif initial['currentPawn'] == 2:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerX"][0]}  {initial["currentPositionOfPlayerX"][1]} [ P  {x} {y} ] ]')
    
    
    if initial["currentPlayer"] == "O": 
        if vrstaZida == 'U':
            duzinaliste = len(initial["verticalWalls"]) - 1
            lista = initial["verticalWalls"][duzinaliste]
            x = lista[0]
            y = lista[1]
            print('Uspravni zid: ║ ')
            if initial["currentPawn"] == 1:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerO"][0]}  {initial["currentPositionOfPlayerO"][1]} [ Z  {x} {y} ] ]')
            elif initial['currentPawn'] == 2:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerO"][0]}  {initial["currentPositionOfPlayerO"][1]} [ Z  {x} {y} ] ]')
        else: 
            print('Polozeni zid:  ══')
            duzinaliste = len(initial["horisontalWalls"]) - 1
            lista = initial["horisontalWalls"][duzinaliste]
            x = lista[0]
            y = lista[1]
            if initial["currentPawn"] == 1:
                 print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerO"][0]}  {initial["currentPositionOfPlayerO"][1]} [ P  {x} {y} ] ]')
            elif initial['currentPawn'] == 2:
                print(f'Potez: [ {initial["currentPlayer"]} {initial["currentPawn"]} ]  [ {initial["currentPositionOfPlayerO"][0]}  {initial["currentPositionOfPlayerO"][1]} [ P  {x} {y} ] ]') 

def ValidMovePawn(x,y):
    if x < 0 or x > int(initial["heightOfTable"]):
        print("Inputed coordinates are not valid.")
        
    if y < 0 or y > int(initial["widthOfTable"]):
        print("Inputed coordinates are not valid.")



setInitialValues()    
setInitialState()
#checkEndOfGame()
print(table)