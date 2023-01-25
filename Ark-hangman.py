# main executable for game
import csv
import random
import json
from tempfile import NamedTemporaryFile
import shutil

class Player:
    def __init__(self, username, score = 0, games_won = 0, games_lost = 0):
        self.username = username
        self.score = score
        self.games_won = games_won
        self.games_lost = games_lost
        self.player_dict = {
            "username":self.username, "score":self.score, "games_won": self.games_won, "games_lost": self.games_lost
            }

    def update_stats(self):
        data = find_data()
        user_data = [data[i] for i in range(len(data)) if data[i]["Username"] == self.username]
        user_data = user_data[0]
        old_score = int(user_data["Score"])
        old_games_won = int(user_data["Games Won"])
        old_games_lost = int(user_data["Games Lost"])
        headers = ["Username", "Score", "Games Won", "Games Lost"]
        tempfile = NamedTemporaryFile(mode="w", delete = False)
        with open("players.csv", "r") as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=headers)
            writer = csv.DictWriter(tempfile, fieldnames=headers)
            for row in reader:
                if row['Username'] == self.username:
                    row['Username'], row['Score'], row['Games Won'], row["Games Lost"] = self.username, self.score+old_score, self.games_won+old_games_won, self.games_lost+old_games_lost
                row = {'Username': row['Username'], 'Score': row['Score'], 'Games Won': row['Games Won'], 'Games Lost': row['Games Lost']}
                writer.writerow(row)
        shutil.move(tempfile.name, "players.csv")
        
def find_data():
    # Reads CSV file and stores each line in the data list
    players = open("players.csv")
    players_dict_file = csv.DictReader(players)
    data = []
    for row in players_dict_file:
        data.append(row)
    return data

data = find_data()

def create_player(username):
    # creates a player dict using Player class and the writes it to the CSV file
    global player
    player = Player(username)
    with open("players.csv", "a", newline="") as f:
        headersCSV = [i for i in player.player_dict.keys()]
        entries = csv.DictWriter(f, fieldnames=headersCSV)
        entries.writerow(player.player_dict)
        f.close()





def player_stats(username, data):
    # finds player data from csv file and returns it
    player_data = []
    for i in data:
        if i["Username"] == username:
            player_data.append(i["Score"])
            player_data.append(i["Games Won"])
            player_data.append(i["Games Lost"])
            break
    return player_data

def end():
    # exit out of program
    print("\nGood Bye, thank you for playing.")
    exit()

def random_word():
    # finds a random word from the dinos.txt file
    with open("dinos.txt", "r") as f:
        dinos = f.readlines()
        word = dinos[random.randrange(0, len(dinos))]
        return word.strip("\n")

def hangman(dino):
    # main logic of game
    global current_score, games_won, games_lost
    games_won = 0
    games_lost = 0
    current_score = 0
    incorrect_guesses = 0
    with open("hangman.json", "r") as f:
        figure = json.load(f)
    win = False
    print("\nLets Play Hangman!\n")
    board = ["_"]*len(dino)
    letters = list(dino)
    
    # replaces spaces in the board with actual spaces and ticks them off
    space = " "
    if space in dino:
        space_index = letters.index(space)
        board[space_index] = space
        letters[space_index] = "%"
    print((" ".join(board)))
    # main game loop
    while incorrect_guesses < len(figure):
        guess = input("\nGuess a letter: ")
        if guess in letters:
            while guess in letters:
                guess_index = letters.index(guess)
                board[guess_index] = guess
                letters[guess_index] = "%"
                current_score += 10
        elif guess == "end":
            break
        else:
            incorrect_guesses += 1
            # prints hangman image
            print("\n\n\n '{letter}' was not correct!".format(letter=guess))
            print("\n{image}".format(image=figure[str(incorrect_guesses)]))
        
        print((" ".join(board)))
        print("Score:",current_score)
        if "_" not in board or guess == dino:
            print("\nYou win! It was:\n {dino}!\n".format(dino=dino.title()))
            win = True
            current_score += 120-(incorrect_guesses*10)
            games_won += 1
            print("Score:",current_score)
            return
            
    if not win:
        print("\nGame Over! Word was: \n{dino}\n".format(dino=dino.title()))
        games_lost += 1
        return
    

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
                        play = True
                        while play == True:
                            hangman(dino=random_word().lower())
                            new_stats = Player(username, current_score, games_won, games_lost)
                            new_stats.update_stats()
                            again = input("\nPlay Again?(y/n): ")
                            if again == "n":
                                play = False
                                end()
                            else:
                                continue
                            
            elif option == 2:
                create = True
                while create == True:

                    username = input("Please create a username: ")
                    username.strip().lower()

                    if all(not data[name]["Username"] == username for name in range(len(data))):
                        create_player(username)
                        create = False
                        print("\nWelcome to hangman, {name}.".format(name=username))
                        play = True
                        while play == True:
                            hangman(dino=random_word().lower())
                            new_stats = Player(username, current_score, games_won, games_lost)
                            new_stats.update_stats()
                            again = input("\nPlay Again?(y/n): ")
                            if again == "n":
                                play = False
                                end()
                            else:
                                continue

                    else:
                        print("\nUsername already taken.")
                        
            else:
                print("Option not recognised.")
            
        elif play == "n":
            end()
        else:
            print("Option not recognised.")
main()

