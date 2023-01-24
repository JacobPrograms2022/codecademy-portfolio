# main executable for game
import json
import random

with open("players.json", "r") as f:
    player_file = json.load(f)

score = 0

class Player:
    def __init__(self, username, score = 0, games_won = 0, games_lost = 0):
        self.username = username
        self.score = score
        self.games_won = games_won
        self.games_lost = games_lost


def create_player():
    # player creation, saved in file
    pass

def hangman():
    # main logic of game
    pass

def end():
    # exit out of program
    print("\nGood Bye, thank you for playing.")
    exit()

def main():
    # the loop that the game resides and general menu statements
    while True:
        play = input("Play Game?(y/n): ")
        play.lower()
        if play == "y":
            print("\nWelcome to Ark Hangman!")
            print("Select Player: 1\nCreate Player: 2")
            option = int(input("-->: "))

            if option == 1:
                player = input("Please type your username: ")

            elif option == 2:
                pass
            else:
                print("Option not recognised.")
            
        elif play == "n":
            end()
        else:
            print("Option not recognised.")
main()

