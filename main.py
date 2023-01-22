from datetime import datetime
import pymysql
conn = pymysql.connect(host='20.16.222.208',user = 'ema', password='Admin@8100', db='EMA')

cur = conn.cursor()

cadena1 = (
    "********************************************************************************************************************************************\n\n")
cadena1 = cadena1 + ("   _____                         ___              __   __  __      ______\n")
cadena1 = cadena1 + ("  / ___/___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/\n")
cadena1 = cadena1 + ("  \__ \/ _ \ | / / _ \/ __ \   / /| | / __ \/ __  /  / /_/ / __ `/ / /_ \n")
cadena1 = cadena1 + (" ___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/\n")
cadena1 = cadena1 + ("/____/\___/|___/\___/_/ /_/  /_/  |_/_/ /_/\__,_/  /_/ /_/\__,_/_/_/ \n")
cadena1 = cadena1 + ("  ______     _                   _______                      _             _   _ _ _ \n")
cadena1 = cadena1 + (" |  ____|   | |                 |__   __|                    | |           (_) (_) | |\n")
cadena1 = cadena1 + (" | |__   ___| |_ _____   _____     | | ___ _ __ _ __ __ _  __| | __ _ ___   _   _| | | __ _\n")
cadena1 = cadena1 + (" |  __| / __| __/ _ \ \ / / _ \    | |/ _ \ '__| '__/ _` |/ _` |/ _` / __| | | | | | |/ _` |\n")
cadena1 = cadena1 + (" | |____\__ \ ||  __/\ V /  __/    | |  __/ |  | | | (_| | (_| | (_| \__ \ | | | | | | (_| |\n")
cadena1 = cadena1 + (" |______|___/\__\___| \_/ \___|    |_|\___|_|  |_|  \__,_|\__,_|\__,_|___/ |_| |_|_|_|\__,_|\n\n")
cadena1 = cadena1 + (
    "********************************************************************************************************************************************")

# 2

cadena2 = (
    "********************************************************************************************************************************************\n\n")
cadena2 = cadena2 + ("   .d8888b.           888    888    d8b\n")
cadena2 = cadena2 + ("  d88P  Y88b          888    888    Y8P\n")
cadena2 = cadena2 + ("  Y88b.               888    888\n")
cadena2 = cadena2 + ("  Y888b.    .d88b.  888888 888888   888 88888b.   .d88b.  .d8888b\n")
cadena2 = cadena2 + ("   Y88b.    d8P  Y8b  888    888    888 888 ""88b  d88P""88b 88K\n")
cadena2 = cadena2 + ("     888    88888888  888    888    888 888  888 888  888 Y8888b.\n")
cadena2 = cadena2 + (" Y88b  d88P Y8b.      Y88b.  Y88b.  888 888  888 Y88b 888      X88\n")
cadena2 = cadena2 + ("   Y8888P    Y8888      Y888  Y888  888 888  888   Y88888 88888P\n")
cadena2 = cadena2 + ("                                                      888         \n")
cadena2 = cadena2 + ("                                                 Y8b d88P        \n")
cadena2 = cadena2 + ("                                                   Y88P         \n\n")
cadena2 = cadena2 + (
    "********************************************************************************************************************************************")

# 3
cadena3 = (
    "********************************************************************************************************************************************\n\n")
cadena3 = cadena3 + ("     _____        __     __  ___                ____                            __      \n")
cadena3 = cadena3 + ("   / ___/ ___   / /_   /  |/  /____ _ _  __   / __ \ ____   __  __ ____   ____/ /_____ \n")
cadena3 = cadena3 + ("   \__ \ / _ \ / __/  / /|_/ // __ `/| |/_/  / /_/ // __ \ / / / // __ \ / __  // ___/ \n")
cadena3 = cadena3 + ("  ___/ //  __// /_   / /  / // /_/ /_>  <   / _, _// /_(/ // /_/ // / / // /_/ /(__  ) \n")
cadena3 = cadena3 + (" /____/ \___/ \__/  /_/  /_/ \__,_//_/|_|  /_/ |_| \____/ \__,_//_/ /_/ \__,_//____/\n\n")
cadena3 = cadena3 + (
    "********************************************************************************************************************************************")

# 4

name_digito = False

# 5
cadena5 = (
    "********************************************************************************************************************************************\n\n")
cadena5 = cadena5 + ("    ____                             __        \n")
cadena5 = cadena5 + ("   / __ \ ___   ____   ____   _____ / /_ _____\n")
cadena5 = cadena5 + ("  / /_/ // _ \ / __ \ / __ \ / ___// __// ___/ \n")
cadena5 = cadena5 + (" / _, _//  __// /_/ // /_/ // /   / /_ (__  )\n")
cadena5 = cadena5 + ("/_/ |_| \___// .___/ \____//_/    \__//____/ \n")
cadena5 = cadena5 + ("            /_/                            \n\n")
cadena5 = cadena5 + (
    "********************************************************************************************************************************************")

# 6
cadena6 = (
    "********************************************************************************************************************************************\n\n")
