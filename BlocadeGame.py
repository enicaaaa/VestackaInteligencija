###########################################################################################
initial = {
    "heightOfTable": 0,
    "widthOfTable": 0,
    "numberOfWalls": 0,
    "initialPositionOfPlayerX": [],
    "initialPositionOfPlayerO": [],
    "currentPositionOfPlayerX": [],
    "currentPositionOfPlayerO": [],
    "verticalCoordinatesOfWalls": [],
    "horisontalCoordinatesOfWalls": []
}


# - Funkcija za setovanje inicijalnih vrednosti igrice


def setInitialValues():
    initial["heightOfTable"] = input("Please enter height of table: ")
    initial["widthOfTable"] = input("Please enter width of table: ")
    initial["numberOfWalls"] = input("Please enter number of walls: ")
    initial["initialPositionOfPlayerX"].insert(
        0, [input("Please enter coordinate 1 of first pawn X: "), input("Please enter coordinate 2 of first pawn X: ")])
    initial["initialPositionOfPlayerX"].insert(
        1, [input("Please enter coordinate 1 of second pawn X: "), input("Please enter coordinate 2 of second pawn X:")])
    initial["initialPositionOfPlayerO"].insert(
        0, [input("Please enter coordinate 1 of first pawn Y: "), input("Please enter coordinate 2 of first pawn Y: ")])
    initial["initialPositionOfPlayerO"].insert(
        1, [input("Please enter coordinate 1 of second pawn Y: "), input("Please enter coordinate 2 of second pawn Y: ")])

###########################################################################################
# - Funkcija za matricu


