#Created by Addison Huschka, Rebekah Peratt, and George Dinga


import random
    
class Briefcases:
    def __init__(self):
        self.cases = {} #collection data type 1, dictionary (used to store the number value pairs of the cases)
        self.opened_cases = set() #collection data type 2, set (used to keep track of which cases are open)
    def generate_cases(self):
        amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        random.shuffle(amounts)
        for number in range(1,27):
            self.cases[number] = amounts[number-1]
    def open_case(self,number):
        if number in self.opened_cases:
            print(f'Case{number} has already been opened.')
        else:
            self.opened_cases.add(number)
            print(f'Case {number} contained ${self.cases[number]:,}')
    def remaining_amounts(self):
        return [amt for num, amt in self.cases.items() if num not in self.opened_cases] #this is our 3rd collection data type, list (used to store the remaining amounts in the unopened cases) There are also multiple instances of using lists

def banker_offer(game): #banker_offer(game_1) to run
    offer = sum(game.remaining_amounts())/len(game.remaining_amounts())
    return offer
#this is before the next function because I thought it made more sense here lol
#I think we can just use the average for the bankers formula
#but if someone finds a different way that works too

def deal_or_no_deal():
    choice = input("Do you accept the banker's offer? (deal or no deal): ").lower()
    return choice

def show_remaining_case_values(game, player_case):
    remaining = game.remaining_amounts()
    remaining.append(game.cases[player_case])
    remaining_sorted = sorted(remaining)
    
    print('\nThe remaining case values are:')
    for value in remaining_sorted:
        print(f'${value:,}')

def play_round(game, round_number, cases_to_open, player_case):
    print(f'\nRound {round_number}: Open {cases_to_open} case(s).')
    opened_this_round = []
    
    #for _ in range(cases_to_open):
#this is how we open cases

def play_the_game():
    print("Welcome to Deal or No Deal!")
    player_name = input("Enter your name to start the game: ")
    game = Briefcases()
    game.generate_cases()

#pick player case at some point which replaces:
'''user_case = int(input("Pick a case number 1-26: "))
user_case_value = casevalues.pop(user_case)
casevalues[0] = user_case_value'''

#def create/update_leaderboard(): 
# idk which is a better name lol
#This is how we implement a file
#it will be called every time we play so maybe update instead of create

play_the_game()