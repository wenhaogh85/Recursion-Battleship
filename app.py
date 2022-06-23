import seaLib
import shipLib
import userLib
import utilities as utils

def getUserOption():

    while True:

        print(
            "\n===============================================================" +
            "\n                     Welcome to Battleship" +
            "\n===============================================================" +
            "\n          Your goal is to bomb 5 ships! Good luck!" +
            "\n===============================================================" +
            "\nChoose a level based on the options below:\n" +
            "\n+--------+--------------+-----------------+-----------------+" +
            "\n| Option |    Level     | Number of ships | Number of Bombs |" +
            "\n+--------+--------------+-----------------+-----------------+" +
            "\n|   1    | Beginner     |       30        |       15        |" +
            "\n+--------+--------------+-----------------+-----------------+" +
            "\n|   2    | Intermediate |       20        |       15        |" +
            "\n+--------+--------------+-----------------+-----------------+" +
            "\n|   3    | Expert       |       10        |       15        |" +
            "\n+--------+--------------+-----------------+-----------------+\n" +
            "\n---------------------------------------------------------------\n"
        )

        option = input("Enter option: ")

        if option == "1" or option == "2" or option == "3":
            return option

        else:
            print("That was an invalid option. Try again...")

def getValidUserInput(user, sea):

    while True:

        userCoordinate = userLib.getUserCoordinate()

        if userCoordinate[0] == -1 and userCoordinate[1] == -1:
            return [-1, -1]

        elif userCoordinate[0] == -2 and userCoordinate[1] == -2:
            return [-2, -2]

        elif utils.isUserOutOfRange(userCoordinate, sea) == True:
            utils.printHeaderMessage(
                "-",
                "That coordinate was out of range. Please try again..."
            )

        elif utils.isCoordinateInCoordinates(userCoordinate, user["previousCoordinates"]) == True:
            utils.printHeaderMessage(
                "-",
                "That coordinate has been entered before. Please try again..."
            )

        else:
            return userCoordinate

# -------------------------------------------------------------------
# initialises sea and ships list
sea = seaLib.createSea(10, 30, ".")
user = userLib.createUserProfile(bombsLeft = 15)
numOfShips = 0

# gets user option
option = getUserOption()
level = ""

# interprets user option
if option == "1":
    level = "Beginner"
    numOfShips = 30

elif option == "2":
    level = "Intermediate"
    numOfShips = 20

elif option == "3":
    level = "Expert"
    numOfShips = 10

# initialses the game
ships = shipLib.createShips([], numOfShips, sea)
utils.printHeaderMessage("-", "Level: " + level)

while user["bombsLeft"] != 0 and user["shipsHit"] != 5:

    seaLib.printSea(sea)
    print("\nEnter coordinate 0 0 to quit anytime")

    userLib.displayUserStatus(user)

    userInput = getValidUserInput(user, sea)

    if userInput[0] == -1 and userInput[1] == -1:
        break

    elif userInput[0] == -2 and userInput[1] == -2:
        utils.revealAllShips(ships)

    else:
        ship = utils.isBombShip(userInput, ships)

        if ship != None:

            if ship["isBombed"] == True:
                utils.printHeaderMessage(
                    "-",
                    "This ship has been bombed before. Try again..."
                )

            else:
                ship["isBombed"] = True
                userLib.updateUserStatus(user, userInput, isBombShip = True)
                seaLib.updateSeaStatus(sea, ship["coordinates"], "O")

                utils.printHeaderMessage(
                    "-",
                    "You have bombed a ship!! :)"
                )

        else:
            userLib.updateUserStatus(user, userInput, isBombShip = False)
            seaLib.updateSeaStatus(sea, [userInput], "X")

            utils.printHeaderMessage(
                "-",
                "You missed the ship :'("
            )

if user["shipsHit"] == 5:
    utils.printHeaderMessage("*", "You win :)")

elif user["shipsHit"] < 5 and user["bombsLeft"] == 0:
    utils.printHeaderMessage("*", "You lose :'(")

utils.printHeaderMessage("*", "Game Over!!\nThank you for playing battleship :)")