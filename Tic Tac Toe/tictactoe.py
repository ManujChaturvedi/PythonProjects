from IPython.display import clear_output

def display_board(board):
    print('|_{}_|_{}_|_{}_|'.format(board[7],board[8],board[9]))
    print('|_{}_|_{}_|_{}_|'.format(board[4],board[5],board[6]))
    print('| {} | {} | {} |'.format(board[1],board[2],board[3]))



#Take User input and validate the user input.
def player_input():
  choice = "Wrong"
  valids = ['1','2','3','4','5','6','7','8','9']

  while choice not in valids:
    choice = input("Please enter your choice here (1-9): ")

    if not choice.isdigit():
      print("Please enter a valid integer here.")
    else:
      if choice not in valids:
        print("Please eneter a valid integer in between the range (1-9)")

  return int(choice)


# Check if the place on the board is empty or not that the user have entered if not return false?
def check_space(board, position):
  if board[position] == ' ':
    return True
  return False


def place_the_marker(board, position, marker):
  if check_space(board, position):
    board[position] = marker
  else:
    print("Please try again.")
  return board

# Check if a player won or not ?
def check_win(board,mark):
  if board[7]==mark and board[8]==mark and board[9]==mark:
      return True
  elif board[4]==mark and board[5]==mark and board[6]==mark:
      return True
  elif board[1]==mark and board[2]==mark and board[3]==mark:
      return True
  elif board[7]==mark and board[4]==mark and board[1]==mark:
      return True
  elif board[8]==mark and board[5]==mark and board[2]==mark:
      return True
  elif board[9]==mark and board[6]==mark and board[3]==mark:
      return True
  elif board[7]==mark and board[5]==mark and board[3]==mark:
        return True
  elif board[9]==mark and board[5]==mark and board[1]==mark:
      return True
  else:
      return False

def isBoardFull(board):
  for i in board:
    if i==' ':
      return False
  return True

# Ask the player if he wants to continue or not ?
def replay():
  user_input = input("Do you want to still play ?")
  user_input=user_input.lower()

  if user_input=='yes':
    return True
  return False


def switch_player(player,mark):
  if player==1:
    return (2,'O')
  else:
    return (1,'X')

def play():
  game_on=True
  board = [' '] * 10
  board[0] = '#'

  current_player = 1
  current_marker='X'

  print("---Welcome to tic tac toe--- \n")

  board = [' '] * 10
  board[0] = '#'

  while game_on:
    display_board(board)
    
    print(f"It's Player {current_player} turn --- ")
    position =  player_input()

    board=place_the_marker(board, position, current_marker)

    if check_win(board,current_marker):
      print(f"Congrats, player {current_player} won !")
      display_board(board)
      game_on = replay()
      board = [' '] * 10
      board[0] = '#'
    elif isBoardFull(board):
      print("Draw!")
      game_on = replay()
      board = [' '] * 10
      board[0] = '#'
    else:
      current_player,current_marker = switch_player(current_player,current_marker)
    

play()
