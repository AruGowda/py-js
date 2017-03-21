board = ['']*9


def plot_cell():
    print """
            | {0} | {1} | {2} |
            | {3} | {4} | {5} |
            | {6} | {7} | {8} |
            """.format(*board)
    print board


def make_a_move(cell, player):
    if cell in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        board[cell] = player
        print board
    else:
        raise ValueError("not a valid cell number")
    plot_cell()


def check_winner(player):
    if board[0] == board[1] == board[2] == player:
        print "winner is", board[0]
        return True
    if board[0] == board[4] == board[8] == player:
        print "winner is", board[0]
        return True
    if board[2] == board[4] == board[6] == player:
        print "winner is", board[2]
        return True
    if board[6] == board[7] == board[8] == player:
        print "winner is", board[6]
        return True
    if board[0] == board[3] == board[6] == player:
        print "winner is", board[2]
        return True
    if board[8] == board[5] == board[2] == player:
        print "winner is", board[2]
        return True
    if board[1] == board[4] == board[7] == player:
        print "winner is", board[2]
        return True
    if board[3] == board[4] == board[5] == player:
        print "winner is", board[2]
        return True


def is_board_full():
    return all(board)

if __name__ == "__main__":
    flag = True
    plot_cell()
    while flag:

        if is_board_full():
            print "board full"
            break

        cell_value = input("player 1: enter cell number?\n")
        make_a_move(cell_value, "p1")

        if check_winner("p1"):
            break

        if is_board_full():
            print "board full"
            break

        cell_value = input("player 2: enter cell number?\n")
        make_a_move(cell_value, "p2")

        if check_winner("p2"):
            break
