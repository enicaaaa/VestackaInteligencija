import numpy as np
from numpy.lib.function_base import append

initial = {
    "heightOfTable": 0,
    "widthOfTable": 0,
    "numberOfWalls": 0,
    "initialPositionOfPlayerX" : [],
    "initialPositionOfPlayerO" : []
}

def setInitialTable():
    initial["widthOfTable"] = input("Please enter width of table: ")
    initial["heightOfTable"] = input("Please enter height of table: ")

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
    table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')
    print(table)


    #endregion VISINA iscrtavanje


    
setInitialTable()