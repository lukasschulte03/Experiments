from dis import dis
import random

print(" \n ")

numbers = [1,2,3,1]
 
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
    player = random.randint(1,3)
    opponent = random.randint(1,3)
    print("player chose: " + dic[player])
    print("opponent chose: " + dic[opponent])
    print(str(winner(player - 1, opponent - 1)))
    print(" \n ")

    answer = input("Play again? y/n: ") 
    if answer != "y":
        break
