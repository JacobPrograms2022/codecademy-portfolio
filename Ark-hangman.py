# main executable for game
import csv
import random
import json



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
        
def find_data():
    players = open("players.csv")
    players_dict_file = csv.DictReader(players)
    data = []
    for row in players_dict_file:
        data.append(row)
    return data

data = find_data()

def create_player(username):
    player = Player(username)
    with open("players.csv", "a", newline="") as f:
        headersCSV = [i for i in player.player_dict.keys()]
        entries = csv.DictWriter(f, fieldnames=headersCSV)
        entries.writerow(player.player_dict)
        f.close()

def player_stats(username, data):
    # finds player data and returns it
    player_data = []
    for i in data:
        if i["Username"] == username:
            player_data.append(i["Score"])
            player_data.append(i["Games Won"])
            player_data.append(i["Games Lost"])
            break
    return player_data

def random_word():
    with open("dinos.txt", "r") as f:
        dinos = f.readlines()
        word = dinos[random.randrange(0, len(dinos))]
        return word

def hangman(dino):
    # main logic of game
    incorrect_guesses = 0
    with open("hangman.json", "r") as f:
        figure = json.load(f)

    win = False
    print("Lets Play Hangman!\n")
    board = ["_"]*len(dino)
    print(board)
    letters = list(dino)

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
                select = True
                while select == True:
                    username = input("Please type your username: ")
                    if all(not data[name]["Username"] == username for name in range(len(data))):
                        print("\n{name} does not exist.".format(name = username))
                    else:
                        select = False
                        print("\nWelcome back, {name}.".format(name = username))
                        player_data = player_stats(username, data)
                        print("---------\nScore: {score}\nWins: {wins}\nLost: {lost}\n---------".format(
                            score=player_data[0], wins=player_data[1], lost=player_data[2]
                            ))
                        
                        hangman(dino=random_word())
                            

            elif option == 2:
                create = True
                while create == True:

                    username = input("Please create a username: ")
                    username.strip().lower()

                    if all(not data[name]["Username"] == username for name in range(len(data))):
                        create_player(username)
                        create = False
                    else:
                        print("\nUsername already taken.")
                        
            

            else:
                print("Option not recognised.")
            
        elif play == "n":
            end()
        else:
            print("Option not recognised.")
main()

