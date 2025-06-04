from random import *

N = randint(1, 10)
lives = 3

while lives > 0:
    print("Осталось жизней:", lives)
    print("Какое число загадано?")
    user_answer = int(input())
    if user_answer < 1 or user_answer > 10:
        print("Число должно быть от 1 до 10 включительно.")
    elif user_answer == N:
        print("Победа")
        break
    elif N > user_answer:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
    lives -= 1

print("Было загадано число", N)
print("Конец игры.")