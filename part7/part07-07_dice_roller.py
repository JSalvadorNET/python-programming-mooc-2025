import string
import random
from random import choice, randint

def roll(die: str):
    sequency = ""
    dice_A = "333336"
    dice_B = "222555"
    dice_C = "144444"
    if die == "A":
        num = (random.choice(dice_A)) 
        sequency += num
    elif die == "B":
        num = (random.choice(dice_B)) 
        sequency += num
    elif die == "C":
        num = (random.choice(dice_C)) 
        sequency += num
    return int(sequency)
    
def play(die1: str, die2: str, times: int):
    dice1_won = 0
    dice2_won = 0
    dice_tie = 0
    
    for _ in range(times):
        result1 = roll(die1)  
        result2 = roll(die2)  
        
        if result1 > result2:
            dice1_won += 1
        elif result2 > result1:
            dice2_won += 1
        else:
            dice_tie += 1
    return (dice1_won, dice2_won, dice_tie)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)