def setInitialState():
    positions = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C']
    global table_string
    global new_table_string
    table_string = ""
    table_string += "      "  # 6 blanko znakova
    for i in range(1, int(initial["widthOfTable"])+1):
        if i < 16:
            table_string += positions[i]+"   "  # 1 + 3 blanko znaka
        else:
            # stampanje brojeva/slova u prvom redu
            table_string += positions[i]+"  "

    table_string += "    "  # 4 blanko znaka - 5x5 ovde je 30 ukupno znakova
    table_string += "\n"  # 1 znak - ukupno 31

    table_string += "      "  # 6 blanko znakova
    for i in range(1, (int(initial["widthOfTable"]))+1):
        table_string += "══  "  # stampanje gornje ivice # 4 simbola
    table_string += "    "  # 4+2 = 6 blanko znakova - 30 znakova takodje
    table_string += "\n"  # 1 znak
    table_string += "\n"  # 1 znak - ukupno 32

    for i in range(1, (int(initial["heightOfTable"])) + 1):
        if i < 16:
            # stampanje brojeva/slova sa leve strane(vertikalno) i levih ivica
            table_string += positions[i] + " " + " ║  "  # 6 znakova
        else:
            # stampanje brojeva/slova sa leve strane(vertikalno) i levih ivica (dvocifreni)
            table_string += positions[i]+" " + "║  "

        for j in range(1, int(initial["widthOfTable"]) + 1):
            # table_string +=  "══  "
            table_string += "--  "  # 2 blanko znaka, ukuno 4
        # stampanje brojeva/slova sa desne strane(vertikalno) i desnih ivica
        table_string += "║ " + positions[i]
        table_string += '\n'
        table_string += "    "
        if i < int(initial["heightOfTable"]):
            for k in range(1, int(initial["widthOfTable"]) + 1):
                table_string += "  ╍╍"
        if i < 16:
            table_string += " "
        # table_string += "\n"
        table_string += "\n"  # ukupno TAKODJE 32

    table_string += "      "
    for i in range(1, (int(initial["widthOfTable"]))+1):
        table_string += "══  "  # stampanje donjih ivica
    table_string += "  "
    table_string += "\n"
    table_string += "      "
    for i in range(1, int(initial["widthOfTable"])+1):
        if i < 16:
            # stampanje brojeva u poslednjem redu
            table_string += positions[i]+"   "
        else:
            # stampanje brojeva u poslednjem redu (dvocifreni)
            table_string += positions[i]+"  "
    table_string += "\n"

    koordinatePesak1X = initial["initialPositionOfPlayerX"][0]
    koordinatePesak2X = initial["initialPositionOfPlayerX"][1]
    koordinatePesak1O = initial["initialPositionOfPlayerO"][0]
    koordinatePesak2O = initial["initialPositionOfPlayerO"][1]

    if int(koordinatePesak1X[0]) > 1:
        inkrement = 3
        for i in range(int(koordinatePesak1X[0])-2):
            inkrement += 6

        pesak1X = int(koordinatePesak1X[0]) * 2 * (11 + 4 * int(initial["widthOfTable"])) - \
            inkrement + 4 * \
            int(koordinatePesak1X[1]
                )  # ovaj broj treba modifikovati za svaki novi red
    else:
        pesak1X = int(koordinatePesak1X[0]) * 2 * (11 + 4 * int(
            initial["widthOfTable"])) + 3 + 4 * int(koordinatePesak1X[1])
    table_string = table_string[:pesak1X] + "XX" + table_string[pesak1X + 2:]

    if int(koordinatePesak2X[0]) > 1:
        inkrement = 3
        for i in range(int(koordinatePesak2X[0])-2):
            inkrement += 6

        pesak2X = int(koordinatePesak2X[0]) * 2 * (11 + 4 * int(initial["widthOfTable"])) - \
            inkrement + 4 * \
            int(koordinatePesak2X[1]
                )  # ovaj broj treba modifikovati za svaki novi red
    else:
        pesak1X = int(koordinatePesak2X[0]) * 2 * (11 + 4 * int(
            initial["widthOfTable"])) + 3 + 4 * int(koordinatePesak2X[1])
    table_string = table_string[:pesak2X] + "XX" + table_string[pesak2X + 2:]

    if int(koordinatePesak1O[0]) > 1:
        inkrement = 3
        for i in range(int(koordinatePesak1O[0])-2):
            inkrement += 6

        pesak1O = int(koordinatePesak1O[0]) * 2 * (11 + 4 * int(initial["widthOfTable"])) - \
            inkrement + 4 * \
            int(koordinatePesak1O[1]
                )  # ovaj broj treba modifikovati za svaki novi red
    else:
        pesak1O = int(koordinatePesak1O[0]) * 2 * (11 + 4 * int(
            initial["widthOfTable"])) + 3 + 4 * int(koordinatePesak1O[1])
    table_string = table_string[:pesak1O] + "OO" + table_string[pesak1O + 2:]

    if int(koordinatePesak2O[0]) > 1:
        inkrement = 3
        for i in range(int(koordinatePesak2O[0])-2):
            inkrement += 6

        pesak2O = int(koordinatePesak2O[0]) * 2 * (11 + 4 * int(initial["widthOfTable"])) - \
            inkrement + 4 * \
            int(koordinatePesak2O[1]
                )  # ovaj broj treba modifikovati za svaki novi red
    else:
        pesak2O = int(koordinatePesak2O[0]) * 2 * (11 + 4 * int(
            initial["widthOfTable"])) + 3 + 4 * int(koordinatePesak2O[1])
    table_string = table_string[:pesak2O] + "OO" + table_string[pesak2O + 2:]


###########################################################################################


# -Funkcija za proveru kraja igre
def checkEndOfGame():
    if initial["currentPositionOfPlayerX"][0] or initial["currentPositionOfPlayerX"][1] == initial["initialPositionOfPlayerO"][0] or initial["initialPositionOfPlayerO"][1]:
        print("Game is over! The winner of the game is the player X")
    if initial["currentPositionOfPlayerO"][0] or initial["currentPositionOfPlayerO"][1] == initial["initialPositionOfPlayerX"][0] or initial["initialPositionOfPlayerX"][1]:
        print("Game is over! The winner of the game is the player O")


#############################################################################################
# - funkcija KO CE PRVI IGRATI


def whoPlaysFirst():
    firstPlayer = {
        "name": "",
        "sign": "X"
    }
    secondPlayer = {
        "name": "",
        "sign": "O"
    }

    def printPlayer(player):
        print(player["name"] + ", sa znakom - " + player["sign"])

    igrac = "igrac"
    kompjuter = "kompjuter"

    print("IZABERITE KO CE PRVI IGRATI")
    first = input("I - igrac, K - kompjuter. ")

    if(first == "I" or first == "i"):
        firstPlayer["name"] = "igrac"
        secondPlayer["name"] = "kompjuter"
    elif(first == "K" or first == "k"):
        firstPlayer["name"] = "kompjuter"
        secondPlayer["name"] = "igrac"

    print("Prvi igrac: ")
    printPlayer(firstPlayer)
    print("Drugi igrac: ")
    printPlayer(secondPlayer)
