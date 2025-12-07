print("Угадайте число, которое загадала машина")
import random
number = random.randint(1, 10)
attempts = 3
guessed = False
for i in range(1, attempts+1):
    guess = int(input())
    if guess == number:
        print("Угадали")
        guessed = True
        break
    else:
        print("Неверно")
        if guess < number:
            print("Больше")
        else:
            print("Меньше")
if not guessed:
    print(f"Было загадано число {number}")