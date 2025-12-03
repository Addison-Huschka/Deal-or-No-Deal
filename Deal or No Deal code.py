#Created by Addison Huschka, Rebekah Peratt, and George Dinga


import random

class Briefcases:
    def __init__(self):
        self.cases = {} #collection data type 1, dictionary (used to store the number value pairs of the cases)
        self.opened_cases = set() #collection data type 2, set (used to keep track of which cases are open)
    def generate_cases(self): #this generates the cases with random amounts
        amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        random.shuffle(amounts)
        for number in range(1,27):
            self.cases[number] = amounts[number-1]
    def open_case(self,number): #this opens a case and reveals the amount inside
        if number in self.opened_cases:
            print(f'Case{number} has already been opened.')
        else:
            self.opened_cases.add(number)
            print(f'Case {number} contained ${self.cases[number]:,}')
    def remaining_amounts(self): #this returns the amounts in the unopened cases
        return [amt for num, amt in self.cases.items() if num not in self.opened_cases] #collection data type 3, list (used to store the remaining amounts in the unopened cases) There are also multiple instances of using lists



def banker_offer(game): #this is where we calculate the banker's offer
    offer = sum(game.remaining_amounts())/len(game.remaining_amounts())
    return offer
#I think we can just use the average for the bankers formula
#but if someone finds a different way that works too



def deal_or_no_deal():
    choice = input("Do you accept the banker's offer? Deal or no deal?: ").lower()
    return choice == "deal"



def show_remaining_case_values(game, player_case):
    remaining = game.remaining_amounts()
    remaining_sorted = sorted(remaining)
    
    print('\nThe remaining case values are:')
    for value in remaining_sorted:
        print(f'${value:,}')




def play_round(game, round_number, cases_to_open, player_case): #when called in the game, it will ask to open cases
    print(f'\nRound {round_number}: Open {cases_to_open} case(s).')
    opened_this_round = []
    
    for _ in range(cases_to_open): #this is how we open cases
        while True:
            try:
                case_number = int(input("Select a case to open (1-26): "))
                if case_number < 1 or case_number > 26:
                    print("Invalid case number. Please choose a number between 1 and 26.")
                elif case_number in game.opened_cases:
                    print("This case has already been opened. Please choose another.")
                elif case_number == player_case:
                    print("You cannot open your own case. Please choose another.")
                else:
                    game.open_case(case_number)
                    opened_this_round.append(case_number)
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 26.")


def get_winnings(entries): #helper function for sorting leaderboard entries
    return entries[1]
def create_leaderboard(player_name,winnings,filename="leaderboard.txt"): #creates/updates a leaderboard file that stores the top 5 scores
    entries = [] #list of tuples (name, score)
    try:
        with open(filename, "r") as file: #read existing leaderboard entries
            for line in file:
                name, score = line.strip().split(": $")
                entries.append((name, float(score.replace(",",""))))
    except FileNotFoundError:
        pass
        
    entries.append((player_name, winnings))
    entries.sort(key=get_winnings, reverse=True)
    entries = entries[:5]  # Keep only top 5 scores

    with open(filename, "w") as file: #write updated leaderboard entries
        for name, score in entries:
            file.write(f"{name}: ${score:,}\n")


def play_the_game():
    print("Welcome to Deal or No Deal!")
    player_name = input("\nEnter your name to start the game: ")
    game = Briefcases()
    game.generate_cases()

    while True: #this forces the player to pick a valid case number
        try:
            player_case = int(input(f"\nWelcome {player_name}! Pick your personal case (1-26): "))
            if player_case < 1 or player_case > 26:
                print("Invalid case number. Please choose a number between 1 and 26.")
            else:
                print(f"You have chosen case #{player_case} to keep until the end.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 26.")
    #I did the code above to make sure the player picks a valid case number and so that it is still included in the other calculations and remaining case values. I tested it so trust me that it works (:

    round_number = 1
    end_indicator = False
    
    while round_number < 9:
        if round_number < 5:    
            round_structure = [6,5,4,3,2] #number of cases to open each round
            round_number += 1
            play_round(game, round_number, round_structure[round_number-1], player_case)
            print(f"\nThe Banker offers ${banker_offer(game)}.")
            choice = deal_or_no_deal()
            if choice == "deal":
                print(f"\nCongratulations! You won ${banker_offer(game)}.")
                end_indicator = True
                break
            else:
                continue
        else:  #the if/else is here because after the 5th round the player only picks one case, but there are up to 9 rounds total
            round_number += 1
            play_round(game, round_number, 1, player_case)
            print(f"\nThe Banker offers ${banker_offer(game)}.")
            choice = deal_or_no_deal()
            if choice == "deal":
                print(f"\nCongratulations! You won ${banker_offer(game)}.")
                end_indicator = True
                break
            else:
                continue
    if end_indicator == False:
        for key in game.cases:
            if key not in game.opened_cases:
                last_case = key

        players_prize = int(input(f"\nThere are two remaining cases. Do you choose your case {player_case}, or the remaining case {last_case}? "))
        print(f"Congratulations! You won ${game.cases[last_case]}")

    create_leaderboard(player_name, winnings=game.cases[last_case])

play_the_game()