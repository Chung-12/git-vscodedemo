from sys import argv
from random import randint

start = int(argv[1])
end = int(argv[2])

goal_num = randint(start, end)
guess_num = int(input(f"Guess a Number between {start} {end} "))

while True:
    if goal_num == guess_num:
        print("YOu won the Game")
        break
    elif goal_num > guess_num:
        guess_num = int(input("Guess higher "))
    else:
        guess_num = int(input("Guess lower "))

