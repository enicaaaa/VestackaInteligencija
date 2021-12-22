###########################################################################################
initial = {
    "heightOfTable": 0,
    "widthOfTable": 0,
    "numberOfWalls": 0,
    "initialPositionOfPlayerX" : [],
    "initialPositionOfPlayerO" : []
}

# - Funkcija za setovanje inicijalnih vrednosti igrice
def setInitialValues():
    initial["heightOfTable"] = input("Please enter height of table: ")
    initial["widthOfTable"] = input("Please enter width of table: ")
    initial["numberOfWalls"] = input("Please enter number of walls: ")
    initial["initialPositionOfPlayerX"].insert(
        0, [input("Please enter x: "), input("Please enter y: ")])
    initial["initialPositionOfPlayerX"].insert(
        1, [input("Please enter x: "), input("Please enter y: ")])
    initial["initialPositionOfPlayerO"].insert(
        0, [input("Please enter x: "), input("Please enter y: ")])
    initial["initialPositionOfPlayerO"].insert(
        1, [input("Please enter x: "), input("Please enter y: ")])

###########################################################################################
# - Funkcija za matricu
def setInitialState():
    sumH = int(initial["heightOfTable"]) * 2 + 3
    sumW = int(initial["widthOfTable"]) * 2 + 3
    positions = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','10','11','12','13','14','15','16','17','18','19','1A','1B','1C']
###########################################################################################


# -Funkcija za proveru kraja igre
def checkEndOfGame():
    for player in initial["initialPositionOfPlayerO"]:
        if player[2] == 'X':
            print("Game is over! The winner of the game is the player X")
    for player in initial["initialPositionOfPlayerX"]:
        if player[2] == 'O':
            print("Game is over! The winner of the game is the player O")
#############################################################################################
#       - funkcija KO CE PRVI IGRATI  
def whoPlaysFirst():
    firstPlayer = {
        "name" : "",
        "sign" : "X"
    }
    secondPlayer = {
        "name" : "",
        "sign" : "O"
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
        "player" : "X", # X ili O
        "pawn" : "", # 1 ili 2
        "x" : -1, # koordinata
        "y" : -1, # koordinata
        "wall" : "", # boja zida
        "wx" : -1, # koordinata gornjeg levog kvadratica od zida
        "wy" : -1 # koordinata gornjeg levog kvadratica od zida
    }
    turnO = {
        "player" : "O",  # X ili O
        "pawn" : "",    # 1 ili 2
        "x" : -1,       # koordinata
        "y" : -1,       # koordinata
        "wall" : "",    # boja zida
        "wx" : -1,      # koordinata gornjeg levog kvadratica od zida
        "wy" : -1       # koordinata gornjeg levog kvadratica od zida
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
def State(zid, potez,preostali):
   
    print(" Preostali zidovi: " +preostali)
    print(" Potez: " +potez)
    print(" Poslednji stavljen zid: " +zid)

State("Uspravni zid","[X 2]","5") #random vrednosti radi provere za ovu funkciju

########################################################
# -Funkcija ValidMovePawn()
val=initial.values() #uzimamo vrednosti svih kljuceva u dictionary
n=val[1] #prva vrednost je height tabele pa je to broj n odnosno visina matrice
m=val[2] #druga vrednost je width tabele pa je to broj m odnosno sirina matrice

table=[n][m] #matrica

def ValidMovePawwn(x,y): #funkcija koja proverava validnost poteza pesaka
   
    while True:
        if y==0: break #pocetak tabele
        if y==n-3: break #minus 3 zbog ona 2 karaktera za pokazivanje kraja tabele i rednog broja
        if x==0:break #pocetak tabele
        if x== m-3:break #minus 3 zbog ona 2 karaktera za pokazivanje kraja tabele i rednog broja

        if table[x][y]=="+": break #plus sam pretpostavio da cemo da stavimo da bude zid
        if table[x][y]=="a" or "b":break # a i b su pesaci

########################################################

# -Funkcija ValidMoveWall

def ValidMoveWall(x,y): #funkcija koja proverava validnost poteza zidova

    while True:
        if y==0: break
        if y==n-1: break #minus 3 zbog ona 2 karaktera za pokazivanje kraja tabele i rednog broja
        if x==0:break
        if x== m-1:break #minus 3 zbog ona 2 karaktera za pokazivanje kraja tabele i rednog broja

        if table[x][y]=="+": break #plus sam pretpostavio da cemo da stavimo da bude zid
        if table[x][y]=="a" or "b":break # a i b su pesaci


        if table[x+2][y+2]=="+": break #posto zid vredi 2 polja moramo da proverimo i za sledece polje od unetog, a to je plus 2 zbog onog "zida" tj uspravne crte koja deli polja
        if table[x+2][y+2]=="a" or "b":break #isto objasnjenje kao i za ovo iznad

########################################################

