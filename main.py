from random import randint
board = [['-','-','-'],['-','-','-'],['-','-','-']]
player = ""
game_is_on = True
winner = ""

def check_win():
    global winner
    # horizontal
    for i in range(3):
        if board[i].count("X") == 3 or board[i].count("O") == 3:
            winner = board[i][0]
            return True
    # vertical
    for i in range(3):
        if board[0][i] + board[1][i] + board[2][i] =="XXX" or board[0][i] + board[1][i] + board[2][i] == "OOO":
            winner = board[0][i]
            return True

    #diagonal
    if board[0][0] + board[1][1] + board[2][2] == "XXX" or board[0][0] + board[1][1] + board[2][2] == "OOO":
        winner = board[0][0]
        return True
    if board[0][2] + board[1][1] + board[2][0] == "XXX" or board[0][2] + board[1][1] + board[2][0] == "OOO":
        winner = board[0][0]
        return True

    #draw - doesn't work
    count = 0
    for i in range(3):
        if "-" not in board[i]:
            count += 1

    if count == 3:
        winner = "no-one "
        return True
    print(count)

    return False





def boardLayout():
    global player, game_is_on
    for i in range(3):
     print(board[i])
    player = input("place an X using coordinates (row,col): ")
    player = str.replace(player, ",", "")

    if player == "stop":
        game_is_on = False
        quit()

def npc():
    rand_x = randint(0, 2)
    rand_y = randint(0, 2)

    if board[rand_x][rand_y] != "-":
        npc()
    else:
        board[rand_x][rand_y] = "O"





while game_is_on:
    boardLayout()

    if check_win():
        print(f"{winner} wins")
        quit()


    x = int(player[0])-1
    y = int(player[1])-1

    #print(f"{x},{y}")



    board[x][y] = "X"
    check_win()
    npc()