cadena6 = cadena6 + ("    ____                 __    _                    \n")
cadena6 = cadena6 + ("   / __ \ ____ _ ____   / /__ (_)____   ____ _\n")
cadena6 = cadena6 + ("  / /_/ // __ `// __ \ / //_// // __ \ / __ `/\n")
cadena6 = cadena6 + (" / _, _// /_/ // / / // ,<  / // / / // /_/ /\n")
cadena6 = cadena6 + ("/_/ |_| \__,_//_/ /_//_/|_|/_//_/ /_/ \__, /\n")
cadena6 = cadena6 + ("                                     /____/ \n\n")
cadena6 = cadena6 + (
    "********************************************************************************************************************************************")

# 7
cadena7 = (
    "********************************************************************************************************************************************\n\n")
cadena7 = cadena7 + ("     ____               __      ____   ____   ______                  __       \n")
cadena7 = cadena7 + ("    / __ \ ___   _____ / /__   / __ \ / __/  / ____/____ _ _____ ____/ /_____ \n")
cadena7 = cadena7 + ("   / / / // _ \ / ___// //_/  / / / // /_   / /    / __ `// ___// __  // ___/ \n")
cadena7 = cadena7 + ("  / /_/ //  __// /__ / ,<    / /_/ // __/  / /___ / /_/ // /   / /_/ /(__  ) \n")
cadena7 = cadena7 + (" /_____/ \___/ \___//_/|_|   \____//_/     \____/ \__,_//_/    \__,_//____/ \n\n")
cadena7 = cadena7 + (
    "********************************************************************************************************************************************")

# 8

cadena8 = (
    "********************************************************************************************************************************************\n\n")
cadena8 = cadena8 + ("     ____   ____   ____   ____     ____   __\n")
cadena8 = cadena8 + ("    / __ ) / __ ) / __ \ / __ \   / __ \ / /____ _ __  __ ___   _____ _____\n")
cadena8 = cadena8 + ("   / __  |/ __  |/ / / // / / /  / /_/ // // __ `// / / // _ \ / ___// ___/\n")
cadena8 = cadena8 + ("  / /_/ // /_/ // /_/ // /_/ /  / ____// // /_/ // /_/ //  __// /   (__  )\n ")
cadena8 = cadena8 + ("/_____//_____//_____//_____/  /_/    /_/ \__,_/ \__, / \___//_/   /____/\n")
cadena8 = cadena8 + ("                                                /____/                   \n\n")
cadena8 = cadena8 + (
    "********************************************************************************************************************************************")
jugadores = {
    "11115555A": {"name": "Mario", "human": False, "bank": False, "initialCard": 2, "priority": 1, "type": 30, "bet": 4,
                  "points": 0, "cards": [], "roundPoints": 0},
    "22225555A": {"name": "Pedro", "human": False, "bank": False, "initialCard": 13, "priority": 2, "type": 40,
                  "bet": 4, "points": 0, "cards": [], "roundPoints": 0},
    "25252525A": {"name": "Lucas", "human": False, "bank": False, "initialCard": 25, "priority": 3, "type": 50,
                  "bet": 4, "points": 0, "cards": [], "roundPoints": 0},
    "70919171M":{"name":"Kevin","human":True,"bank":False,"initialCard":15,"priority":1,"type":30,
                   "bet":4,"points":0,"cards":[],"roundPoints":0},
    "23605230P":{"name":"Leo","human":True,"bank":False,"intialCard":32,"priority":2,"type":40,"bet":4,"points":0,"cards":[],
                 "roundPoints":0},
    "53309533H":{"name":"Paolo","human":True,"bank":False,"initalCard":39,"priorty":3,"type":50,"bet":4,"points":0,"cards":[],
                 "roundPoints":0}
}



