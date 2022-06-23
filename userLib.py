# creates a user profile using dictionary
def createUserProfile(bombsLeft):

    return {
        "previousCoordinates" : [],
        "bombsLeft" : bombsLeft,
        "shipsHit" : 0
    }

# updates the user status when the user bomb or miss a ship
def updateUserStatus(user, coordinate, isBombShip):

    user["previousCoordinates"].append(coordinate)

    if isBombShip == True:
        user["shipsHit"] = user["shipsHit"] + 1

    user["bombsLeft"] = user["bombsLeft"] - 1

# displays the user status to the user during the game
def displayUserStatus(user):

    print("\nbombs left: {}\nships hit: {}".format(user["bombsLeft"], user["shipsHit"]))

# prompts the user to enter a coordinate
def getUserCoordinate():

    while True:

        try:
            userRow, userColumn = map(int, input("\nEnter coordinate: ").split())
            break

        except ValueError:
            print("That was an invalid coordinate. Try again...")

    return [userRow - 1, userColumn - 1]