##########################################################################################


def haveTurn(player):
    print("haveTurnFunction")
#       - funkcija za menjanje trenutnog stanja


def setMove():
    turnX = {
        "player": "X",  # X ili O
        "pawn": "",  # 1 ili 2
        "x": -1,  # koordinata
        "y": -1,  # koordinata
        "wall": "",  # boja zida
        "wx": -1,  # koordinata gornjeg levog kvadratica od zida
        "wy": -1  # koordinata gornjeg levog kvadratica od zida
    }
    turnO = {
        "player": "O",  # X ili O
        "pawn": "",    # 1 ili 2
        "x": -1,       # koordinata
        "y": -1,       # koordinata
        "wall": "",    # boja zida
        "wx": -1,      # koordinata gornjeg levog kvadratica od zida
        "wy": -1       # koordinata gornjeg levog kvadratica od zida
    }

    if(haveTurn(igracX)):
        pawn = input("pawn:  ")
        x = input("pawnCoordinateX:  ")
        y = input("pawnCoordinateY:  ")
        wall = input("wall:  ")
        wx = input("wallX:  ")
        wy = input("wallY:  ")

        turnX["pawn"] = pawn
        turnX["x"] = x
        turnX["y"] = y
        turnX["wall"] = wall
        turnX["wx"] = wx
        turnX["wy"] = wy
    elif(haveTurn(igracO)):
        pawn = input("pawn:  ")
        x = input("pawnCoordinateX:  ")
        y = input("pawnCoordinateY:  ")
        wall = input("wall:  ")
        wx = input("wallX:  ")
        wy = input("wallY:  ")

        turnO["pawn"] = pawn
        turnO["x"] = x
        turnO["y"] = y
        turnO["wall"] = wall
        turnO["wx"] = wx
        turnO["wy"] = wy
########################################################
# -Funkcija STATE - broj preostalih zidova koje igrac ima


def State(potez, preostali):

    print(" Preostali zidovi: " + preostali)
    print(" Potez: " + potez)
    print(" Poslednji stavljen zid: " + initial["numberOfWalls"])

########################################################
# -Funkcija ValidMovePawn()
# val=initial.values() #uzimamo vrednosti svih kljuceva u dictionary
# n=val[1] #prva vrednost je height tabele pa je to broj n odnosno visina matrice
# m=val[2] #druga vrednost je width tabele pa je to broj m odnosno sirina matrice

# table=[n][m] #matrica


def ValidMovePawn(x, y):  # funkcija koja proverava validnost poteza pesaka

    if x < 0 or x > int(initial["heightOfTable"]):
        print("Inputed coordinates are not valid.")
        # pocetak tabele
    if y < 0 or y > int(initial["widthOfTable"]):
        print("Inputed coordinates are not valid.")

    if int(x) > 1:
        inkrement = 3
        for i in range(int(x)-2):
            inkrement += 6

            # ovaj broj treba modifikovati za svaki novi red
            provera = int(x) * 2 * (11 + 4 *
                                    int(initial["widthOfTable"])) - inkrement + 4 * int(y)

    else:
        provera = int(x) * 2 * (11 + 4 *
                                int(initial["widthOfTable"])) + 3 + 4 * int(y)
        if table_string[provera] == "X":
            print("There is already a pawn on the field you want to move your pawn! ")

    # if table[x][y] == "+":
        # break  # plus sam pretpostavio da cemo da stavimo da bude zid
    # if table[x][y] == "a" or "b":
        # break  # a i b su pesaci

########################################################

# -Funkcija ValidMoveWall