def menu_seleccion_jugadores(bots,humanos):
    # print(bots,humanos)

    cadena4 = (
        "********************************************************************************************************************************************\n\n")
    cadena4 = cadena4 + (
        "   _____        __     ______                           ____   __                                \n")
    cadena4 = cadena4 + (
        "  / ___/ ___   / /_   / ____/____ _ ____ ___   ___     / __ \ / /____ _ __  __ ___   _____ _____\n ")
    cadena4 = cadena4 + (
        "  \__ \ / _ \ / __/  / / __ / __ `// __ `__ \ / _ \   / /_/ // // __ `// / / // _ \ / ___// ___/\n")
    cadena4 = cadena4 + (
        " ___/ //  __// /_   / /_/ // /_/ // / / / / //  __/  / ____// // /_/ // /_/ //  __// /   (__  ) \n")
    cadena4 = cadena4 + (
        "/____/ \___/ \__/   \____/ \__,_//_/ /_/ /_/ \___/  /_/    /_/ \__,_/ \__, / \___//_/   /____/\n")
    cadena4 = cadena4 + (
        "                                                                     /____/                   \n\n")
    cadena4 = cadena4 + (
        "********************************************************************************************************************************************")
    print(cadena4)
    asteriscos = (
        "***************************************************************Select Players***************************************************************")
    print(asteriscos)
    intro = (
        "                             Boot Players                             ||                             Human Players                           ")
    print(intro)
    guiones = (
        "--------------------------------------------------------------------------------------------------------------------------------------------")
    print(guiones)
    a = (
        "ID                  Name                     Type                     || ID                  Name                     Type                  ")
    print(a)
    estrellitas = (
        "********************************************************************************************************************************************")
    print(estrellitas)
    if len(bots)>len(humanos):
        grande=len(bots)
    else:
        grande=len(humanos)
    concatenar_bot = 0
    concatenar_humano=0
    for x in range(0,grande):
        if concatenar_bot==len(bots):
            print(' '*72+' ',end='')
        for i in range(concatenar_bot,len(bots)):
            print(bots[i].ljust(20) + jugadores[bots[i]]['name'].ljust(25), end='')
            if jugadores[bots[i]]['type'] == 50:
                print('Bold'.ljust(25) +"||"+" ", end='')
            elif jugadores[bots[i]]['type'] == 40:
                print('Moderated'.ljust(25)+"||"+" ", end='')
            elif jugadores[bots[i]]['type'] == 30:
                print('Cautius'.ljust(25) +"||"+" ", end='')
            concatenar_bot+=1
            break
        if concatenar_humano==len(humanos):
            print('')
        for j in range(concatenar_humano, len(humanos)):

            print(humanos[j].ljust(20) + jugadores[humanos[j]]['name'].ljust(25), end='')
            if jugadores[humanos[j]]['type'] == 50:
                print('Bold'.ljust(10))
            elif jugadores[humanos[j]]['type'] == 40:
                print('Moderated'.ljust(10))
            elif jugadores[humanos[j]]['type'] == 30:
                print('Cautious'.ljust(10))
            concatenar_humano += 1
            break



    return " "
game = []
maxRounds1 = [5]
contextGame = {"game": game, "maxRounds": maxRounds1}
cartas_poker = {
    'R01': {"nombre": "As de rombos", "value": 1, "priority": 4, "realValue": 1},
    'R02': {"nombre": "Dos de rombos", "value": 2, "priority": 4, "realValue": 2},  # carta de Mario 2
    'R03': {"nombre": "Tres de rombos", "value": 3, "priority": 4, "realValue": 3},
    'R04': {"nombre": "Cuatro de rombos", "value": 4, "priority": 4, "realValue": 4},
    'R05': {"nombre": "Cinco de rombos", "value": 5, "priority": 4, "realValue": 5},
    'R06': {"nombre": "Seis de rombos", "value": 6, "priority": 4, "realValue": 6},
    'R07': {"nombre": "Siete de rombos", "value": 7, "priority": 4, "realValue": 7},
    'R10': {"nombre": "Sota de rombos", "value": 8, "priority": 4, "realValue": 0.5},
    'R11': {"nombre": "Caballo de rombos", "value": 9, "priority": 4, "realValue": 0.5},
    'R12': {"nombre": "Rey de rombos", "value": 10, "priority": 4, "realValue": 0.5},

    'Z01': {"nombre": "As de corazones", "value": 1, "priority": 3, "realValue": 1},
    'Z02': {"nombre": "Dos de corazones", "value": 2, "priority": 3, "realValue": 2},
    'Z03': {"nombre": "Tres de corazones", "value": 3, "priority": 3, "realValue": 3},  # carta de Pedro 3
    'Z04': {"nombre": "Cuatro de corazones", "value": 4, "priority": 3, "realValue": 4},
    'Z05': {"nombre": "Cinco de corazones", "value": 5, "priority": 3, "realValue": 5},
    'Z06': {"nombre": "Seis de corazones", "value": 6, "priority": 3, "realValue": 6},
    'Z07': {"nombre": "Siete de corazones", "value": 7, "priority": 3, "realValue": 7},
    'Z10': {"nombre": "Sota de corazones", "value": 8, "priority": 3, "realValue": 0.5},
    'Z11': {"nombre": "Caballo de corazones", "value": 9, "priority": 3, "realValue": 0.5},
    'Z12': {"nombre": "Rey de corazones", "value": 10, "priority": 3, "realValue": 0.5},

    'P01': {"nombre": "As de pikas", "value": 1, "priority": 2, "realValue": 1},
    'P02': {"nombre": "Dos de pikas", "value": 2, "priority": 2, "realValue": 2},
    'P03': {"nombre": "Tres de pikas", "value": 3, "priority": 2, "realValue": 3},
    'P04': {"nombre": "Cuatro de pikas", "value": 4, "priority": 2, "realValue": 4},
    'P05': {"nombre": "Cinco de pikas", "value": 5, "priority": 2, "realValue": 5},  # Carta de Lucas 5
    'P06': {"nombre": "Seis de pikas", "value": 6, "priority": 2, "realValue": 6},
    'P07': {"nombre": "Siete de pikas", "value": 7, "priority": 2, "realValue": 7},
    'P10': {"nombre": "Sota de pikas", "value": 8, "priority": 2, "realValue": 0.5},
    'P11': {"nombre": "Caballo de pikas", "value": 9, "priority": 2, "realValue": 0.5},
    'P12': {"nombre": "Rey de pikas", "value": 10, "priority": 2, "realValue": 0.5},

    'T01': {"nombre": "As de treboles", "value": 1, "priority": 1, "realValue": 1},
    'T02': {"nombre": "Dos de treboles", "value": 2, "priority": 1, "realValue": 2},
    'T03': {"nombre": "Tres de treboles", "value": 3, "priority": 1, "realValue": 3},
    'T04': {"nombre": "Cuatro de treboles", "value": 4, "priority": 1, "realValue": 4},
    'T05': {"nombre": "Cinco de treboles", "value": 5, "priority": 1, "realValue": 5},
    'T06': {"nombre": "Seis de treboles", "value": 6, "priority": 1, "realValue": 6},
    'T07': {"nombre": "Siete de treboles", "value": 7, "priority": 1, "realValue": 7},
    'T10': {"nombre": "Sota de treboles", "value": 8, "priority": 1, "realValue": 0.5},
    'T11': {"nombre": "Caballo de treboles", "value": 9, "priority": 1, "realValue": 0.5},
    'T12': {"nombre": "Rey de treboles", "value": 10, "priority": 1, "realValue": 0.5}
}

