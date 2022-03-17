import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
 
dic = {
    1 : "rock",
    2 : "paper",
    3 : "scissors",
}

def LineSpam(amount):
    for i in range(amount):
        print(" \n ")

def winner(p1, p2, p1name, p2name):
        if (p1 +1) % 3 == p2:
            return "\n" + color.YELLOW + color.BOLD + p2name + color.END + " won!"
        elif p1 == p2:
            return "\n" + color.GREEN + color.BOLD + "It is a draw!" + color.END
        else:
            return "\n" + color.PURPLE + color.BOLD + p1name + color.END + " won!"
 
def ComputerGame():
    while True:
        opponent = random.randint(1,3)
        LineSpam(50)
        player = input("Choose: ("+color.BOLD+"1"+color.END+")Rock, ("+color.BOLD+"2"+color.END+")Paper, ("+color.BOLD+"3"+color.END+")Scissors: ") 
        while player not in ["1", "2", "3"]:
            player = input("Invalid input, choose: ("+color.BOLD+"1"+color.END+")Rock, ("+color.BOLD+"2"+color.END+")Paper, ("+color.BOLD+"3"+color.END+")Scissors: ") 
        player = int(player)
        LineSpam(50)
        print("\nplayer chose: " + dic[player])
        print("opponent chose: " + dic[opponent])
        print(str(winner(player - 1, opponent - 1, "Player", "Opponent")))
        answer = input("\nPlay again? "+color.BOLD+"y/n"+color.END+": ") 
        if answer.lower() == "y" or answer.lower() == "yes":
            continue
        else:
            break

def versus():
    while True:
        LineSpam(50)
        player1 = input("Player 1, Choose: ("+color.BOLD+"1"+color.END+")Rock, ("+color.BOLD+"2"+color.END+")Paper, ("+color.BOLD+"3"+color.END+")Scissors: ") 
        while player1 not in ["1", "2", "3"]:
            player1 = input("Invalid input, choose: ("+color.BOLD+"1"+color.END+")Rock, ("+color.BOLD+"2"+color.END+")Paper, ("+color.BOLD+"3"+color.END+")Scissors: ") 
        player1 = int(player1)
        LineSpam(50)
        player2 = input("Player 2, Choose: ("+color.BOLD+"1"+color.END+")Rock, ("+color.BOLD+"2"+color.END+")Paper, ("+color.BOLD+"3"+color.END+")Scissors: ") 
        while player2 not in ["1", "2", "3"]:
            player2 = input("Invalid input, choose: ("+color.BOLD+"1"+color.END+")Rock, ("+color.BOLD+"2"+color.END+")Paper, ("+color.BOLD+"3"+color.END+")Scissors: ") 
        player2 = int(player2)
        LineSpam(50)
        print("\nplayer 1 chose: " + dic[player1])
        print("player 2 chose: " + dic[player2])
        print(str(winner(player1 - 1, player2 - 1, "Player 1", "Player 2")))
        answer = input("\nPlay again? "+color.BOLD+"y/n"+color.END+": ") 
        if answer.lower() == "y" or answer.lower() == "yes":
            continue
        else:
            break

LineSpam(50)

answer = input("\nPlay ("+color.BOLD+"1"+color.END+")2v2 or ("+color.BOLD+"2"+color.END+")vs Computer: ")
while answer not in ["1", "2"]:
        answer = input("Invalid input, choose: ("+color.BOLD+"1"+color.END+")2v2 or ("+color.BOLD+"2"+color.END+")vs Computer: ") 
if answer == "1":
    versus()
elif answer == "2":
    ComputerGame()
else:
    quit()