def ValidMoveWall(x, y):  # funkcija koja proverava validnost poteza zidova

    while True:
        if y == 0:
            break
        if y == n-1:
            break  # minus 3 zbog ona 2 karaktera za pokazivanje kraja tabele i rednog broja
        if x == 0:
            break
        if x == m-1:
            break  # minus 3 zbog ona 2 karaktera za pokazivanje kraja tabele i rednog broja

        if table[x][y] == "+":
            break  # plus sam pretpostavio da cemo da stavimo da bude zid
        if table[x][y] == "a" or "b":
            break  # a i b su pesaci

        if table[x+2][y+2] == "+":
            break  # posto zid vredi 2 polja moramo da proverimo i za sledece polje od unetog, a to je plus 2 zbog onog "zida" tj uspravne crte koja deli polja
        if table[x+2][y+2] == "a" or "b":
            break  # isto objasnjenje kao i za ovo iznad

########################################################

    global numberOfVerticalWalls


def inputVerticalWall():

    global table_string

    dodatZid = []
    dodatZid.insert(
        0, input("Please enter FIRST coordinate of VERTICAL wall:"))
    dodatZid.insert(
        1, input("Please enter SECOND coordinate of VERTICAL wall:"))
    initial["verticalCoordinatesOfWalls"].append(dodatZid)

    if int(dodatZid[0]) > 1:
        inkrement = 3
        inkrement1 = 7
        for i in range(int(dodatZid[0])-2):
            inkrement += 6
            inkrement1 += 6

        zidIndex = int(dodatZid[0]) * 2 * (11 + 4 * int(initial["widthOfTable"])) - \
            inkrement + 4 * \
            int(dodatZid[1]
                ) + 2  # ovaj broj treba modifikovati za svaki novi red

        zidIndex1 = (int(dodatZid[0])+1) * 2 * (11 + 4 * int(initial["widthOfTable"])) - \
            inkrement1 + 4 * \
            int(dodatZid[1]
                )

    else:
        zidIndex = int(dodatZid[0]) * 2 * (11 + 4 * int(initial["widthOfTable"])) + \
            3 + 4 * \
            int(dodatZid[1]
                ) + 2  # ovaj broj treba modifikovati za svaki novi red

        zidIndex1 = (int(dodatZid[0])+1) * 2 * (11 + 4 * int(initial["widthOfTable"]))-1  \
            + 4 * \
            int(dodatZid[1]
                )
    table_string = table_string[:zidIndex] + "||" + table_string[zidIndex + 2:]
    table_string = table_string[:zidIndex1] + \
        "||" + table_string[zidIndex1 + 2:]


# zid index i zid index1 pre else ne rade tj ne radi iscrtavanje horizontalnih zidova za x>1.
def inputHorisontalWall():
    # jedina stvar koja ne radi vezano za formulu!!!

    global table_string

    dodatZid = []
    dodatZid.insert(
        0, input("Please enter FIRST coordinate of HORISONTAL wall:"))
    dodatZid.insert(
        1, input("Please enter SECOND coordinate of HORISONTAL wall:"))
    initial["horisontalCoordinatesOfWalls"].append(dodatZid)

    if int(dodatZid[0]) > 1:
        inkrement = 3
        for i in range(int(dodatZid[0])-2):
            inkrement += 6

        zidIndex = int(dodatZid[0]) * (2+int(dodatZid[0])) * (11 + 4 * (int(initial["widthOfTable"]))) + \
            4 * \
            int(dodatZid[1]
                ) + 2  # ovaj broj treba modifikovati za svaki novi red

        zidIndex1 = int(dodatZid[0]) * 3 * (11 + 4 * (int(initial["widthOfTable"]))) + \
            4 * \
            int(dodatZid[1]
                ) + 6
    else:
        zidIndex = int(dodatZid[0]) * 3 * (11 + 4 * (int(initial["widthOfTable"]))) + \
            4 * \
            int(dodatZid[1]
                ) + 2  # ovaj broj treba modifikovati za svaki novi red

        zidIndex1 = int(dodatZid[0]) * 3 * (11 + 4 * (int(initial["widthOfTable"]))) + \
            4 * \
            int(dodatZid[1]
                ) + 6
    table_string = table_string[:zidIndex] + "==" + table_string[zidIndex + 2:]
    table_string = table_string[:zidIndex1] + \
        "==" + table_string[zidIndex1 + 2:]


setInitialValues()
setInitialState()
inputHorisontalWall()
inputVerticalWall()
ValidMovePawn(2,1)
print(table_string)


# print(table_string)
