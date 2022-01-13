

def main():
    person = change_person("")
    board = print_board()
    while not (draw(board) or winner(board)):
        create_board(board)
        next_move(person, board)
        person = change_person(person)
        if person == "x":
            winningPlayer = "o"
        elif person == "o":
            winningPlayer = "x"    
    create_board(board)
    if draw(board):
        print("It's a draw.")
    elif winner(board):
        print(f"{winningPlayer} is the winner!")
    print("Good game. Thanks for playing!")


def print_board():
    board = []
    for tile in range(9):
        board.append(tile + 1)
    return board


def create_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def draw(board):
    for tile in range(9):
        if board[tile] != "x" and board[tile] != "o":
            return False
    return True
    

def next_move(person, board):
    tile = int(input(f"It's {person}'s turn to choose a tile (1-9): "))
    board[tile - 1] = person


def change_person(currentTile):
    if currentTile == "" or currentTile == "o":
        return "x"
    elif currentTile == "x":
        return "o"


if __name__ == "__main__":
    main()
