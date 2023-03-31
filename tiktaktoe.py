def print_board(board):
    print("-------------")
    for i in range(3):
        print("|",end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")
    
def check_win(board, player):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return True
        if board[0][i]==board[1][i]==board[2][i]==player:
            return True    
    if board[0][0]==board[1][1]==board[2][2]==player:
            return True        
    if board[0][2]==board[1][1]==board[2][0]==player:
            return True
    return False

def tik_tak_toe():
     board=[[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
     current_player= "X"
     while True:
          print_board(board)
          row = int(input(f"{current_player}, Choose your row (0 to 2)"))
          col = int(input(f"{current_player}, Choose your column (0 to 2)"))
          if board[row][col] !=" ":
               print("The spot is already taken")
               continue
          board[row][col]=current_player
          if check_win(board, current_player):
               print_board(board)
               print(f"{current_player} wins :")
               break
          if all(" " not in row for row in board):
               print_board(board)
               print("Game is tie now")
               break
          current_player="O" if current_player=="X" else "X"

          
          
          
tik_tak_toe()
