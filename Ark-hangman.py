# main executable for game
import csv
import random

players = open("players.csv")
players_dict_file = csv.DictReader(players)
data = []
for row in players_dict_file:
    data.append(row)

score = 0
players_list = []
class Player:
    def __init__(self, username, score = 0, games_won = 0, games_lost = 0):
        self.username = username
        self.score = score
        self.games_won = games_won
        self.games_lost = games_lost
        self.player_dict = {
            "username":self.username, "score":self.score, "games_won": self.games_won, "games_lost": self.games_lost
            }
        players_list.append(self.player_dict)
        


def create_player(username):
    player = Player(username)
    with open("players.csv", "a", newline="") as f:
        headersCSV = [i for i in player.player_dict.keys()]
        entries = csv.DictWriter(f, fieldnames=headersCSV)
        entries.writerow(player.player_dict)
        f.close()

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
                username = input("Please type your username: ")

            elif option == 2:
                create = True
                while create == True:

                    username = input("Please create a username: ")
                    username.strip().lower()

                    if all(not data[name]["Username"] == username for name in range(len(data))):
                        create_player(username)
                        create = False
                    else:
                        print("Username already taken.")
                        
            

            else:
                print("Option not recognised.")
            
        elif play == "n":
            end()
        else:
            print("Option not recognised.")
main()

