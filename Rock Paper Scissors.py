# https://ascii.co.uk/art

rock = '''
_      ___ _
|  _,-' _ `_)
|~'    ' `\()
|       (____)
|      (_____)
|--.____(___)

'''

paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' 
'''

scissor = '''
  .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/  
'''

from random import choice

choices = ["paper", "rock", "scissor"]
asci_art = {
    "scissor": scissor,
    "paper": paper,
    "rock": rock,
}
again = True
while again:
    try:
        user_choice = input("What do you choose? 'rock', 'paper', or 'scissor'?: ")
        print(asci_art[user_choice])
        computer_choice = choice(choices)
        print(f"computer choice is: {asci_art[computer_choice]}")
        if user_choice in choices:
            if user_choice != computer_choice:
                if (user_choice == "rock" and computer_choice == "scissor" or
                        user_choice == "paper" and computer_choice == "rock" or
                        user_choice == "scissor" and computer_choice == "paper"):
                    print("You win")
                else:
                    print("You lose!")
            else:
                print("it's a draw")
        again_user = input("Do you want play again? 'y' or 'n': ")
        if again_user == 'n':
            again = False
    except:
        print("You'r answer is not valid")
