import numpy as np

initial = {
    "heightOfTable": 0,
    "widthOfTable": 0,
    "numberOfWalls": 0,
    "initialPositionOfPlayerX" : [],
    "initialPositionOfPlayerO" : []
}

def setInitialTable():
    # initial["widthOfTable"] = input("Please enter width of table: ")
    # initial["heightOfTable"] = input("Please enter height of table: ")

    positions = ['    ','1   ','2   ','3   ','4   ','5   ','6   ','7   ','8   ','9   ','A   ','B   ','C   ','D   ','E   ','F   ',
                '10  ','12  ','13  ','14  ','15  ','16  ', '17   ','18   ','19   ' ,'1A   ','1B   ','1C   ']
    # positions = positions[:int(initial["widthOfTable"]) + 1]

    walls = ['   ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ','==  ']

    # walls = walls[:int(initial["widthOfTable"]) + 1]

    row = ['1','║','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','|','••','║', '1']

    tableWalls = ['   ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ','⁃⁃  ']

    # for i in range(0,int(initial["widthOfTable"])):
    #     print('x') 


    a = np.array([positions, walls, row, tableWalls])
    table = str(a).replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '').replace('list', '').replace("'",'')
    
    print(table)
    # print("dddddddddddddddddddddddddddddddddddddd  dddddddddddddddddddddddddddddddddddddd dddddddddddddddddddddddddddddddddddddd")

setInitialTable()