import random

def play():
  user = input("Type 'r' for ROCK, 's' for SCISSOR or 'p' for PAPER. ")
  computer = random.choice(['s','r','p'])
  if computer == user:
    print("It's a tie. :( ")
    return

  if win(user, computer):
    print(f" Congrats! You won! The computer choose {computer}")
    return 
  
  print(f"Too bad. You lost. The computer choose {computer}")


def win(player, opponent):
  if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
    return True


play()