cartas = {
    'O01': {"nombre": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
    'O02': {"nombre": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},  # carta de Mario 2
    'O03': {"nombre": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
    'O04': {"nombre": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
    'O05': {"nombre": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
    'O06': {"nombre": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
    'O07': {"nombre": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
    'O10': {"nombre": "Sota de Oros", "value": 8, "priority": 4, "realValue": 0.5},
    'O11': {"nombre": "Caballo de Oros", "value": 9, "priority": 4, "realValue": 0.5},
    'O12': {"nombre": "Rey de Oros", "value": 10, "priority": 4, "realValue": 0.5},

    'C01': {"nombre": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
    'C02': {"nombre": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
    'C03': {"nombre": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},  # carta de Pedro 3
    'C04': {"nombre": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
    'C05': {"nombre": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
    'C06': {"nombre": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
    'C07': {"nombre": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
    'C10': {"nombre": "Sota de Copas", "value": 8, "priority": 3, "realValue": 0.5},
    'C11': {"nombre": "Caballo de Copas", "value": 9, "priority": 3, "realValue": 0.5},
    'C12': {"nombre": "Rey de Copas", "value": 10, "priority": 3, "realValue": 0.5},

    'E01': {"nombre": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
    'E02': {"nombre": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
    'E03': {"nombre": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
    'E04': {"nombre": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
    'E05': {"nombre": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},  # Carta de Lucas 5
    'E06': {"nombre": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
    'E07': {"nombre": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
    'E10': {"nombre": "Sota de Espadas", "value": 8, "priority": 2, "realValue": 0.5},
    'E11': {"nombre": "Caballo de Espadas", "value": 9, "priority": 2, "realValue": 0.5},
    'E12': {"nombre": "Rey de Espadas", "value": 10, "priority": 2, "realValue": 0.5},

    'B01': {"nombre": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
    'B02': {"nombre": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
    'B03': {"nombre": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
    'B04': {"nombre": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
    'B05': {"nombre": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
    'B06': {"nombre": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
    'B07': {"nombre": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
    'B10': {"nombre": "Sota de Bastos", "value": 8, "priority": 1, "realValue": 0.5},
    'B11': {"nombre": "Caballo de Bastos", "value": 9, "priority": 1, "realValue": 0.5},
    'B12': {"nombre": "Rey de Bastos", "value": 10, "priority": 1, "realValue": 0.5}
}



mazo = ['O01','O02','O03''O04','O05','O06','O07','O08','O09','O010','O011','O012','C01','C02','C02','C03','C04','C05','C06','C07','C08','C09','C010','C011','C0112',
        'E01','E02','E03','E04','E05','E06','E07','E08','E09','E010','E011','E012','B01','B02','B03','B04','B05','B06','B07','B08''B09','B010','B011','B012' ]




menu00 = "1)Add/Remove/Show Players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\n6)Exit"
menu01 = "1)New Human Player\n2)New Boot\n3)Show/Remove Players\n4)Go back"
menu02 = "1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds (Default 5 Rounds)\n4)Go back"
menu04 = "1)Players With More Earnings\n2)Players With More Games Played\n3)Players With More Minutes Played\n4)Go back"
menu05 = "1)  Initial card more repeated by each user,only users who have played a minimum of 3 games\n2)  Player who makes the highest bet per game,find the round with the highest bet.\n3)  Player who makes the lowest bet per game.\n4)  Percentage of rounds won per player in each game(%), as well as their average bet for the game.\n5)  List of games won by Bots.\n6)  Rounds won by the bank in each game.\n7)  Number of users have been the bank in each game.\n8)  Average bet per game.\n9)  Average bet of the first round of each game.\n10) Average bet of the last round of each game..\n11)Go Back"
menu03 = ("1)View Stats\n2)View Game Stats\n3)Set Bet\n4)Order Card\n5Automatic Play\n6)Stand")
menu_profile = 'Select your Profile:\n1)Cautious\n2)Moderated\n3)Bold'
m00 = True
m01 = False
m02 = False
m03 = False
jugador_humano = False
jugador_bot = False
tipo_juego = False
jugador_juego = False
salir = False
while not salir:
    while not salir:
        while m00:
            print(cadena1)
            print(menu00)
            opc = input("Opcion:")
            if not opc.isdigit():
                print("Solo se aceptran digitos")
            elif not int(opc) in range(0, 7):
                print("Opcion incorrecta")
            else:
                opc = int(opc)
                if opc == 1:
                    m00 = False
                    m01 = True
                    while m01:
                        lista_dni_jugadores = list(jugadores)
                        print(cadena8)
                        print()
                        print(menu01)
                        opc2 = input("Opcion:")
                        if not opc2.isdigit():
                            print("Solo se aceptran digitos")
                        elif not int(opc2) in range(0, 6):
                            print("Opcion incorrecta")
                        else:
                            opc2 = int(opc2)
                            if opc2 == 1:
                                name_human = input('Name: ')
                                for i in name_human:
                                    if i.isdigit():
                                        name_digito = True
                                if len(name_human) == 0:
                                    print('Incorrect name')
                                elif name_human[0] == ' ' and len(name_human) == 1:
                                    print('Incorrect name')
                                elif name_human[0] == ' ':
                                    print('Incorrect name, the name cannot start with space')
                                elif name_digito == True:
                                    print('Incorrect name')
                                else:
                                    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
                                    numeros = "1234567890"
                                    nif = input("Enter new NIF: ")
                                    if (len(nif) == 9):
                                        letraControl = nif[8].upper()
                                        dni = nif[:8]
                                        if not nif[0:8].isdigit():
                                            print('The first 8 characters of DNI are numbers')
                                        elif not nif[8].isalpha():
                                            print('Dni has to end with a letter')
                                        elif (len(dni) == len([n for n in dni if n in numeros])):
                                            if tabla[int(dni) % 23] == letraControl:
                                                nif = nif.upper()
                                                while nif in lista_dni_jugadores:
                                                    print('NIF {} already exists'.format(nif))
                                                    input('Enter to continue')
                                                    break
                                                else:

                                                    print(menu_profile)
                                                    jugadores[str(nif)] = {}
                                                    jugadores[nif]['name'] = name_human
                                                    jugadores[nif]['human'] = True
                                                    jugadores[nif]['bet'] = 4
                                                    jugadores[nif]['points'] = 0
                                                    jugadores[nif]['cards'] = []
                                                    jugadores[nif]['roundPoints'] = 0
                                                    import random

                                                    a = random.randrange(1, 40)
                                                    jugadores[nif]['initialCard'] = a

                                                    opc9 = input("Opcion:")
                                                    if not opc9.isdigit():
                                                        print("Solo se aceptran digitos")
                                                    elif not int(opc9) in range(0, 5):
                                                        print("Opcion incorrecta")
                                                    else:
                                                        opc9 = int(opc9)
                                                        if opc9 == 1:
                                                            jugadores[nif]['type'] = 30
                                                        if opc9 == 2:
                                                            jugadores[nif]['type'] = 40
                                                        if opc9 == 3:
                                                            jugadores[nif]['type'] = 50
                                                        if jugadores[nif]['type'] == 30:
                                                            jugadores[nif]['priority'] = 1
                                                        if jugadores[nif]['type'] == 40:
                                                            jugadores[nif]['priority'] = 2
                                                        if jugadores[nif]['type'] == 50:
                                                            jugadores[nif]['priority'] = 3

                                            else:
                                                print('Incorrect DNI letter')
                                    else:

                                        print('Incorrect lenght')
                                print()
                                bootskeys = []
                                bootsname = []
                                bootstype = []
                                humankeys = []
                                humanname = []
                                humantype = []
                                vueltashuman = 0
                                vueltasboot = 0

                                for i in list(jugadores):
                                    if jugadores[i]["human"] == False:
                                        bootskeys.append(i)
                                        bootsname.append(jugadores[i]["name"])
                                        bootstype.append(str(jugadores[i]["type"]))
                                        cadena = (bootskeys[vueltasboot].ljust(20) + bootsname[vueltasboot].ljust(25) +
                                                  bootstype[
                                                      vueltasboot] + " " * 23 + "||")
                                        vueltasboot += 1


                                    elif jugadores[i]["human"] == True:
                                        humankeys.append(i)
                                        humanname.append(jugadores[i]["name"])
                                        humantype.append(str(jugadores[i]["type"]))
                                        cadena += (" " * 1 + humankeys[vueltashuman].ljust(20) + humanname[
                                            vueltashuman].ljust(25) + humantype[
                                                       vueltashuman] + "\n")
                            if opc2 == 2:
                                name_bot = input('Name: ')
                                for i in name_bot:
                                    if i.isdigit():
                                        name_digito = True
                                if len(name_bot) == 0:
                                    print('Incorrect name')
                                elif name_bot[0] == ' ' and len(name_bot) == 1:
                                    print('Incorrect name')
                                elif name_bot[0] == ' ':
                                    print('Incorrect name, the name cannot start with space')
                                elif name_digito == True:
                                    print('Incorrect name')
                                print()


                                def newRandomDNI():
                                    import random
                                    Letras = (
                                    "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q",
                                    "V", "H", "L", "C", "K", "E", "T",
                                    )
                                    Numero_dni = random.randint(10000000, 99999999)
                                    Letra_dni = Letras[Numero_dni % 23]
                                    cadena = str(Numero_dni)
                                    cadena += Letra_dni
                                    return cadena


                                a = newRandomDNI()
                                print(a)
                                import random

                                jugadores[str(a)] = {}
                                jugadores[a]['name'] = name_bot
                                jugadores[a]['human'] = False
                                jugadores[a]['bet'] = 4
                                jugadores[a]['points'] = 0
                                jugadores[a]['cards'] = []
                                jugadores[a]['roundPoints'] = 0
                                c = random.randrange(1, 40)
                                jugadores[a]['initalCard'] = c
                                b = random.randrange(1, 3)
                                if b == 1:
                                    jugadores[a]['type'] = 30
                                    jugadores[a]['priority'] = 1
                                if b == 2:
                                    jugadores[a]['type'] = 40
                                    jugadores[a]['priority'] = 2
                                if b == 3:
                                    jugadores[a]['type'] = 50
                                    jugadores[a]['priority'] = 3
                            bootskeys = []
                            bootsname = []
                            bootstype = []
                            humankeys = []
                            humanname = []
                            humantype = []
                            vueltashuman = 0
                            vueltasboot = 0

                            for i in list(jugadores):
                                if jugadores[i]["human"] == False:
                                    bootskeys.append(i)
                                    bootsname.append(jugadores[i]["name"])
                                    bootstype.append(str(jugadores[i]["type"]))
                                    cadena = (bootskeys[vueltasboot].ljust(20) + bootsname[vueltasboot].ljust(25) +
                                              bootstype[
                                                  vueltasboot] + " " * 23 + "||")
                                    vueltasboot += 1


                                elif jugadores[i]["human"] == True:
                                    humankeys.append(i)
                                    humanname.append(jugadores[i]["name"])
                                    humantype.append(str(jugadores[i]["type"]))
                                    cadena += (" " * 1 + humankeys[vueltashuman].ljust(20) + humanname[
                                        vueltashuman].ljust(25) + humantype[
                                                   vueltashuman] + "\n")
                            if opc2 == 3:
                                print(menu_seleccion_jugadores(bootskeys,humankeys))
                                print(
                                    "********************************************************************************************************************************************")
                                print("                           id to remove player ,exit to exit")
                                a = input()
                                if a == "id" or a == "ID":
                                    id = input("ID:")
                                    if id in jugadores.keys():
                                        del jugadores[id]
                                        query = f"delete from PLAYER where id_player='{id}'"
                                        cur.execute(query)
                                        conn.commit()

                                        print("ID removed!!")
                                        input("Enter to continue")




                                elif a == "exit" or a == "EXIT":
                                    print()
                            if opc2 == 4:
                                m01 = False
                                m00 = True
                if opc == 2:
                    m00 = False
                    m02 = True
                    while m02:

                        print(cadena2)
                        print(menu02)
                        opc1 = input("Opcion:")
                        if not opc1.isdigit():
                            print("Solo se aceptran digitos")
                        elif not int(opc1) in range(0, 6):
                            print("Opcion incorrecta")
                        else:
                            opc1 = int(opc1)
                            if opc1 == 1:
                                bootskeys = []
                                bootsname = []
                                bootstype = []
                                humankeys = []
                                humanname = []
                                humantype = []
                                vueltashuman = 0
                                vueltasboot = 0

                                for i in list(jugadores):
                                    if jugadores[i]["human"] == False:
                                        bootskeys.append(i)
                                        bootsname.append(jugadores[i]["name"])
                                        bootstype.append(str(jugadores[i]["type"]))
                                        cadena = (bootskeys[vueltasboot].ljust(20) + bootsname[vueltasboot].ljust(25) +
                                                  bootstype[
                                                      vueltasboot] + " " * 23 + "||")
                                        vueltasboot += 1


                                    elif jugadores[i]["human"] == True:
                                        humankeys.append(i)
                                        humanname.append(jugadores[i]["name"])
                                        humantype.append(str(jugadores[i]["type"]))
                                        cadena += (" " * 1 + humankeys[vueltashuman].ljust(20) + humanname[
                                            vueltashuman].ljust(25) + humantype[
                                                       vueltashuman] + "\n")
                                print()
                                print(20 * '*', 'Actual Players In Game', '*' * 20)
                                if len(game)== 0:
                                    print(18 * ' ', 'There is no players in game', ' ' * 20)
                                elif len(game)>=1:
                                    for i in game:
                                        print(i)
                                print(18 * ' ', 'Enter to continue', ' ' * 20)
                                input()
                                print(menu_seleccion_jugadores(bootskeys,humankeys))
                                print(
                                    "********************************************************************************************************************************************")
                                print("                           id to add player ,exit to exit")
                                a = input()
                                if a == "id" or a == "ID":
                                    id = input("ID:")
                                    if id in jugadores.keys():
                                        game.append(id)

                                        contextGame["game"] = game
                                        print(contextGame)
                                    if not id in jugadores.keys():
                                        print("Incorrect ID")

                                elif a == "exit" or a == "EXIT":
                                    print()



                                jugador_humano = True
                            if opc1 == 2:
                                baraja = []
                                print("1)ESP-ESP\n2)POKER-POKER")
                                opc10 = input("Opcion:")
                                if not opc10.isdigit():
                                    print("Solo se aceptran digitos")
                                elif not int(opc10) in range(0, 3):
                                    print("Opcion incorrecta")
                                else:
                                    opc10 = int(opc10)
                                    if opc10 == 1:
                                        baraja = cartas
                                        print(baraja)
                                    if opc10 == 2:
                                        baraja = cartas_poker
                                        print(baraja)
                                tipo_juego = True
                            if opc1 == 3:
                                print(cadena3)
                                print("Maximo de Rondas (el maximo es 30)")
                                maxRounds = input("")
                                if not maxRounds.isdigit():
                                    print("Solo se aceptran digitos")
                                elif not int(maxRounds) in range(0, 30):
                                    print("Opcion incorrecta")
                                else:
                                    maxRounds = int(maxRounds)
                                    maxRounds1.clear()
                                    maxRounds1 = maxRounds

                            if opc1 == 4:
                                m02 = False
                                m00 = True

                if opc == 3:
                    if jugador_humano == True and tipo_juego == True and len(game)==2:
                        jugador_juego = True
                    if jugador_juego == False:
                        print('Set the players that compose the game first')
                        input('Enter to continue')
                    else:
                        while m03:
                            opc3 = input("Opcion:")
                            if not opc3.isdigit():
                                print("Solo se aceptran digitos")
                            elif not int(opc3) in range(0, 5):
                                print("Opcion incorrecta")
                            else:
                                opc3 = int(opc3)
                                print(menu03)
                                if opc3 == 1:
                                    for i in game:
                                        if i in jugadores.keys():
                                            if jugadores[i]["human"] == True:
                                                cadena = "name" + " " * 9 + jugadores[i]["name"] + "\n"
                                                cadena = cadena + "type" + " " * 9 + str(jugadores[i]["type"]) + "\n"
                                                cadena = cadena + "human" + " " * 8 + str(jugadores[i]["human"]) + "\n"
                                                cadena = cadena + "bank" + " " * 9 + str(jugadores[i]["bank"]) + "\n"
                                                cadena = cadena + "initialCard" + " " * 2 + str(
                                                    jugadores[i]["initialCard"]) + "\n"
                                                cadena = cadena + "priority" + " " * 5 + str(
                                                    jugadores[i]["priority"]) + "\n"
                                                cadena = cadena + "bet" + " " * 10 + str(jugadores[i]["bet"]) + "\n"
                                                cadena = cadena + "points" + " " * 7 + str(jugadores[i]["points"]) + "\n"
                                                cadena = cadena + "cards" + " " * 8 + str(jugadores[i]["cards"]) + "\n"
                                                cadena = cadena + "roundPoints" + " " * 2 + str(
                                                    jugadores[i]["roundPoints"]) + "\n"
                                                print(cadena)
                            if opc3 == 2:
                                print()
                            if opc3 == 3:
                                setbet = input("New Bet:")

                                if not setbet.isdigit():
                                    print("Solo se aceptran digitos")
                                elif not int(setbet) in range(0, 7):
                                    print("Opcion incorrecta")
                                else:
                                    setbet = int(setbet)
                                for i in game:
                                    if jugadores[i]["human"] == True:
                                        jugadores[i]["bet"] = setbet
                            if opc3 == 4:
                                import random



                                a = random.randrange(1, len(cartas))
                                b = cartas.keys()
                                c = []
                                opc21 = int(input(":"))
                                if opc21 == 1:
                                    baraja = cartas

                                elif opc21 == 2:
                                    baraja = cartas_poker
                                for i in baraja.keys():
                                    c.append(i)
                                d = c[a]

                                for i in game:
                                    if jugadores[i]["human"] == True:
                                        jugadores[i]["cards"] = d
                                        print(jugadores[i]["cards"])
                                        if jugadores[i]["human"] == True:
                                            variable = baraja[d]["nombre"]
                                            variable2 = baraja[d]["realValue"]
                                            jugadores[i]["points"] += variable2
                                            print("Te ha salido el", variable, "y ahora tienes", variable2, "puntos")
                                    elif jugadores[i]["human"] == False:
                                        k = random.randrange(1, len(cartas))
                                        j = cartas.keys()
                                        m = []
                                        for j in baraja.keys():
                                            m.append(j)
                                        u = m[k]
                                        baraja[j]["cards"] = u
                                        variable5 = baraja[u]["realValue"]
                                        jugadores[i]["points"] += variable5
                            if opc3 == 5:
                                print()
                            if opc3 == 6:
                                if not contextGame["Game"] == maxRounds1:
                                    print()

                if opc == 4:
                    m00 = False
                    m04 = True
                    while m04:
                        print(cadena6)
                        print(menu04)
                        opc4 = input("Opcion:")
                        if not opc4.isdigit():
                            print("Solo se aceptran digitos")
                        elif not int(opc4) in range(0, 5):
                            print("Opcion incorrecta")
                        else:
                            opc4 = int(opc4)
                            if opc4 == 1:
                                print("\n")
                                query = "select id_player,ending_points-starting_points,id_game from PLAYER_GAME order by ending_points-starting_points desc;"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID PARTIDA'.ljust(15) + 'PUNTOS FINALES'.ljust(20) + 'ID PARTIDA')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(15) + str(i[2]).rjust(16))
                                input("\nEnter to continue")
                            if opc4 == 2:
                                print("\n")
                                query = "select id_player as ID,count(*) as partidas from PLAYER_GAME group by id_player;"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID JUGADOR'.ljust(15) + 'PARTIDAS JUGADAS')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(14))
                                input("\nEnter to continue")
                            if opc4 == 3:
                                print("\n")
                                query = "select p.id_player,time(sum(g.end_hour-g.start_hour)) from GAME g inner join PLAYER_GAME p on g.id_game=p.id_game group by p.id_player order by time(sum(g.end_hour-g.start_hour)) desc;"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID JUGADOR'.ljust(15) + 'MINUTOS TOTALES')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(16))
                                input("\nEnter to continue")
                            if opc4 == 4:
                                m04 = False
                                m00 = True

                if opc == 5:
                    m00 = False
                    m05 = True
                    while m05:
                        print(cadena5)
                        print(menu05)
                        opc5 = input("Opcion:")
                        if not opc5.isdigit():
                            print("Solo se aceptran digitos")
                        elif not int(opc5) in range(0, 12):
                            print("Opcion incorrecta")
                        else:
                            opc5 = int(opc5)
                            if opc5 == 1:
                                print("---------------------------------------------------------In Contruction---------------------------------------------------------------------")
                                input("                                                        Enter to continue")
                            if opc5 == 2:
                                print("\n")
                                query = "select id_game,any_value(id_player),min(bet) from ROUNDS group by id_game;"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID_PARTIDA'.ljust(15) + 'ID JUGADOR'.ljust(15) + 'APUESTA MÍNIMA')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(20) + str(i[2]).rjust(13))
                                input("\nEnter to continue")
                            if opc5 == 3:
                                print("\n")
                                query = "select id_game,any_value(id_player),max(bet) from ROUNDS group by id_game;"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID_PARTIDA'.ljust(15) + 'ID JUGADOR'.ljust(15) + 'APUESTA MAXIMA')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(20) + str(i[2]).rjust(13))
                                input("\nEnter to continue")
                            if opc5 == 4:
                                print(
                                    "---------------------------------------------------------In Contruction---------------------------------------------------------------------")
                                input("                                                        Enter to continue")
                            if opc5 == 5:
                                print("\n")
                                query = "select r.id_player,p.id_game,p.ending_points-p.starting_points from PLAYER_GAME p inner join PLAYER r on p.id_player=r.id_player where r.human=0 and (p.ending_points-p.starting_points)=(select max(pg.ending_points-pg.starting_points) from PLAYER_GAME pg where pg.id_game=p.id_game) order by p.ending_points-p.starting_points desc"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID JUGADOR'.ljust(15) + 'ID PARTIDA'.ljust(15) + 'PUNTOS FINALES')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(11) + str(i[2]).rjust(19))
                                input("\nEnter to continue")
                            if opc5 == 6:
                                print(
                                    "---------------------------------------------------------In Contruction---------------------------------------------------------------------")
                                input("                                                        Enter to continue")
                            if opc5 == 7:
                                print("\n")
                                query = "select id_game,count(distinct id_player)from ROUNDS where bank=TRUE group by id_game;"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID PARTIDA'.ljust(15) + 'JUGADORES BANCA EN LA PARTIDA')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(25))
                                input("\nEnter to continue")
                            if opc5 == 8:
                                print(
                                    "---------------------------------------------------------In Contruction---------------------------------------------------------------------")
                                input("                                                        Enter to continue")
                            if opc5 == 9:
                                print(
                                    "---------------------------------------------------------In Contruction---------------------------------------------------------------------")
                                input("                                                        Enter to continue")
                            if opc5 == 10:
                                print("\n")
                                query = "select r.id_game,round(avg(r.bet),2) from ROUNDS r inner join GAME g on r.id_game=g.id_game where g.number_rounds=r.round_number group by r.id_game;"
                                cur.execute(query)
                                row = cur.fetchall()
                                print('ID_PARTIDA'.ljust(15) + 'PUNTOS MEDIOS ULTIMA RONDA')
                                for i in row:
                                    print(str(i[0]).rjust(5) + str(i[1]).rjust(23))
                                input("\nEnter to continue")
                            if opc5 == 11:
                                m05 = False
                                m00 = True

                if opc == 6:
                    m00 = False
                    Salir = True