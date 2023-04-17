
import sys
# Print the board
def printboard(board):
    print('----------------------------------')
    for row in board:
        print(*row, sep="\t")

def AIPlay(board):
    #to find the best cordinate and place the value X
    bestMove = findBestMove(board)
    board[bestMove[0]][bestMove[1]]='x'
    print("AI Played")
    printboard(board)
    #To Check who won
    if (Checkwon(board) == 1):
        print("\nAI Won")
        sys.exit()
    elif  (Checkwon(board) == -1):
        print("\nOpponent Won")
        sys.exit()
    elif  (isMovesLeft(board) == False) :
        print("\nIt's a draw !")
        sys.exit()

def Checkwon(board) :
    # Checking for Rows for X or O victory.
    for i in range(3) :    
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            if (board[i][0] == 'x') :
                return 1
            else :
                return -1

    # Checking for Columns for X or O victory.
    for i in range(3) :
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            if (board[0][i] == 'x') :
                return 1
            else:
                return -1

    # Checking for Diagonals for X or O victory.
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_'):
        if (board[0][0] == 'x') :
            return 1
        else :
            return -1

    if (board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_') :
        if (board[0][2] == 'x') :
            return 1
        else:
            return -1

    # Else if none of them have won then return 0
    return 0

def isMovesLeft(board) :
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == '_') :
                return True
    return False



def minimax(board, depth, player, alpha, beta):
    score = Checkwon(board)
    if score == 1:
        return 10 - depth
    if score == -1:
        return depth - 10
    if not isMovesLeft(board):
        return 0

    if player == 'x':
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, 'o', alpha, beta))
                    alpha = max(alpha, best)
                    board[i][j] = '_'

                    # Alpha-beta pruning
                    if beta <= alpha:
                        break
        return best

    # If this minimizer's move
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'o'
                    best = min(best, minimax(board, depth + 1, 'x', alpha, beta))
                    beta = min(beta, best)

                    # Undo the move
                    board[i][j] = '_'

                    # Alpha-beta pruning
                    if beta <= alpha:
                        break
        return best



def findBestMove(board):
    bestVal = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':

                board[i][j] = 'x'
                moveVal = minimax(board, 0, 'o', alpha, beta)

                board[i][j] = '_'

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove




board = [
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]
]

print("Hi Welcome to Unbeatable TicTacToe")
input("Press Enter to Continue !!")
AIPlay(board)

while True :
    n = input("What's the position of Your Move? (1-9)\n")
    match n:
        case "1":
            if (board [0][0] != '_'):
                print("Invalid move do Again")
            else:    
                board [0][0]='o'
                AIPlay(board)
        case "2":
            if (board [0][1] != '_'):
                print("Invalid move do Again")
            else:
                board [0][1]='o'
                AIPlay(board)
                        
        case "3":
            if (board [0][2] != '_'):
                print("Invalid move do Again")
            else:
                board [0][2]='o'
                AIPlay(board)         
        case "4":
            if (board [1][0] != '_'):
                print("Invalid move do Again")
            else:
                board [1][0]='o'
                AIPlay(board)         
        case "5":
            if (board [1][1] != '_'):
                print("Invalid move do Again")
            else:
                board [1][1]='o'
                AIPlay(board)     
        case "6":
            if (board [1][2] != '_'):
                print("Invalid move do Again")
            else:
                board [1][2]='o'
                AIPlay(board)    
        case "7":
            if (board [2][0] != '_'):
                print("Invalid move do Again")
            else:
                board [2][0]='o'
                AIPlay(board)
        case "8":
            if (board [2][1] != '_'):
                print("Invalid move do Again")
            else:
                board [2][1]='o'
                AIPlay(board)     
        case "9":
            if (board [2][2] != '_'):
                print("Invalid move do Again")
            else:
                board [2][2]='o'
                AIPlay(board)     
        case _:
            print("Wrong Input")





