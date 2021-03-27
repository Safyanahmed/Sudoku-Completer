board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# backtracking to find another solution and to see if board is complete meaning a solution has been found.
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    # go through 1-9 across board and check is valid solution has been added. if it has then repeat solve again using if statement.
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            # repeat solve function.
            if solve(bo):
                return True
            # if value added doesn't work change it back to 0.
            bo[row][col] = 0

    return False

# define board to check if it is valid using board, number and position.
# check row
def valid(bo, num, pos):
    # check each column in row and if a number is equal to the number that we have added in.
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column for same numbers.
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box by diving by position by 3.
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # check box for same numbers.
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

        return True

# for loop - add in spaces for line for every increment of 3 digits.
def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

# for loop - get all rows and then print vertical lines. j != 0 makes sure no lines on left side.
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# nested for loop -  find an empty square on board which is essentially is a 0.
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # find row first, then col.

print_board(board)
solve(board)
print("#########################")
print_board(board)