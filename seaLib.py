# creates a sea based on the number of rows, columns and symbol provided
# by using list comprehension
def createSea(rows, columns, symbol):

    return [[symbol for column in range(columns)] for row in range(rows)]

# prints the sea
def printSea(sea):

    rows = len(sea)
    columns = len(sea[0])

    print(end="   ")
    printColumnA1(start = 1, end = columns // 10)

    print(end="   ")
    printColumnB1(start = 1, end = columns // 10)

    printRows(start = 1, end = rows, rows = sea)

# prints the topmost column using printColumnA2 
# and bottom column using printColumnB1
# based on the range of start and end by recursively
# increasing the value of start one at a time
def printColumnA1(start, end):

    if start > end:
        print()
        return

    elif start <= end:
        printColumnA2(1, start)

    printColumnA1(start + 1, end)

# prints the topmost columns by printing whitspace (nothing)
# if the column value is less than 10 and print the value in tenth places
# if the column value is 10 by recursively increasing the 
# column value by one at a time
def printColumnA2(columns, numOfTenth):

    TENTH_PLACE = 10
    nothing = " "

    if columns == TENTH_PLACE:
        print(numOfTenth, end=" ")
        return

    elif columns < TENTH_PLACE:
        print(nothing, end=" ")

    printColumnA2(columns + 1, numOfTenth)

# prints bottom column using printColumnB2
# based on the range of start and end by recursively
# increasing the value of start one at a time
def printColumnB1(start, end):

    if start > end:
        print()
        return

    elif start <= end:
        printColumnB2(1)

    printColumnB1(start + 1, end)

# prints the bottom column by recursively increasing
# the value of the columns one at a time
def printColumnB2(columns):

    TENTH_PLACE = 10

    if columns == TENTH_PLACE:
        print("0", end=" ")
        return

    elif columns < TENTH_PLACE:
        print(columns, end=" ")

    printColumnB2(columns + 1)

# prints the row number, and prints the sea using the printRow
# based on the range of start and end
# by recursively increasing the start value and shrinking the
# rows of the sea one at a time
def printRows(start, end, rows):

    TENTH_PLACE = 10

    if start > end and len(rows) == 0:
        return

    elif start <= end:

        if start < TENTH_PLACE:
            print(" {}".format(start), end=" ")

        else:
            print("{}".format(start), end=" ")

        printRow(rows[0])

    printRows(start + 1, end, rows[1:])

# prints a row (list) of the sea based on the index value of the column
# by recursively shrinking the row (list) one column at a time
def printRow(columns):

    if len(columns) == 0:
        print()
        return

    elif len(columns) > 0:
        print(columns[0], end=" ")

    printRow(columns[1:])

# updates the sea 2D list based on the coordinates row and columns
# by recursively reducing the list of coordinates one
# coordinate at a time
def updateSeaStatus(sea, coordinates, symbol):

    if len(coordinates) == 0:
        return

    elif len(coordinates) > 0:

        row = coordinates[0][0]
        column = coordinates[0][1]

        sea[row][column] = symbol

    return updateSeaStatus(sea, coordinates[1:], symbol)