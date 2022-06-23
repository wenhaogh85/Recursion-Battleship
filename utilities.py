import shipLib

# reveals all ship coodinates that has not been bombed
def revealAllShips(ships):

    for ship in ships:

        if ship["isBombed"] == False:
            print("\n" + ("*" * 50))
            shipLib.printShip(ship)

# prints messages to the user
def printHeaderMessage(symbol, message):

    print(
        "\n" + (symbol * 63) +
        "\n" + message +
        "\n" + (symbol * 63) + "\n"
    )

# returns False if both coordinates are not equal
def isCoordinateEqual(coordinate1, coordinate2):

    isRowEqual = coordinate1[0] == coordinate2[0]
    isColumnEqual = coordinate1[1] == coordinate2[1]

    if isRowEqual == True and isColumnEqual == True:
        return True
    else:
        return False

# checks if the coordinate is in list of coordinates
# by recursively shrinking the list and only comparing
# the first coordinate from the list of coordinates
def isCoordinateInCoordinates(coordinate, coordinates):

    if len(coordinates) == 0:
        return False

    elif isCoordinateEqual(coordinate, coordinates[0]) == True:
        return True

    return isCoordinateInCoordinates(coordinate, coordinates[1:])

# checks if the ship coordinates is out of range from the sea
# by recursively increasing the index of the ship coordinate one at a time
def isShipOutOfRange(index, ship, sea):

    maxRow = len(sea) - 1
    maxColumn = len(sea[0]) - 1

    if index > len(ship["coordinates"]):
        return False

    elif index < len(ship["coordinates"]):

        if ship["coordinates"][index][0] > maxRow or ship["coordinates"][index][1] > maxColumn:
            return True

    return isShipOutOfRange(index + 1, ship, sea)

# checks if the user coordinate is out of range from the sea
def isUserOutOfRange(coordinate, sea):

    maxRow = len(sea) - 1
    maxColumn = len(sea[0]) - 1

    if coordinate[0] > maxRow or coordinate[1] > maxColumn:
        return True

    if coordinate[0] < 0 or coordinate[1] < 0:
        return True

    return False

# checks if the user coodinate is in a list of ships coordinates
# by recursively shrinking the list of ships and only comparing
# the first coordinate from the list of coordinates
def isBombShip(userCoordinate, ships):

    if len(ships) == 0:
        return None

    elif len(ships) > 0:

        if isCoordinateInCoordinates(userCoordinate, ships[0]["coordinates"]) == True:
            return ships[0]

    return isBombShip(userCoordinate, ships[1:])