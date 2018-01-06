"""
Implementing RPSLS for Practice Project
"""

import random

def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and return integer (0-1-2-3-4)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        pass
        
def number_to_name(number):
    """
    Take number as input (0-1-2-3-4)
    and return name (rock-Spock-paper-lizard-scissors)
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        pass
        
def rpsls(player_choice):
    """
    Take player_choice in the form of a string,
    play a game of RPSLS,
    and print results to the console.
    """
    print()
    print("Player chooses   " + player_choice)
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses " + comp_choice)
    
    difference = (player_number - comp_number) % 5
    
    if difference == 0:
        print("Player and Computer tied!")
    elif difference == 3 or difference == 4:
        print("Computer wins!")
    elif difference == 1 or difference == 2:
        print("Player wins!")
    else:
        pass

	
print("#### Testing name_to_number ####")
print(name_to_number("rock"))           # output - 0
print(name_to_number("Spock"))          # output - 1
print(name_to_number("paper"))          # output - 2
print(name_to_number("lizard"))         # output - 3
print(name_to_number("scissors"))       # output - 4
print(name_to_number("bad choice"))     # output - None

print("#### Testing number_to_name ####")
print(number_to_name(0))                # output - rock
print(number_to_name(1))                # output - Spock
print(number_to_name(2))                # output - paper
print(number_to_name(3))                # output - lizard
print(number_to_name(4))                # output - scissors
print(number_to_name(5))                # output - None

print("#### RPSLS ####")
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
