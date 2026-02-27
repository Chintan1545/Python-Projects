## Rock Paper Scissor Game with python

import random

item_list = ['Rock','Paper','Scissor']
user_choice = input("Enter your move = Rock,Paper,Scissor: ")
computer_choice = random.choice(item_list)
print(f"User choice = {user_choice} and computer choich = {computer_choice}")

if user_choice == computer_choice:
    print("Both chooese same: -> Match Tie")

elif user_choice =='Rock':
    if computer_choice == 'Paper':
        print("Paper covers Rock: -> Computer win")
    else:
        print("Rock smashes Scissor: -> You win")

elif user_choice =='Paper':
    if computer_choice == 'Scissor':
        print("Scissor cuts Paper: -> Computer win")
    else:
        print("Paper covers Rock: -> You win")

elif user_choice =='Scissor':
    if computer_choice == 'Paper':
        print("Scissor cuts Paper: -> You win")
    else:
       print("Rock smashes Scissor: -> Computer win")


## output 1 
'''
Enter your move = Rock,Paper,Scissor:  Rock
User choice = Rock and computer choich = Scissor
Rock smashes Scissor: -> You win
'''
## output 2
'''
Enter your move = Rock,Paper,Scissor:  Paper
User choice = Paper and computer choich = Paper
Both chooese same: -> Match Tie
'''
## output 3
'''
Enter your move = Rock,Paper,Scissor:  Scissor
User choice = Scissor and computer choich = Rock
Rock smashes Scissor: -> Computer win
'''