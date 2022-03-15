import random
 
dic = {
    1 : "rock",
    2 : "paper",
    3 : "scissors",
}

def winner(p1, p2):
        if (p1 +1) % 3 == p2:
            return "\nOpponent won!"
        elif p1 == p2:
            return "\nIt is a draw!"
        else:
            return "\nPlayer won!"

while True:
    opponent = random.randint(1,3)
    print("\n---------------------------------------------\n")
    player = input("Choose: (1)Rock, (2)Paper, (3)Scissors: ") 
    while player not in ["1", "2", "3"]:
        player = input("Invalid input, choose: (1)Rock, (2)Paper, (3)Scissors: ") 
    player = int(player)
    print("\nplayer chose: " + dic[player])
    print("opponent chose: " + dic[opponent])
    print(str(winner(player - 1, opponent - 1)))
    answer = input("\nPlay again? y/n: ") 
    if answer.lower() == "y" or answer.lower() == "yes":
        continue
    else:
        break
