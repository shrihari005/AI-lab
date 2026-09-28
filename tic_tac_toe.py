board = ["O" , " " , "X", "X" , " " , " " ,"X" , "O" , "O" ]
player = "X"

pathcost = {"X" : 0 , "O" : 0}

for turn in range(3):

    print(f"\n{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}\n")

    move = int(input(f"Player {player}, enter position (0-8): "))
    if board[move] == " ":
        board[move] = player
        pathcost[player] += 1
    else:
        print("Taken....!")

    b = board
    if (b[0]==b[1]==b[2]==player or b[3]==b[4]==b[5]==player or b[6]==b[7]==b[8]==player or
        b[0]==b[3]==b[6]==player or b[1]==b[4]==b[7]==player or b[2]==b[5]==b[8]==player or
        b[0]==b[4]==b[8]==player or b[2]==b[4]==b[6]==player):
        print(f"\nPlayer {player} wins! ")
        break
    player = "O" if player == "X" else "X"
else:
    print("\nIt's a tie! ")

print(f"Path cost X = {pathcost['X']}")
print(f"Path cost O = {pathcost['O']}")
