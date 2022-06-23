import random

import utilities as utils

# creates a ship based on row and columns from the sea using dictionary
def createShip(sea):

    minRow = 0
    maxRow = len(sea)

    minColumn = 0
    maxColumn = len(sea[0])

    shipRow = random.randrange(minRow, maxRow)
    shipColumn = random.randrange(minColumn, maxColumn)

    startCoordinate = [shipRow, shipColumn]

    isHorizontal = random.choice([True, False])

    coordinates = createShipCoordinates([], startCoordinate, 3, isHorizontal)

    return {
        "isHorizontal" : isHorizontal,
        "coordinates" : coordinates,
        "isBombed" : False
    }

# prints the ship information for debugging purpose
def printShip(ship):

    print(
        "isHorizontal: {}\ncoordinates: {}\nisBombed: {}".format(
            ship["isHorizontal"], ship["coordinates"], ship["isBombed"]
        )
    )

# creates the ship coordinates based on the starting coordinate
# to expand the ships body based on the length given and 
# orientation of the ship (isHorizontal)
# each of the ships coordinate are recursively appended into the coordinates list
# one at a time
def createShipCoordinates(coordinates, startCoordinate, length, isHorizontal):

    if length == 0:
        return coordinates

    elif length > 0:

        if len(coordinates) == 0:
            coordinates.append(startCoordinate)

        else:
            if isHorizontal == True:
                row = startCoordinate[0]
                column = startCoordinate[1] + len(coordinates)

            elif isHorizontal == False:
                row = startCoordinate[0] + len(coordinates)
                column = startCoordinate[1]

            coordinates.append([row, column])

    return createShipCoordinates(coordinates, startCoordinate, length - 1, isHorizontal)

# check if both ship are the same in terms of having the same coordinate
# by recursively increasing the index of ship1 one at a time 
# to compare its coordinate with the list of coordinates in ship2
def isShipEqual(index, ship1, ship2):

    if index == len(ship1["coordinates"]):
        return False

    elif index < len(ship1["coordinates"]):

        coordinate = ship1["coordinates"][index]
        coordinates = ship2["coordinates"]

        if utils.isCoordinateInCoordinates(coordinate, coordinates) == True:
            return True

    return isShipEqual(index + 1, ship1, ship2)

# checks if both the ship are the same in terms of having the same coordinate
# by recursively shrinking the list of ships one at a time and comparing
# the ship with the first ship in the list of ships
def isShipInShips(ship, ships):

    if len(ships) == 0:
        return False

    elif isShipEqual(0, ship, ships[0]) == True:
        return True

    return isShipInShips(ship, ships[1:])

# creates ships based on the number of ships provided and based on the
# rows and columns of the sea by recursively decreasing the numOfShips value
# if the ship created is not a duplicate with any ship in the list of ships
def createShips(ships, numOfShips, sea):

    if numOfShips == 0:
        return ships

    elif numOfShips > 0:

        ship = createShip(sea)

        if utils.isShipOutOfRange(0, ship, sea) == False:

            if numOfShips == 1:
                ships.append(ship)
                numOfShips -= 1

            else:

                if isShipInShips(ship, ships) == False:
                    ships.append(ship)
                    numOfShips -= 1

    return createShips(ships, numOfShips, sea)
