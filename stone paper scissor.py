#importing the random module
import random


# step 1: Take input from 
user_choice= input('Pick your move [rock, paper, scissor]: ')
#random.choice(['Rock', 'Peper', 'Scissor'])
# this cammand pick a string randomly from 'Rock', 'Paper', 'Scissor'
# and assign it to the computer_choice variable 
computer_choice= input('Pick computer move [rock, paper, scissor]: ')
'''
#print the input taken
print(user_choice, computer_choice)
'''

# lets create the logic
if user_choice== 'rock' and  computer_choice== 'rock':
    print('Draw')
elif user_choice== 'rock' and computer_choice== 'peper':
    print('Computer Won')
elif user_choice== 'rock' and computer_choice== 'scissor':
    print('user won')
elif user_choice== 'paper' and computer_choice== 'rock':
    print('user won')
elif user_choice== 'paper' and computer_choice== 'paper':
    print('Draw')
elif user_choice== 'paper' and computer_choice== 'scissor':
    print('Computer Won')
elif user_choice== 'scissor' and computer_choice== 'rock':
    print('Computer Won')
elif user_choice== 'scissor' and computer_choice== 'paper':
    print('user won')
elif user_choice== 'scissor' and computer_choice== 'scissor':
    print('Draw')
