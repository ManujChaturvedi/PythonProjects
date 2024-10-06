import random

def guess(x):
  random_number = random.randint(1,x)
  guess=0
  while guess!=random_number:
    guess = int(input(f" Guess a number between 1 and {x} "))
    if (guess<random_number): {
      print(" Sorry guess again. Guess is too low. ")
    }
    elif (guess>random_number): {
      print(" Sorry guess again. Guess is too high. ")
    }

  print(f" Your guess is correct. {random_number}. ")


def computer_guess(x):
  low = 1
  high = x
  feedback = ""
  while feedback!='c':
    if(low!=high):
      guess = random.randint(low,high)
    else:
      guess = low

    feedback = input(f"Is {guess} is too High(H), too low(L) or correct(C)").lower()

    if(feedback == 'h'):
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

  print(f"Yay! Computer guessed the number correctly. The number was {guess}")  


# guess(10)
computer_guess(10)