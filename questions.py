# Посчитать количество попыток, которые потратил пользователь
# и вывести количество попыток в конце
question = "Какой сегодня месяц?"
right_answer = "июнь"

print(question)
user_answer = input()
attempts = 1
lives = 3

while user_answer != right_answer and lives > 0:
    lives -= 1
    print("Wrong! Try again.")
    user_answer = input()
    attempts += 1

if user_answer == right_answer:
    print("Well done!")
else:
    print("You lost all of your lives")

'''
if user_answer == right_answer:
    print("Well done!")
else:
    print("Too bad.")
'''
